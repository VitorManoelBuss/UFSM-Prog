""" A empresa C.K.H. Sanitários paga uma comissão para seus vendedores de acordo com a seguinte tabela:
- Até 10.000,00 de vendas: 10% de comissão
- de 10.000,01 a 25.000,00: 7,5% de comissão
- acima de 25.000,00: 5% de comissão
Faça um programa que leia o total de vendas realizadas por um colaborador e escreva o total de comissão que 
ele receberá."""

venda_total = float(input("Qual o valor total de vendas: "))

if (venda_total <= 10000) :
    acrescimo = venda_total * 0.10

elif (venda_total <= 25000 ) :
    acrescimo = 10000.00 * 0.10 + (venda_total - 10000.00) * 0.075

elif (venda_total > 25000 ) :
    acrescimo = 10000 * 0.10 + 15000 * 0.075 + (venda_total - 25000) * 0.05
    
print (f"Comissão de R${acrescimo:.2f}")
