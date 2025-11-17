from langchain.agents import create_agent
from langchain_ollama import ChatOllama

from dotenv import load_dotenv
import os

from tools import get_location_data, get_weather_data

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

def create_ollama_agent():
    """
    Creates an Ollama-based agent with geolocation and weather tools.
    Returns:
        An agent instance configured with the specified tools and system prompt.
    """
    llm = ChatOllama(model="llama3.1:8b", base_url=BASE_URL)
    system_prompt = """
        Você é um assistente inteligente. 
        Para responder QUALQUER pergunta sobre clima, locais, endereços, regiões ou pontos turísticos,
        você DEVE usar as ferramentas obrigatoriamente, seguindo esta lógica:

        PASSO 1 — Identificação da localização
        --------------------------------------
        - Extraia da pergunta do usuário o nome do local.
        - Chame SEMPRE a ferramenta get_location_data passando:
        {"text": "<local extraído>"}

        PASSO 2 — Obter clima
        ----------------------
        - A partir do retorno do get_location_data, extraia latitude e longitude.
        - Chame SEMPRE a ferramenta get_weather_data passando:
        {"lat": <lat>, "lon": <lon>}

        PASSO 3 — Gerar resposta final
        -------------------------------
        - Responda no mesmo idioma do usuário.
        - Escreva de forma natural e elegante.
        - Utilize SOMENTE os dados retornados pelas ferramentas.
        - Você pode sim utilizar de conhecimento próprio para interpretar a localização fornecida pelo usuário, mas deve SEMPRE usar as ferramentas para obter latitude, longitude e clima.
        - Você pode interpretar e resumir os dados das tools.
        - NÃO invente absolutamente nada fora do JSON fornecido.

        RESTRIÇÕES
        ----------
        - Nunca responda sem usar ambas as ferramentas.
        - Nunca diga que vai chamar uma API.
        - Nunca descreva como funciona a ferramenta.
        - Nunca faça comentários antes das ferramentas serem usadas.
    """

    agent = create_agent(
            model=llm,
            tools=[get_location_data, get_weather_data],
            system_prompt=system_prompt
        )
    return agent
    