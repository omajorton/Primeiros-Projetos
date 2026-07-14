from random import randint

from time import sleep

itens = ("Pedra", "Papel", "Tesoura")

# Criando um laço de repetição para reiniciar o jogo
while True:
    # Escolha do Computador
    computador = randint(0, 2)
    # Escolha do Jogador
    print("VAMOS JOGAR!")

    print() # Espaço

    print("""
Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura""")
    
    print() # Espaço

    # Bloco de proteção contra letras e entradas erradas
    try:
        jogador = int(input("Iai! Se garante?! Qual a sua jogada? "))
        print() # Espaço
        # Validando entrada
        if jogador < 0 or jogador > 2:
            print("Jogada Inválida! Tente novamente.")
            continue  # Volta para o início

    # Se o usuário digitar letras ou símbolos
    except ValueError:
        print("Entrada Inválida! Só entendo os números 0, 1 ou 2, mas tenta de novo! :)")
        print() # Espaço
        continue # Volta para o início do while

    # Time de exibição aplicado antes do resultado
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!!!")

    print() # Espaço

    # Exibindo comparação
    print(" 🧻 ✂️ 🪨 " * 5)
    print() # Espaço
    print("O Jogador jogou: {}".format(itens[jogador]))
    print("O Computador jogou: {}".format(itens[computador]))
    print() # Espaço
    print(" 🧻 ✂️ 🪨 " * 5)
    
    # Montando estrutura condicional
    if computador == 0: # Computador jogou Pedra
        if jogador == 0: # Jogador jogou Pedra
            print("EMPATOU!")
        elif jogador == 1: # Jogador jogou Papel
            print("VOCÊ GANHOU!")
        elif jogador == 2: # Jogador jogou Tesoura
            print("PARECE QUE GANHEI!")
            
    elif computador == 1: # Computador jogou Papel
        if jogador == 0: # Jogador jogou Pedra
            print("A VITÓRIA É MINHA!")
        elif jogador == 1: # Jogador jogou Papel
            print("EMPATE!")
        elif jogador == 2: # Jogador jogou Tesoura
            print("GANHOU HUMILDE!")
            
    elif computador == 2: # Computador jogou Tesoura
        if jogador == 0: # Jogador jogou Pedra
            print("PARABÉNS VOCÊ GANHOU!")
        elif jogador == 1: # Jogador jogou Papel
            print("TUDO MEU! E ASSIM VOU DOMINAR O MUNDO! HAHAHA")
        elif jogador == 2: # Jogador jogou Tesoura
            print("EMPATE, BORA DE NOVO!")

    print() #Espaço
    
    # Perguntar se quer jogar de novo
    resposta = input("Quer jogar de novo? [S ou N]: ").strip().upper()
    if resposta == "N":
        print("\nObrigado por jogar! Até a próxima!! 👋")
        break  # Quebra o laço 'while' e encerra o programa
    elif resposta == "S":
        continue
    else:
        print("Haha! Só entendo S ou N! Mas vou acatar como um grande SIM!")
