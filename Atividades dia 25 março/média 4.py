#A média da disciplina será calculada com a seguinte fórmula:
#Nota 1º Bimestre: Prova 1 (6 pontos) + Atividades 1 (4 pontos)
#Nota 2º Bimestre: Prova 2 (6 pontos) + Atividades 2 (4 pontos)
#Média: (Nota1 + Nota2) / 2
#Faça um programa em Python que leia as notas das 2 provas e das 2 atividades e calcule e escreva a média final do aluno.


prova1 = float(input("Insira a nota da prova do primeiro bimestre "))
atividade1 = float(input("Insira a nota da atividade do primeiro bimestre "))

prova2 = float(input("Insira a nota da prova do segundo bimestre "))
atividade2 = float(input("Insira a nota da atividade do segundo bimestre "))

nota1 = prova1 + atividade1
nota2 = prova2 + atividade2

media = (nota1 + nota2)/2

print (f"Sua média foi {media:,.2f}")