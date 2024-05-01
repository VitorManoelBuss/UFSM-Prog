"""Faça um programa que leia o número inicial e o número final e o número múltiplo e escreva todos os números 
do intervalo, que são múltiplos do número lido"""


num1 = int(input("Insira o primeiro valor: "))
num2 = int(input("Qual o último valor: "))
mult = int(input("Qual o múltiplo: "))

for i in range (num1, num2 + 1):
    if i % mult == 0:
        print(i)