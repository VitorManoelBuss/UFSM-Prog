"""Faça um programa que leia o número inicial e o número final e escreva a soma de todos os números do 
intervalo lido"""

num1 = int(input("Insira um número para iniciar: "))
num2 = int(input("Insira o número que vai terminar: "))

numf = num2 + 1
soma = 0


for i in range (num1,numf):
    soma = soma + i
    print (i)
print(f"A soma dos números: {soma}")