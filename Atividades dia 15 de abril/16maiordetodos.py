""""Faça um programa que leia 10 números e escreva qual é o maior deles"""

maior = 0

for i in range (1,11):
    n = float(input("Digite um número: "))

    if (n > maior):
        maior = n

print(f"O maior núemro digitado foi: {maior:.2f}")