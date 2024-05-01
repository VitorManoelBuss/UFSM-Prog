import math

a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))

delta = b ** 2 - 4 * a * c

if (delta > 0):
    
    x1 = (- b + math.sqrt(delta)) / 2 * a
    x2 = (- b - math.sqrt(delta)) / 2 * a
    print(f"A primeira raiz é {x1}")
    print(f"A segunda raiz é {x2}")
else:
    print("Não há raiz para delta negativo")
