"""Faça um programa que implemente o jogo do par-ou-ímpar. O programa deve ler um número correspondente à 
jogada do jogador 1 e outro número correspondente ao jogador 2. Caso a soma dos números seja ímpar, 
o jogador 1 venceu; caso seja par, o jogador 2 venceu. Escreva quem venceu."""


jogador1 = int(input("Você é o jogador ímpar, digite um número: "))
jogador2 = int(input("Você é o jogador par, digite um número: "))

    
resultado = jogador1 + jogador2

if  (resultado % 2 != 0):
    print(f"A soma dos números deu o resultado {resultado} que é ímpar, sendo assim o jogador 1 ganhou")
        
else:
    print(f"A soma dos números deu o resultado {resultado} que é par, sendo assim o jogador 2 ganhou")
          