# Implementação de recurso de chat manualmente.
from google import genai
from google.genai import types
from google.genai.types import (
    Content,
    Part,
    GenerateContentConfig
)
import os
from dotenv import load_dotenv

load_dotenv()  # carrega variáveis do .env para o ambiente

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = 'gemini-2.0-flash'

client = genai.Client(api_key=GEMINI_API_KEY)

# Pergunta do usuário
pergunta = Content(
    role='user',
    parts=[Part(text="Como criar um projeto de front?")]
)

# Adiciona a mensagem
historico = [pergunta]

# Configurando o modelo
configuracao_modelo = types.GenerateContentConfig(
    system_instruction="Você um desenvolvedor de frontend, especializado em React.",
    temperature=0.0,
    # max_output_tokens=500
)

response = client.models.generate_content(
    model="gemini-2.0-flash", 
    contents=historico,
    config=configuracao_modelo
)

# Reunindo as partes para gerar o contexto
historico.append(
    Content(
        role='assistant',
        parts=[Part(text=response.text)]
    )
)

# Nova pergunta
historico.append(
    Content(
        role='user',
        parts=[Part(text="Pode me dar um exemplo?")]
    )
)

# Repete o processo

response = client.models.generate_content(
    model="gemini-2.0-flash", 
    contents=historico,
    config=configuracao_modelo
)

# Reunindo as partes para gerar o contexto
historico.append(
    Content(
        role='assistant',
        parts=[Part(text=response.text)]
    )
)

# Exibe a saída
for mensagem in historico:
    print('-------------')
    print(f'Role:{mensagem.role}')
    print(f'Texto:{mensagem.parts[0].text}')