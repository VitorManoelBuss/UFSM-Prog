#A Flávia Jando em sua última viajem trouxe um termômetro dos EUA, mas esqueceu que lá a temperatura é 
#expressa em graus Fahrenheit. 
#Faça um algoritmo/programa em Python que leia a temperatura em graus Fahrenheit e calcule e escreva 
#atemperatura em graus Celsius, de acordo com a fórmula:
#GrausCelsius = (GrausFahrenheit - 32) / 1.8

grausFahrenheit = float(input("Informe a temperatura em graus Fahrenheit: "))
grausCelsius = (grausFahrenheit -32)/1.8
print ("A temperatura em graus Celsius é:",grausCelsius)