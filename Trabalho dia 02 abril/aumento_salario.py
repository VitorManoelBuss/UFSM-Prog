salario = float(input("Digite o valor do seu salário atual: R$"))

salario_novo = salario + (salario * 0.12)
reajuste = salario_novo - salario

print(
    f"""
    Salário atual: R${salario:,.2f} 
    Valor do reajuste: R${reajuste:,.2f}
    Salário com reajuste R${salario_novo:,.2f}
""")