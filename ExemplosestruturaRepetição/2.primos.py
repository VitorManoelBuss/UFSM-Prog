"""Faça um programa que leia um número e escreva se o mesmo é primo ou não. Um número é primo quando tem 
somente 2 divisores"""

cont = 0
n = int(input("Informe um número: "))

for i in range(1, n+1):
    if n % i == 0:
        cont = cont + 1

if cont==2:
    print(n, " é primo")
else:
    print(n, " não é primo")