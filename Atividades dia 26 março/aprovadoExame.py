#Faça um programa em Python que leia 2 valores e escreva a média dos mesmos e escreva se o aluno está aprovado
#ou em exame. Para estar aprovado a média precisa ser maior ou igual a 7

nota1 = int(input("Primeira nota: "))
nota2 = int(input("Segunda nota: "))

media = (nota1 + nota2) / 2

if (media >= 7):
    print(f"Sua média é {media:,.2f}. Você passou")

elif (media <= 6.99):
    print(f"Sua média é {media:,.2f}. Ficou de exame")   