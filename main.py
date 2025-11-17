from dotenv import load_dotenv
from agent import create_ollama_agent

load_dotenv()


def main():
    # Create the Ollama-based agent
    agent = create_ollama_agent()

    # Question
    question = input("Enter a question about a geographical location and weather: ")

    # Invoke the agent with the question and print the response
    response = agent.invoke({"messages": [{"role": "user", "content": question}]})
    print(response["messages"][-1].content)

if __name__ == "__main__":
    main()