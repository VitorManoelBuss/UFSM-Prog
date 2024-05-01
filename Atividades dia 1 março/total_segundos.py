"""Faça um programa que leia a quantidade total em segundos e calcule e escreva a quantidade correspondente em horas, minutos e segundos. Exemplo: 5000 segundos = 1 hora, 23 minutos e 20 segundos
"""

tseg = int(input("Total em segundos: "))
hora  = tseg // 3600
resto = tseg % 3600
minuto = resto // 60
seg = resto % 60
print("Horas: ",hora, ", Minutos: ", minuto, ", Segundos: ", seg)