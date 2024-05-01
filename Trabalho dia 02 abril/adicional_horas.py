quant_h = int(input("Digite o número de horas trabalhadas no mês: "))
valor_h = float(input("Digite o valor da hora trabalhada R$"))

if(quant_h <= 200):
    salario = quant_h * valor_h
    print(f"Você não tem direito a hora extra seu salário se mantém o mesmo R${salario:,.2f}")

elif(quant_h > 200):
    hora_extra = (quant_h - 200) * valor_h * 50/100
    salario_final = hora_extra + quant_h * valor_h
    print(f"Seu salário passa a ser de R${salario_final:,.2f} com aumento de R${hora_extra:,.2f}")