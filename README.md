# PyBuddy — Tutor de Python para Iniciantes

Agente conversacional que responde dúvidas de Python para iniciantes,
construído com a API gratuita do Google Gemini.

## Como rodar

**1. Instale as dependências:**
```bash
pip install google-generativeai python-dotenv
```

**2. Configure sua chave da API:**

Renomeie o arquivo `.env.example` para `.env` (ou crie um `.env`) e cole sua chave:
```
GEMINI_API_KEY=sua_chave_aqui
```
Pegue sua chave gratuita em: https://aistudio.google.com/

**3. Execute o agente:**
```bash
python agent.py
```

## Estrutura do projeto
```
├── agent.py          # Código do agente
├── system_prompt.txt # Prompt que define o comportamento do agente
├── reflexao.md       # Reflexão escrita sobre as decisões de design
├── .env              # Sua chave de API (não sobe pro GitHub)
└── .gitignore        # Garante que o .env não seja commitado
```

## Observações
- O agente mantém o histórico da conversa enquanto estiver rodando
- Para encerrar, digite `sair`
- Perguntas fora do escopo de Python para iniciantes são recusadas educadamente