""""Faça um programa que leia 10 números e escreva quantos são menores que 50, quantos são de 50 a 69, 
quantos são de 70 a 100 e quantos são maiores que 100"""


menor50 = 0
maior50 = 0
maior70 = 0
maior100 = 0


for i in range (1, 11):
    n = float(input("Informe um número: "))

    if (n < 50 ):
        menor50 = menor50 + 1

    elif (n >= 50 and n <= 69):
        maior50 = maior50 + 1

    elif (n >= 70 and n <= 100):
        maior70 = maior70 + 1

    else:
        maior100 = maior100 + 1 


print (f""" 
Menores que 50: {menor50}
Números de 50 a 69 são: {maior50}
Números de 70 a 100 são: {maior70}
Maiores que 100: {maior100}
""")
