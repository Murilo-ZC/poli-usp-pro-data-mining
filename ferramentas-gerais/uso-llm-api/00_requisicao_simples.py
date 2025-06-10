from google import genai
import os
from dotenv import load_dotenv

load_dotenv()  # carrega variáveis do .env para o ambiente

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="O que é Data Mining?"
)
print(response.text)