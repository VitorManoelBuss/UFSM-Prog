"""Faça um programa que leia o número inicial e o número final e escreva todos os números do intervalo lido"""
num1 = int(input("Insira um número para iniciar: "))
num2 = int(input("Insira o número que vai terminar: "))

numf = num2 + 1

for i in range (num1,numf):
    print (i)