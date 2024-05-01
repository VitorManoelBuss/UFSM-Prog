"""
Faça um programa que leia 10 números e ao final, os escreva na ordem em que foram digitados. 
Ordene em ordem crescente e os escreva. 
"""

lnumeros = []


for i in range(10):
    numeros = int(input("Informe um número: "))

    lnumeros.append(numeros)
    
print(f"Números na ordem que foram digitados: {lnumeros}")
    
lnumeros.sort()

print(f"Em ordem crescente: {lnumeros}")