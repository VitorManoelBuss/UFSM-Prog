"""Faça um programa que fique lendo as jogadas (com um while True no início) de um jogo de par ou ímpar 
semelhante ao anterior e escrevendo quem venceu e o placar acumulado (quantidade de vitórias de cada jogador). 
O programa deve encerrar quando o jogador 1 informar o número 0 (usar um break para interromper o while)."""

contador1 = 0
contador2 = 0

while True:

    jogador1 = int(input("Você é o jogador ímpar, digite um número: "))
    if (jogador1 == 0):
        break
    jogador2 = int(input("Você é o jogador par, digite um número: "))

            
    resultado = jogador1 + jogador2

    if  (resultado % 2 != 0):
        print(f"A soma dos números deu o resultado {resultado} que é ímpar, sendo assim o jogador 1 ganhou")
        contador1 = contador1 + 1
                
    else:
        print(f"A soma dos números deu o resultado {resultado} que é par, sendo assim o jogador 2 ganhou")
        contador2 = contador2 + 1
    


print(f"Vítorias do jogador 1: {contador1}\nVitórias do jogador 2: {contador2}")       
