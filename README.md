# 🌍 Ollama GeoWeather Agent

An intelligent agent that answers questions about **geographical locations** and **weather conditions**, powered by **Ollama**, **LangChain**, and real-time geolocation + weather APIs.

The agent automatically:
1. Extracts the location from the user question  
2. Fetches geolocation information using **GeoApify**  
3. Fetches weather information using **wttr.in**  
4. Generates a natural-language answer in the same language as the user  

---

## 🚀 Features

- 🔧 **Custom LangChain Tools** (geolocation + weather)  
- 🌦️ **Real-time weather data** via wttr.in  
- 🗺️ **Accurate location data** from GeoApify  
- 🤖 **Ollama local LLM** (`llama3.1:8b`)  
---

## 💡 Example Questions

### ❓ "Vai chover na Avenida Paulista hoje?"
**Answer:**  
"Baseado nas informações obtidas, não há chance de chuva na Avenida Paulista hoje.  
O tempo estará com 75% de cobertura de nuvens e uma temperatura de 24°C.  
Além disso, há uma possibilidade de precipitação de 0,3 mm."

---

### ❓ "Como está o clima no Parque Ibirapuera, São Paulo?"
**Answer:**  
"O clima no Parque Ibirapuera, em São Paulo, está com temperaturas de 24°C  
e umidade do ar de 83%. Há chances de chuva leve.  
É recomendável levar protetor solar."
