"""
Faça um programa que leia 10 números e os armazene em uma lista. A seguir, crie outra lista com os 
respectivos valores da primeira lista multiplicados por 5. Exiba as duas listas, lado a lado, com 1 valor de 
cada lista em cada linha. 
"""
l1 = []
l2 = []

for i in range(10):
    numero = int(input("Informe um número: "))

    l1.append(numero)
    l2.append(numero * 5)

for i in range(10):
    print(f"{l1[i]} x 5 = {l2[i]}")


#evandro.preuss@ufsm.br