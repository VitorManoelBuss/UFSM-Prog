"""A comissão de um vendedor é proporcional ao seu volume de vendas. Faça um programa que leia o valor da venda 
e calcule e escreva a comissão do vendedor. A comissão será de:

3% sobre as vendas até R$ 10.000,00
5% sobre o que ultrapassar os R$ 10.000,00 de vendas"""

venda = float(input("Valor da venda: "))
if venda <= 10000:
    com = venda * 3 / 100
else:
    com = 10000 * 3 / 100 + (venda-10000) * 5 / 100
print("Comissão: ", com)