# 🎮 Jokenpô Interativo em Python

Este é o **meu primeiro projeto de desenvolvimento**! Desenvolvi este jogo clássico de Pedra, Papel e Tesoura para consolidar os fundamentos da lógica de programação e aplicar estruturas de controle de fluxo de forma prática.

O projeto foi construído do zero, focando na experiência de jogo via terminal, tratamento de exceções e interatividade contínua com o usuário.

---

## 🛠️ Tecnologias e Recursos Utilizados
* **Linguagem:** Python 3
* **Biblioteca `random` (`randint`):** Utilizada para gerar a escolha aleatória do computador de 0 a 2.
* **Biblioteca `time` (`sleep`):** Aplicada para criar pausas dramáticas (`JO`, `KEN`, `PO!!!`) antes da exibição dos resultados.
* **Tuplas:** Uso da estrutura de dados imutável `itens` para mapear os índices numéricos aos textos ("Pedra", "Papel", "Tesoura").

---

## 🧠 Lógica e Estrutura do Código
O software foi desenhado seguindo as seguintes boas práticas de lógica:

* **Laço de Repetição Infinito (`while True`):** Permite que o jogo rode continuamente até que o usuário decida encerrar ativamente.
* **Tratamento de Erros de Entrada (`try/except ValueError`):** Proteção do sistema contra quebras indesejadas caso o jogador digite letras ou símbolos em vez de números.
* **Validação de Intervalo:** Filtro condicional que impede jogadas menores que 0 ou maiores que 2, reiniciando o fluxo com instruções claras.
* **Estrutura Condicional Aninhada:** Árvore de decisão otimizada com `if/elif` mapeando todas as combinações possíveis entre o jogador e a máquina.

---

## 🗺️ Roadmap de Evolução (Próximos Passos)
Para dar continuidade ao meu aprendizado e evolução deste repositório, planejo as seguintes melhorias:

- [ ] **Interface Gráfica com Botões:** Migrar o jogo do terminal para uma interface visual intuitiva, facilitando a escolha do usuário com cliques.
- [ ] **Validação Avançada no Loop Final:** Refinar o menu de reinicialização para tratar entradas inválidas além das opções "S" e "N".
- [ ] **Contador de Placar:** Implementar variáveis para persistir o histórico de vitórias do jogador e do computador durante a sessão.

---

## ⚙️ Como Executar o Jogo

### Pré-requisitos
Você precisará ter o **Python 3** instalado em sua máquina.

### Passo a Passo
1. Baixe ou clone os arquivos deste repositório.
2. Abra o terminal (ou Prompt de Comando) na pasta onde salvou o código.
3. Execute o comando:
   ```bash
   python minigame jokenpo.py
   ```
---

## 👤 Autor
* **Pedro Elton Silva do Nascimento**
* Vamos nos conectar? [Meu LinkedIn](https://www.linkedin.com/in/pedro-elton-silva-do-nascimento-b43622111/)
