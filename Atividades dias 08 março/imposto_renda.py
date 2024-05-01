"""Faça um programa que leia o valor do salário e calcule o valor do Imposto de Renda, de acordo com a tabela 
a seguir:"""

salario = float(input("Informe seu salário: R$"))

if (salario <= 2259.20):
    print(f"Você não paga imposto de renda")

elif (salario <= 2826.65):
    aliq = (salario - 2259.20) * 0.075

elif (salario <= 3751.05):
   aliq = (2826.65 - 2259.20) * 0.075 + (salario - 2826.65) * 0.15

elif (salario <= 4664.68):
    aliq = (2826.65 - 2259.20) * 0.075 + (3751.06 - 2826.65) * 0.15 + (salario - 3751.05)

else :
    aliq = (2826.65 - 2259.20) * 0.075 + (3751.06 - 2826.65) * 0.15 + (4664.68 - 3751.05) * 0.225 + (salario - 4664.68) * 0.275

print(f"Você pagará de imposto R${aliq:.2f}")