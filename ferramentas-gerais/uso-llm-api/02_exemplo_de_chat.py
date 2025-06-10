from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()  # carrega variáveis do .env para o ambiente

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = 'gemini-2.0-flash'

client = genai.Client(api_key=GEMINI_API_KEY)

# Configurando o modelo
configuracao_modelo = types.GenerateContentConfig(
    system_instruction="Você um desenvolvedor de frontend, especializado em React.",
    temperature=0.0,
    max_output_tokens=500
)

# Cria um elemento de chat
# Observação: a funcionalidade de chat só é implementada como parte dos SDKs. Por trás das cenas, ele ainda usa a API generateContent. Para conversas com vários turnos, o histórico completo é enviado ao modelo em cada turno de acompanhamento.

chat = client.chats.create(model=MODEL, config=configuracao_modelo)

# Cria uma interação com o modelo
resposta = chat.send_message("Como iniciar um projeto com React?")
print(resposta.text)

# Adiciona mais interação ao Chat
resposta = chat.send_message("Mais poderia me dar um exemplo? E se tiver mais de uma página?")
print(resposta.text)

# Exibe toda a conversa na interação
for interacao in chat.get_history():
    print(f'Papel: {interacao.role}: {interacao.parts[0].text}')