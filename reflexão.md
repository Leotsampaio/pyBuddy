# Reflexão — PyBuddy: Tutor de Python para Iniciantes

## 1. Decisões de design do prompt

**Por que escolhi esse domínio?**
[Escreva aqui sua justificativa — ex: relevância para o grupo de IA, domínio que você conhece, utilidade prática...]

**Quais elementos do system prompt foram mais difíceis de definir?**
[Ex: delimitar o escopo, definir o tom, escrever o exemplo few-shot...]

**O que você testou e mudou?**
[Ex: "A primeira versão do prompt não tinha o exemplo de conversa, e o agente ficava muito
formal. Adicionei o few-shot e o tom ficou mais próximo do que eu queria."]

---

## 2. Uma coisa que funcionou e uma que não funcionou

**O que funcionou bem:**

Conversa de exemplo:
```
Você: O que é uma lista em Python?
PyBuddy: Lista é uma coleção ordenada de valores que você pode mudar depois de criar.
         Exemplo: frutas = ["maçã", "banana", "laranja"]. Você consegue acessar qualquer
         item pelo índice, como frutas[0] que retorna "maçã". Tenta criar uma lista com
         suas comidas favoritas e me mostra!
```
[Comente por que funcionou — o agente seguiu o tom? Usou exemplo concreto? Incentivou prática?]

**O que não funcionou:**

Conversa de exemplo:
```
Você: [sua pergunta aqui]
PyBuddy: [resposta problemática aqui]
```
[Comente o que causou o problema — ambiguidade no prompt? Falta de instrução? Limitação do modelo?]

---

## 3. O que eu faria com mais tempo

[Ex: Adicionaria uma ferramenta de execução de código para o agente poder testar os
exemplos em tempo real. Ou: Refinaria o prompt para o agente detectar o nível do aluno
automaticamente nas primeiras mensagens.]

---

*Nota: Usei o Claude (claude.ai) para auxiliar na estrutura inicial do projeto e dos
comentários do código. A compreensão e adaptação do conteúdo gerado são de minha responsabilidade.*