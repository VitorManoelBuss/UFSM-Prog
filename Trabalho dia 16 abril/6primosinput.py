"""Faça um programa que escreva os números primos entre 1 e 50, juntamente com sua soma"""

num1 = int(input("Digite o primeiro número da lista que você quer saber: "))
num2 = int(input("Digite o último número da lista que você quer saber: "))

for i in range(num1, num2 + 1):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i)