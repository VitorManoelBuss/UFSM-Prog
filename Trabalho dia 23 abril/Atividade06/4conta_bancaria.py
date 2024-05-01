"""
Faça um programa que controla o saldo de uma conta, com um menu com as opções:
1 - Depositar: ler o valor do depósito
2 - Sacar: ler o valor do saque. Somente pode sacar se tiver saldo suficiente
3 - Mostrar saldo
4 - Sair
"""

saldo = 0
while True:
    print("\n---------------")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Consultar saldo")
    print("4 - Sair")
    print("---------------\n")
    op = int(input("Escolha a opção: "))

    if (op == 1):
        deposito = float(input("Qual o valor que deseja depositar R$"))
        saldo = saldo + deposito
        print(f"Valor de R${deposito:,.2f} depositado com sucesso!")

    elif (op == 2):
       if(saldo > 0):
            saque = float(input("Informe o valor que deseja sacar R$"))
            if (saldo >= saque):
                saldo = saldo - saque
                print("Saque efetuado")
            else:
                print("Saldo insuficiente")

    elif (op == 3):
        print(f"Seu saldo é de R${saldo:,.2f}")

    elif (op == 4):
        break
    
    else:
        print("Opção inválida!")
