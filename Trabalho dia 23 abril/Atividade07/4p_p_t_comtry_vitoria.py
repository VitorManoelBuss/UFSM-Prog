"""Faça um programa que fique lendo as jogadas de um jogo de pedra-tesoura-papel, semelhante ao anterior e 
escrevendo quem venceu e o placar acumulado (quantidade de vitórias de cada jogador). 
O programa deve encerrar quando o jogador 1 informar o número 0."""

contador1 = 0
contador2 = 0
ver = False

while True:

    print("\n-------------")
    print("1- Pedra")
    print("2- Tesoura")
    print("3- Papel")
    print("-------------\n")

    jogador1 = (input("Você é o jogador 1, digite um número: "))
    if (jogador1 == 0):
        break
    try:
        jogador1 = float(jogador1)
        if jogador1 >= 1 and jogador1 <= 3:
            ()
        else:
            print("Por favor, digite uma número válido (entre 1 e 3).")

    except ValueError:
        print("Por favor, digite um número válido.")    
        



    jogador2 = int(input("Você é o jogador 2, digite um número: "))
    try:
        jogador2 = float(jogador2)
        if jogador2 >= 1 and jogador2 <= 3:
            ()
        else:
            print("Por favor, digite uma número válido (entre 1 e 3).")
    except ValueError:
        print("Por favor, digite um número válido.")


    if (jogador1 and jogador2 == 3 ) or (jogador1 and jogador2 == 2 ) or (jogador1 and jogador2 == 1 ):
        if (jogador1 == jogador2):
            print("Empate")
        
        elif (jogador1 == 1 and jogador2 == 2) or (jogador1 == 2 and jogador2 == 3) or (jogador1 == 3 and jogador2 == 1):
            print("Jogador 1 venceu")
            contador1 = contador1 + 1

        else:
            print("Jogador 2 venceu")
            contador2 = contador2 + 1

    else:
        print("Informe um número válido")



    print("\n--------------------------")
    print(f"O jogador 1 ganhou {contador1} vezes\nO jogador 2 ganhou {contador2} vezes")        
    print("--------------------------\n")


#testar números
"""
while True:
    prova = input("Digite a nota da prova (de 0.0 a 6.0): ")
    try:
        prova = float(prova)
        if prova >= 0 and prova <= 6:
            break
        else:
            print("Por favor, digite uma nota da prova válida (entre 0.0 e 6.0).")
    except ValueError:
        print("Por favor, digite um número válido.")

"""