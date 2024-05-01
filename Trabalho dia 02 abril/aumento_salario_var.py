salario = float(input("Digite o valor do seu salário: R$"))

if (salario <= 3000):
    aumento = 0.12 * salario
    print(f"Aumento de R${aumento:,.2f} no seu salário")

elif(salario > 3000):
    aumento = 0.09 * salario
    print(f"Aumento de R${aumento:,.2f} no seu salário")