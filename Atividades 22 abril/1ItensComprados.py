"""
Faça um programa que leia um número não conhecido de valores correspondendo à quantidade de produtos e valor 
unitário do mesmo, contando a quantidade e somando o valor parcial da compra, até que seja informado a 
quantidade 0 (zero). Ao final, escreva a quantidade de itens comprados e o valor total da compra.
"""

cont = 0
total = 0
while True:
    quant = float(input("Informe a quantidade: "))
    if quant == 0:
        break
    valorunit = float(input("Informe o valor unitário: "))
    cont = cont + 1
    valorparc = quant * valorunit
    print(valorparc)
    total = total + valorparc
print("Quantidade de itens: ", cont)
print("Total da compra: ",total)