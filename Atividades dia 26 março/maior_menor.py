"""Faça um algoritmo que leia 3 números e escreva qual é o maior e qual é o menor deles"""

a = float(input("Informe o 1º número: "))
b = float(input("Informe o 2º número: "))
c = float(input("Informe o 3º número: "))
#encontra o maior
if a >= b and a >= c:
    print("Maior: ",a)
elif b >= a and b >= c:
    print("Maior: ",b)
else:
    print("Maior: ",c)
#encontra o menor
if a <= b and a <= c:
    print("Menor: ",a)
elif b <= a and b <= c:
    print("Menor: ",b)
else:
    print("Menor: ",c)



#Ou usando max e min:



a = float(input("Informe o 1º número: "))
b = float(input("Informe o 2º número: "))
c = float(input("Informe o 3º número: "))
maior = max(a, b, c)
menor = min(a, b, c)
if maior == menor:
    print("Iguais: ", maior)
else:
    print("Maior: ", maior)
    print("Menor: ", menor)