"""Faça um programa que leia o termo inicial, a razão de uma progressão aritmética e escreva os 10 primeiros 
termos da mesma"""

t = int(input("Informe o termo inicial: "))
r = int(input("Informe a razão: "))

for i in range (1,11):
    print(t)
    t = t + r

