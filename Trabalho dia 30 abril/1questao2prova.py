"""
Faça um programa que leia um número não conhecido de valores até que seja informado o número 0. Ao final, 
escrever a soma e a quantidade de números informados.
"""

#While

"""soma = 0 
quantidade = 0

while True:
    numero = int(input("Ao informar 0 o programa encerra. \n Informe um valor: "))

    soma = soma + numero
    quantidade = quantidade + 1

    if numero == 0:
        break

print(f"Soma: {soma}\n Quantidade de números:{quantidade}")"""

#Lista

lnumeros = []

while True:
    numero = int(input("Ao informar 0 o programa encerra. \n Informe um valor: "))

    if numero == 0:
        break

    lnumeros.append(numero)


print(f" Soma: {sum(lnumeros)}\n Quantidade de números:{len(lnumeros)}")