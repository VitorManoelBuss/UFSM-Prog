valor_compra = float(input("Digite o valor da compra: "))
codigo = int(input("""
(1)  À vista, com 8% de desconto
(2)  À vista no cartão, 4% de desconto
(3) Em 3x, preço normal sem juros
(4) Em 8x, preço acrescido de 10%
            
Digite o número que se adequa a venda: 
"""))

if (codigo == 1):
    total = valor_compra - (valor_compra * 0.08)
    desconto = valor_compra - total
    print(f"""
Pagamento à vista no dinheiro ou pix       
Valor a pagar R${total:,.2f}
Valor do desconto R${desconto:,.2f}
""")
    
elif (codigo == 2):
    total = valor_compra - (valor_compra * 0.04)
    desconto = valor_compra - total
    print(f"""
Pagamento à vista no cartão
Valor a pagar R${total:,.2f}
Valor do desconto R${desconto:,.2f}
""")
    
elif (codigo == 3):
    parcela = valor_compra / 3
    print(f"""
Pagamento em 3x sem juros
Valor da parcela R${parcela:,.2f}
Valor total R${valor_compra:,.2f}
""")

elif (codigo == 4):
    juros = valor_compra + (valor_compra * 0.10)
    parcela = juros / 8
    print(f""" 
Pagamento em 8x com juros de 10%
Valor da parcela R${parcela:,.2f}
Valor total R${juros:,.2f}
""")
