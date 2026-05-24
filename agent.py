import os
from groq import Groq
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Pega a chave da API do Groq
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    print("Erro: chave GROQ_API_KEY não encontrada no .env")
    exit(1)

# Lê o system prompt do arquivo separado
with open("system_prompt.txt", "r", encoding="utf-8") as f:
    system_prompt = f.read()

# Inicializa o cliente Groq
client = Groq(api_key=api_key)

# Modelo usado — llama-3.3-70b é o melhor disponível no plano gratuito do Groq
MODELO = "llama-3.3-70b-versatile"

# Histórico começa com o system prompt — ele fica fixo na posição 0
historico = [{"role": "system", "content": system_prompt}]

print("=" * 50)
print("  PyBuddy — Tutor de Python para Iniciantes")
print(f"  Modelo: {MODELO}")
print("=" * 50)
print("Digite sua dúvida sobre Python. Para sair, escreva 'sair'.\n")

while True:
    entrada = input("Você: ").strip()

    if entrada.lower() in ["sair", "exit", "quit"]:
        print("\nAté mais! Continue praticando Python. :)")
        break

    if not entrada:
        continue

    # Adiciona a mensagem do usuário ao histórico
    historico.append({"role": "user", "content": entrada})

    try:
        # Chama a API passando o histórico completo (inclui system prompt + conversa)
        resposta = client.chat.completions.create(
            model=MODELO,
            messages=historico
        )

        conteudo = resposta.choices[0].message.content

        # Adiciona a resposta ao histórico para manter o contexto nos próximos turnos
        historico.append({"role": "assistant", "content": conteudo})

        print(f"\nPyBuddy: {conteudo}\n")

    except Exception as e:
        print(f"\n[Erro ao chamar a API: {e}]\n")