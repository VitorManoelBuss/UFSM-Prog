"""Faça um programa que leia o termo inicial, a razão de uma progressão aritmética, a quantidade de termos e 
escreva os termos da mesma"""


t = int(input("Informe o termo inicial: "))
r = int(input("Informe a razão: "))
n = int(input("Informe a quantidade de termos: "))

for i in range (n):
    print(t)
    t = t + r
