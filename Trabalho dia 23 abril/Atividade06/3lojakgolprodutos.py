"""A loja K. Gol vende os seguintes produtos:
1 - boné a R$ 10,00
2 - camiseta a R$ 20,00
3 - bermuda a R$ 25,00
4 - calção de banho a R$ 15,00
5 - maiô a R$ 40,00
6 - biquini a R$ 30,00
Faça um programa que fique lendo o código do produto e a quantidade até que seja digitado 0 para encerrar 
a compra. Quando encerrar a compra escrever o total a pagar e exibir novamente o menu para ficar pronto para 
realizar outra venda."""

while True:
    valor_final = 0
    reiniciar = False

    while not reiniciar:
        bone = 10
        camiseta = 20
        bermuda = 25
        calcao_banho = 15
        maio = 40
        biquini = 30

        print("\n---------------")
        print("1 - Boné R$10")
        print("2 - Camiseta R$20")
        print("3 - Bermuda R$25")
        print("4 - Calção de banho R$15")
        print("5 - Maiô R$40")
        print("6 - Biquíni R$30")
        print("0 - Sair e mostrar o total a pagar")
        print("---------------\n")
        op = int(input("Escolha a opção: "))
        
        if (op == 1):
            valor_final = valor_final + bone

        elif (op == 2):
            valor_final = valor_final + camiseta

        elif (op == 3):
            valor_final = valor_final + bermuda

        elif (op == 4):
            valor_final = valor_final + calcao_banho
        
        elif (op == 5):
            valor_final = valor_final + maio

        elif (op == 6):
            valor_final = valor_final + biquini
        
        elif (op == 0):
            reiniciar = True
        
        else:
            print("---------------")
            print("\nOpção inválida!")

    if not reiniciar:
        break

    print(f"O valor final da sua compra é de R${valor_final}")

print("Programa encerrado")

