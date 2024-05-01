"""O inverno é uma estação maravilhosa, não é mesmo? Todos nós amamos vestir um poncho, participar de uma roda
 de chimarrão, assar pinhões no fogão a lenha… Mas nem todos gostam do inverno, especialmente em lugares onde 
 o inverno costuma ser muito cruel. Em Fred Westeros, por exemplo, o humor das pessoas é definido de acordo 
 com as tendências climáticas.

Com base nas temperaturas dos três últimos dias, as pessoas podem ficar tristes ou felizes.

Se a temperatura subiu do 1º para o 2º dia, mas desceu ou permaneceu constante do 2º para o 3º, 
as pessoas ficam tristes.
Se a temperatura subiu do 1º para o 2º dia e do 2º para o 3º, as pessoas ficam felizes.
Se a temperatura desceu do 1º para o 2º dia, mas subiu ou permaneceu constante do 2º para o 3º, 
as pessoas ficam felizes.
Se a temperatura desceu do 1º para o 2º dia e do 2º para o 3º, as pessoas ficam tristes.
Se a temperatura permaneceu constante (igual) do 1º para o 2º dia, as pessoas ficam felizes, se subiu do 2º 
para o 3º dia ou tristes caso contrário.
Faça um programa que leia a temperatura dos dias 1, 2 e 3 e escreva se as pessoas estarão felizes ou tristes."""

d1 = float(input("Temperatura do dia 1: "))
d2 = float(input("Temperatura do dia 2: "))
d3 = float(input("Temperatura do dia 3: "))

if (d1 < d2 and d2 >= d3):
    print("Tristes")

elif (d1 < d2 and d2 < d3):
    print("Felizes")

elif (d1 > d2 and d2 <= d3):
    print("Felizes")

elif (d1 > d2 and d2 > d3):
    print("Tristes")

elif (d1 == d2 and d2 < d3 ):
    print("Felizes")

else:
    print("Tristes")


    