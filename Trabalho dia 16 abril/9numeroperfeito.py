"""Um número perfeito é um número inteiro positivo que é igual à soma de seus divisores próprios positivos, 
excluindo ele mesmo. Em outras palavras, um número perfeito é aquele cuja soma de seus divisores próprios 
(excluindo o próprio número) é igual ao próprio número.

Por exemplo, o número 6 é um número perfeito porque seus divisores próprios positivos são 1, 2 e 3, e a soma 
deles é 1 + 2 + 3 = 6. Outro exemplo é o número 28, cujos divisores próprios positivos são 1, 2, 4, 7 e 14, 
e a soma deles é 1 + 2 + 4 + 7 + 14 = 28.
Faça um programa que leia um número e escreva se o mesmo é um número perfeito ou não."""

num = int(input("Informe o número positivo e inteiro que você quer saber se é perfeito: "))

soma = 0

for i in range(1, num):
    if (num % i == 0):
        soma = soma + i



if (soma == num):
    print(f"O número {num} é perfeito")
else:
    print(f"O número {num} não é perfeito")