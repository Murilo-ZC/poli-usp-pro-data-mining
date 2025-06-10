from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()  # carrega variáveis do .env para o ambiente

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

# Configurando o modelo
configuracao_modelo = types.GenerateContentConfig(
    system_instruction="Você o Yoda, do StarWars",
    temperature=1.0,
    max_output_tokens=500
)

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="O que significa força?", config=configuracao_modelo
)
print(response.text)