"""Faça um programa que leia o valor de uma venda e o código da forma de pagamento, de acordo com a tabela
a seguir: Código - Classificação
• 1 - À vista, com 5% de desconto
• 2 - Em 2x, preço normal sem juros
• 3 - Em 5x, preço acrescido de 5%
Com base neste código, o programa deverá calcular e escrever o valor a pagar, a forma de pagamento e o valor 
de cada parcela, se for o caso."""

venda = float(input("Valor da venda: "))
op = int(input("Opção de pgto [1-a vista, 2-2x s/juro, 3-5x c/juro]:"))
if op == 1:
    desc = venda * 5 / 100
    print("Desconto: ",desc)
    total = venda - desc
    print("Total: ", total)
elif op == 2:
    parc = venda / 2
    print("2 parcelas de: ", parc)
elif op == 3:
    acr = venda * 5 / 100
    print("Acréscimo: ",acr)
    total = venda + acr
    print("Total: ", total)
    parc = total / 5
    print("5 parcelas de: ", parc)
else:
    print("Opção Inválida!")