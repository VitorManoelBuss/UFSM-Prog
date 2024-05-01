"""Faça um programa que leia o valor do salário de um funcionário e a quantidade de filhos com direito 
ao salário família. Sobre o salário, há um desconto de INSS de 9% e um acréscimo de R$ 62,04 para cada filho 
(salário família). Escreva o salário bruto, o desconto de INSS e o adicional de salário família."""

salario = float(input("Seu salário R$"))
filho = int(input("Digite a quantia de filhos que tens "))

inss = salario  * 0.09
acrescimo = filho * 62.04

print(f"""
Salário bruto R${salario:,.2f}
Desconto do INSS R${inss:,.2f}
Adicional de salário família R${acrescimo:,.2f}
""")