#Faça um programa em Python que leia o valor de uma venda e o percentual de comissão que o vendedor recebe 
#e calcule e escreva o valor da comissão

venda = float(input("Valor da venda: R$"))
percent = float(input("% da comissão: "))

comissao = venda * percent / 100


print(f"Sua comissão foi de: R${comissao:,.2f}")