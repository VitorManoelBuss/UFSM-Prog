valor_venda = float(input("Valor da venda: R$"))
codigo = int(input(f"""
(1) Cliente comum
(2) Funcionário
(3) Vip

Digite um número de acordo com a lista               
"""))


if (codigo == 2):
    porc = 0.10 * valor_venda
    total = valor_venda - porc
    print(f"Valor a pagar R${total:,.2f}")

elif (codigo == 3):
   porc = 0.05 * valor_venda
   total = valor_venda - porc
   print(f"Valor a pagar R${total:,.2f}") 

elif (codigo == 1):
    print(f"Valor a pagar R${valor_venda:,.2f}")