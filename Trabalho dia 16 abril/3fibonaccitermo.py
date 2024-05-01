"""Faça um programa que leia a quantidade de termos e escreve a série de Fibonacci com a quantidade de termos 
lido."""

termo = int(input("Informe quantos termos da série Fibonacci você quer saber: "))

pen = 0
ult = 1

if (termo <= 2):
    print("A série de Fibonacci precisa de pelo menos dois termos para começar, reinicie o programa!")

else:
     print("\n1º termo:")
     print(pen)
     print("\n2º termo:")
     print(ult)
for i in range(termo - 2):
        t = ult + pen
        pen = ult
        ult = t
        print(f"\n{i + 3}º termo:")
        print(t)