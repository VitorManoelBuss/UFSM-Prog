"""Faça um programa que fique lendo o valor de uma dívida, a taxa de juros mensal e a quantidade de meses e 
escreva o valor da dívida ao final do período. O programa deve encerrar quando for informado o valor da dívida 
igual a 0."""

while True:
    divida = float(input("Informe o valor da dívida: "))

    if divida == 0:
        print("Programa encerrado")
        break

    juros = float(input("Informe a porcentagem de juros (Não use %, apenas números): ")) / 100

    meses = int(input("Informe quantos meses faltam para o encerramento do pagamento: "))

    for i in range(meses):
        divida = divida * (1 + juros)

    print(f"O valor da dívida em {meses} será de R${divida:,.2f}")


    
    #exemplo de questão com juros compostos# 
