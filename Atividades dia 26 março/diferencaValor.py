#Faça um programa que leia 2 números e escreva a diferença do maior pelo menor

n1 = float(input("Informe o 1º número: "))
n2 = float(input("Informe o 2º número: "))
if n1 >= n2:
    dif = n1 - n2
else:
    dif = n2 - n1
print("A diferença é: ", dif)