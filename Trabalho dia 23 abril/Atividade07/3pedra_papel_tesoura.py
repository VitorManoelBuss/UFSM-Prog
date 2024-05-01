"""Faça um programa que implemente o jogo pedra-tesoura-papel. O programa deve ler a opção de jogada do 
jogador 1 e do jogador 2, com as opções: 1-Pedra, 2-Tesoura, 3-Papel. Se as opções forem iguais, dá empate, 
caso contrário, pedra vence tesoura, tesoura vence papel e papel vence pedra. Escreva quem venceu a partida.
"""



while True:
    
    print("\n-------------")
    print("1- Pedra")
    print("2- Tesoura")
    print("3- Papel")
    print("-------------\n")

    jogador1 = int(input("Você é o jogador 1, digite um número: "))
    jogador2 = int(input("Você é o jogador 2, digite um número: "))


    if (jogador1 and jogador2 == 3 ) or (jogador1 and jogador2 == 2 ) or (jogador1 and jogador2 == 1 ):
        
        if (jogador1 == jogador2):
            print("Empate")
        
        elif (jogador1 == 1 and jogador2 == 2) or (jogador1 == 2 and jogador2 == 3) or (jogador1 == 3 and jogador2 == 1):
            print("Jogador 1 venceu")

        else:
            print("Jogador 2 venceu")

    else:
        print("Informe um número válido")


