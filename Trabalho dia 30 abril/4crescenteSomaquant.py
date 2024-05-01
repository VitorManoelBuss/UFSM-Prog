"""
Faça um programa que leia um número não conhecido de valores até que seja informado o número 0. 
Ao final, escrever os números em ordem decrescente, juntamente com a soma e a quantidade de números informados. 
"""

lnumeros = []

while True :
    numeros = int(input("Informe um número: "))
    if numeros == 0:
        break

    lnumeros.append(numeros)
    
lnumeros.sort(reverse = True)

print(f"Em ordem decrescente: {lnumeros}")
print(f"Soma dos termos: {sum(lnumeros)}")
print(f"Quantidade de termos: {len(lnumeros)}")