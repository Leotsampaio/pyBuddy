# Reflexão — PyBuddy: Tutor de Python para Iniciantes

## 1. Decisões de design do prompt

**Por que escolhi esse domínio?**
escolhi o tutor de python para iniciantes, pois hoje em dia saber uma linguagem de programação é quase obrigatorio, então pensando nisso, esse agente facilitaria o aprendizado disso.

**Quais elementos do system prompt foram mais difíceis de definir?**
delimitar o escopo, definir o tom e escrever o exemplo few-shot

**O que você testou e mudou?**
A primeira versão do prompt não tinha o exemplo de conversa, e o agente ficava muito
formal. Adicionei o few-shot e o tom ficou mais próximo do que eu queria.

---

## 2. Uma coisa que funcionou e uma que não funcionou

**O que funcionou bem:**

Conversas comuns
```
Você: O que é uma lista em Python?
PyBuddy: Lista é uma coleção ordenada de valores que você pode mudar depois de criar.
         Exemplo: frutas = ["maçã", "banana", "laranja"]. Você consegue acessar qualquer
         item pelo índice, como frutas[0] que retorna "maçã". Tenta criar uma lista com
         suas comidas favoritas e me mostra!
```

funcionou bem porque ta dando bons exemplos e de forma amigável

**O que não funcionou:**

Poderia ter uma conexão com uma interface html que acabou não sendo feito.

---

## 3. O que eu faria com mais tempo

Adicionaria uma ferramenta de execução de código para o agente poder testar os
exemplos em tempo real. 

---

*Nota: Usei o Claude (claude.ai) para auxiliar na estrutura inicial do projeto e dos
comentários do código. A compreensão e adaptação do conteúdo gerado são de minha responsabilidade.*