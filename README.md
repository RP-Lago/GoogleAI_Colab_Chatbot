# Google Generative AI Chatbot 🌟

Este projeto demonstra como usar a biblioteca `google-generativeai` para criar um chatbot interativo com modelos de IA generativa do Google, como o **Gemini**. O chatbot suporta uma interação contínua usando a API do Google Generative AI.

## 🛠 Requisitos

- **Google Colab** ou ambiente Python local.
- Uma **chave de API do Google Generative AI** (obtenha no [Google AI Studio](https://studio.ai.google/)).
- Biblioteca `google-generativeai` instalada.

## 🚀 Instalação

1. Instale a biblioteca necessária:
   ```bash
   pip install google-generativeai==2.0.0
   ```

2. Configure sua chave de API no Colab:
   - No menu do Colab, acesse **Ambiente de execução > Gerenciar chaves de API e credenciais**.
   - Adicione sua chave de API como `secretkey`.

3. Copie o código do projeto para seu ambiente.

## 📜 Uso

1. Configure sua chave de API no código:
   ```python
   secretkey = userdata.get('secretkey')
   genai.configure(api_key=secretkey)
   ```

2. Liste os modelos disponíveis:
   ```python
   modelos_disponiveis = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
   print("Modelos disponíveis:", modelos_disponiveis)
   ```

3. Selecione um modelo (por exemplo, `gemini-1.5-pro-latest`) e inicie a sessão de chat:
   ```python
   chat = model.start_chat(history=[])
   ```

4. Interaja com o chatbot:
   - Digite suas mensagens e receba respostas da IA.
   - Digite `fim` para encerrar a conversa.

## 🖥 Exemplo de Saída

```
Digite 'fim' para encerrar o chat.
Você: Olá, tudo bem?
Gemini: Olá! Estou aqui para ajudar. Como posso assisti-lo hoje?
Você: O que você sabe sobre inteligência artificial?
Gemini: Inteligência artificial é um campo fascinante que busca criar sistemas capazes de realizar tarefas que normalmente exigem inteligência humana, como aprendizado e tomada de decisões.
Você: fim
```

## 🔒 Segurança

Certifique-se de manter sua chave de API segura. Evite compartilhá-la publicamente e use mecanismos como variáveis de ambiente ou `userdata` no Colab.

## 📖 Recursos Adicionais

- [Documentação oficial da biblioteca](https://github.com/google/generative-ai-python)
- [Google AI Studio](https://studio.ai.google/)

## ✨ Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

---

Feito com ❤️ por [RP-Lago](https://github.com/RP-Lago). 🎉
```