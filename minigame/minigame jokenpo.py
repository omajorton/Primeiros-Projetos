from random import randint
from time import sleep

itens = ("Pedra", "Papel", "Tesoura")

# Criando laço de repetição para reiniciar o jogo
while True:

    # Zera o placar a cada novo jogo
    vitorias_jogador = 0
    vitorias_computador = 0

    # Enquanto ninguém tiver 2 vitórias
    while vitorias_jogador < 2 and vitorias_computador < 2:

        # Escolha do Computador
        computador = randint(0, 2)

        # Escolha do Jogador
        print("VAMOS JOGAR!")

        print()  # Espaço

        print("""
Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura""")

        print()  # Espaço

        # Bloco de proteção contra letras e entradas erradas
        try:
            jogador = int(input("Iai! Se garante?! Qual a sua jogada? "))
            print()

            # Validando entrada
            if jogador < 0 or jogador > 2:
                print("Jogada Inválida! Tente novamente.")
                continue

        # Se o usuário digitar letras ou símbolos
        except ValueError:
            print("Entrada Inválida! Só entendo os números 0, 1 ou 2, mas tenta de novo! :)")
            print()
            continue

        # Time de exibição aplicado antes do resultado
        print("JO")
        sleep(1)
        print("KEN")
        sleep(1)
        print("PO!!!")

        print()

        # Exibindo comparação
        print(" 🧻 ✂️ 🪨 " * 5)
        print()
        print(f"O Jogador jogou: {itens[jogador]}")
        print(f"O Computador jogou: {itens[computador]}")
        print()
        print(" 🧻 ✂️ 🪨 " * 5)

        # Montando estrutura condicional
        if computador == 0:  # Computador jogou Pedra
            if jogador == 0:
                print("EMPATOU!")
            elif jogador == 1:
                print("VOCÊ GANHOU!")
                vitorias_jogador += 1
            elif jogador == 2:
                print("PARECE QUE GANHEI!")
                vitorias_computador += 1

        elif computador == 1:  # Computador jogou Papel
            if jogador == 0:
                print("A VITÓRIA É MINHA!")
                vitorias_computador += 1
            elif jogador == 1:
                print("EMPATE!")
            elif jogador == 2:
                print("GANHOU HUMILDE!")
                vitorias_jogador += 1

        elif computador == 2:  # Computador jogou Tesoura
            if jogador == 0:
                print("PARABÉNS VOCÊ GANHOU!")
                vitorias_jogador += 1
            elif jogador == 1:
                print("Não sabia que eu era tão bom nesse jogo!!")
                vitorias_computador += 1
            elif jogador == 2:
                print("EMPATE, BORA DE NOVO!")

        print()
        print(f"PLACAR: VOCÊ: {vitorias_jogador} | COMPUTADOR: {vitorias_computador}")
        print()

    # Exibir vencedor
    if vitorias_jogador > vitorias_computador:
        print("🏆 PARABÉNS, VOCÊ GANHOU! FARMOU AURA BONITO!!!")
    else:
        print("💀 PEGA P@$A! E ASSIM VOU DOMINAR O MUNDO!!! HAHAHA")

    print()

    # Perguntar se quer jogar de novo
    while True:
        resposta = input("Quer jogar de novo? [S ou N]: ").strip().upper()

        if resposta == "S":
            print("\nBORA PRA MAIS UMA! 🔥\n")
            break

        elif resposta == "N":
            print("\nObrigado por jogar! Até a próxima!! 👋")
            exit()

        else:
            print("Haha! Só entendo S ou N! Tenta de novo. 😅")
