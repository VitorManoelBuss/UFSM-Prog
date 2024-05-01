valor_venda = float(input("Informe qual é o valor da venda em R$"))

codigo_cliente = int(input("""Digite qual o código de identificação de acordo com a tabela
(1) Cliente comum
(2) Funcionário
(3) Vip
Digite o código: 
"""))

valor_final = 0


if(codigo_cliente == 1):
    desconto = 0
    valor_final = valor_venda - (valor_venda * (desconto / 100))

elif(codigo_cliente == 2):
    desconto = 10
    valor_final = valor_venda - (valor_venda * (desconto / 100))

elif(codigo_cliente == 3):
    desconto = 5
    valor_final = valor_venda - (valor_venda * (desconto / 100))

print(f"O valor total foi de R${valor_final:,.2f}")