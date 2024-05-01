"""Faça um programa que escreva a soma dos números pares de 1 até 200"""


soma = 0

for i in range (1,201):
    if (i % 2 == 0):
        soma = soma + i
print(soma)


