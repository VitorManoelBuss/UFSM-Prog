"""Faça um programa em Python que deverá ler o preço em reais de um produto e as cotações do dólar e do euro 
e calcule e escreva os valores em real, dólar e euro."""

valor = float(input("Valor em reais R$"))
cot_dolar = float(input("Cotação do dólar $"))
cot_euro = float(input("Cotação do euro €"))

dolar = valor * cot_dolar
euro = valor * cot_euro

print(f"""
Valor em reais R${valor:,.2f}
Valor em dólar ${dolar:,.2f}
Valor em euro €{euro:,.2f}
""")