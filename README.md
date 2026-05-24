# PyBuddy — Tutor de Python para Iniciantes

Agente conversacional que responde dúvidas de Python para iniciantes via terminal.
Construído com a API gratuita do Groq (modelo LLaMA 3.3 70B).

---

## Como rodar

**1. Clone o repositório:**
```bash
git clone https://github.com/SEU_USUARIO/agente-ia-estudos.git
cd agente-ia-estudos
```

**2. Crie e ative um ambiente virtual:**
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

**3. Instale as dependências:**
```bash
pip install groq python-dotenv
```

**4. Configure sua chave da API:**

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
```
GROQ_API_KEY=sua_chave_aqui
```
Pegue sua chave gratuita em: https://console.groq.com/

**5. Execute o agente:**
```bash
python agent.py
```

Para encerrar a conversa, digite `sair`.

---

## Estrutura do projeto

```
├── agent.py            # Código do agente
├── system_prompt.txt   # Prompt que define o comportamento do agente
├── reflexao.md         # Reflexão escrita sobre as decisões de design
├── .env                # Sua chave de API (não sobe pro GitHub)
├── .gitignore          # Garante que o .env não seja commitado
└── README.md           # Este arquivo
```

---

## Observações

- O agente mantém o histórico da conversa enquanto estiver rodando
- Perguntas fora do escopo de Python para iniciantes são recusadas educadamente
- A chave de API do Groq é gratuita e não exige cartão de crédito