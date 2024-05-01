"""
Faça um programa que leia um número não conhecido de valores até que seja informado o número 0. Ao final, 
escrever o maior e o menor número lido. 
"""

#while

maior = 0
menor = 0


while True:
    numero = float(input("Ao informar 0 o programa encerra. \n Informe um valor: "))

    if numero == 0:
        break

    maior = max(numero)
    menor = min(numero)


print(f"Maior: {maior}\n Menor: {menor}")

#list

lnumeros = []

while True:
    numero = int(input("Ao informar 0 o programa encerra. \n Informe um valor: "))

    if numero == 0:
        break

    lnumeros.append(numero)


print(f" Maior: {min(lnumeros)}\n Menor: {max(lnumeros)}")