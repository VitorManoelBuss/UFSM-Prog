"""Um número primo é aquele que possui somente 2 divisores: 1 e ele mesmo. Faça um programa que leia um número
e testa e escreve se ele é primo ou não."""

cont = 0
n = int(input("Informe o número que você gostaria de saber se é primo: "))

for i in range(1, n+1):
    if n % i == 0:
        cont = cont + 1

if cont==2:
    print(n, "é um número primo!")
else:
    print(n, "não é um número primo!")