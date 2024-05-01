"""Faça um programa que leia um número e escreva a quantidade de divisores"""

#zera o contador
cont =0

#ler um número
n = int(input("Informe um número: "))

#gerar os números de 1 até o nro lido
for i in range(1, n+1):
    #testar se n divido por i sobra 0 => é divisor
    if n % i == 0:
        #contar os divisores
        cont = cont + 1

#escreve a quantidade de divisores
print("Quant de divisores: ", cont)