salario = float(input("Digite o valor do seu salário atual: R$"))
porcentagem = int(input("Digite o percentual de reajuste "))

reajuste = porcentagem / 100
salario_novo = salario * reajuste + (salario) 
valor_reajuste = salario * reajuste



input(
    f"""
Valor do reajuste: R${valor_reajuste:,.2f}
Novo salário: R${salario_novo:,.2f}

""")