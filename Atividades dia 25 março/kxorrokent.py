"""A KXorro QuemT vende hotdog a R$ 10,00 e refri a R$ 5,00. 
Faça um programa que leia a quantidade de hotdog e de refri vendidos e calcule e escreva o 
valor total da venda"""

hotdog = 10
refri = 5

venda_hot = int(input("Vendeu quantos hotdogs: "))
venda_ref = int(input("Vendeu quantos refris: "))

total = (hotdog * venda_hot) + (refri * venda_ref)

print(f"O valor total da venda foi de R${total}")