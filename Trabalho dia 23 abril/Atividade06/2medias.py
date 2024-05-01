"""A média da disciplina será calculada com a seguinte fórmula:
Nota 1º Bimestre: Prova 1 (6 pontos) + Atividades 1 (4 pontos)
     Nota 2º Bimestre: Prova 2 (6 pontos) + Atividades 2 (4 pontos)
     Média: (Nota1 + Nota2) / 2
Faça um programa que leia as notas das provas e das atividades e calcule e escreva a média final do aluno, 
aceitando somente valores válidos para as provas (0 a 6) e para as atividades (0 a 4). Caso a nota não esteja
no intervalo, exibir uma mensagem e ler novamente a nota."""

#Prova1
while True:
    prova1 = input("Digite a nota da prova do primeiro bimestre (de 0.0 a 6.0): ")
    try:
        prova1 = float(prova1)
        if prova1 >= 0 and prova1 <= 6:
            break
        else:
            print("Por favor, digite uma nota válida (entre 0.0 e 6.0).")
    except ValueError:
        print("Por favor, digite um número válido.")


#Trabalho 1
while True:
    trab1 = input("Digite a nota do trabalho do primeiro bimestre (de 0.0 a 4.0): ")
    try:
        trab1 = float(trab1)
        if trab1 >= 0 and trab1 <= 4:
            break
        else:
            print("Por favor, digite uma nota válida (entre 0.0 e 4.0).")
    except ValueError:
        print("Por favor, digite um número válido.")


#Prova2
while True:
    prova2 = input("Digite a nota da prova do segundo bimestre (de 0.0 a 6.0): ")
    try:
        prova2 = float(prova2)
        if prova2 >= 0 and prova2 <= 6:
            break
        else:
            print("Por favor, digite uma nota válida (entre 0.0 e 6.0).")
    except ValueError:
        print("Por favor, digite um número válido.")

#Trabalho 2
while True:
    trab2 = input("Digite a nota do trabalho (de 0.0 a 4.0): ")
    try:
        trab2 = float(trab2)
        if trab2 >= 0 and trab2 <= 4:
            break
        else:
            print("Por favor, digite uma nota válida (entre 0.0 e 4.0).")
    except ValueError:
        print("Por favor, digite um número válido.")

nota1 = prova1 + trab1
nota2 = prova2 + trab2
media = (nota1 + nota2) / 2

print(f"Sua média é {media:,.2f}")