#O tempo pode ser expresso em horas, minutos e segundos ou em segundos.
#Faça um programa que leia a quantidade de tempo: horas, minutos e segundos e escreva a quantidade total em segundos.

hora = float(input("Digite a hora "))
minutos = float(input("Digite os minutos "))
segundos = float(input("Digite os segundos "))

tempoES = segundos + (minutos * 60) + (hora * 3600)

print (f"O horário digitado são {tempoES} segundos")