#Osmar Telo costuma oferecer descontos para seus clientes e precisa de um programa que leia o valor da venda e
#o percentual de desconto concedido e escreva o valor do desconto e o valor final da venda.

venda = float(input("Valor da venda R$"))
desconto = float(input("Porcentagem de desconto "))

porcentagem = desconto / 100
valorDesconto = venda * porcentagem
valorFinal = venda - valorDesconto

print(f"O valor final é de R${valorFinal:,.2f}")
print(f"O desconto é de R${valorDesconto:,.2f}")

#ou

vv = float(input("Informe o valor da venda: "))
pdesc = float(input("Informe o % de desconto: "))
valdesc = vv * pdesc / 100
vcomdesc = vv - valdesc
print("Desconto:", valdesc)
print("Venda com desconto:", vcomdesc)