"""
O pais A tem 1200000 habitantes e a taxa de crescimento da população é de 3% ao ano. O pais B tem 1500000 
habitantes e a taxa de crescimento da população é de 2% ao ano. Faça um programa que calcule quantos anos são 
necessários para que o país A tenha mais população que o país B.
"""

a = 1200000
b = 1500000
cont = 0
while a < b:
    a = a * 1.03
    b = b * 1.02
    cont = cont + 1

print("Depois de ", cont, "anos")
print("a tem ", int(a), " e b tem ",int(b))