#Faça um programa em Python que leia a quantidade de horas trabalhadas e o valor pago por hora e calcule e 
#escreva o salário do trabalhador

horastrab = float(input("Quantias de horas trabalhadas: "))
vlrpg = float(input("Valor pago pelas horas: R$"))

salario = horastrab * vlrpg

print(f"Seu salário é de: R${salario:,.2f}")