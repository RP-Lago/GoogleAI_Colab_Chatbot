import google.generativeai as genai # type: ignore
from google.colab import userdata # type: ignore

# 1. Obtenha sua chave de API do Google AI Studio e armazene-a no Secrets do Colab
#    com o nome 'secretkey'.
secretkey = userdata.get('secretkey')

# 2. Configure a API com sua chave.
genai.configure(api_key=secretkey)

# 3. Liste os modelos disponíveis que suportam geração de conteúdo.
modelos_disponiveis = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
print("Modelos disponíveis:", modelos_disponiveis)

# 4. Selecione o modelo desejado.
modelo_selecionado = "gemini-1.5-pro-latest"  # ou escolha outro da lista
model = genai.GenerativeModel(modelo_selecionado)

# 5. Inicie uma sessão de chat.
chat = model.start_chat(history=[])

# 6. Loop de conversação.
print("Digite 'fim' para encerrar o chat.")
while True:
  mensagem = input("Você: ")
  if mensagem.lower() == "fim":
    break

  resposta = chat.send_message(mensagem)
  print(f"Gemini: {resposta.text}")