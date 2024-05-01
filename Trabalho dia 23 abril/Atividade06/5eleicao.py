"""Fazer um programa que controla uma eleição com três candidatos. O programa deve realizar as seguintes 
tarefas:
- Calcular o total de votos para cada candidato;
- Calcular a quantidade de votos nulos;
- Calcular a quantidade de votos em branco;
A votação deve obedecer as seguintes convenções:
1,2,3 => votos dos candidatos
0 => votos em branco
9 => encerramento da apuração
Qualquer outro número => voto nulo
Ao final escrever qual o candidato vencedor ou se a eleição foi anulada. Uma eleição é anulada caso a soma 
de votos nulos e brancos seja maior que a soma dos votos de todos os candidatos."""



bonoro = 0
lule = 0
daciolo = 0
branco = 0
nulo = 0
nb = 0
totalv = 0

while True:
    


    print("\n---------------")
    print("1 - Bonoro (talkei) ")
    print("2 - Lule (faz oéli)")
    print("3 - Daciolo (glória a deux)")
    print("9 - Encerramento da apuração")
    print("0 - Voto em branco")
    print("---------------\n")
    op = int(input("Escolha a opção: "))

    if (op == 1):
        bonoro = bonoro + 1
        totalv = totalv + 1
        print(f"Você votou no Bonoro, voto cocluído")

    elif (op == 2):
        lule = lule + 1
        totalv = totalv + 1
        print(f"Você votou no Lule, voto cocluído")

    elif (op == 3):
        daciolo = daciolo + 1
        totalv = totalv + 1
        print(f"Você votou no Daciolo, voto cocluído")

    elif (op == 0):
        branco = branco + 1
        nb = nb + 1
        print("Você votou em branco, voto concluído")

    else:
        nulo = nulo + 1
        nb = nb + 1
        print("Você votou nulo, voto concluído")

    if (op == 9):
        print(f"Apuração encerrada")
        break
    

print("\n---------------")
print(f"Bonoro ({bonoro} votos) ")
print(f"Lule ({lule} votos)")
print(f"Daciolo ({daciolo} votos)")
print(f"Nulos ({nulo} votos)")
print(f"Brancos ({branco} votos)")
print("---------------\n")



if (nb > totalv):
    print("Votação anulada, votos em branco e nulos somados são maiores que a soma dos votos dos candidatos")

elif (bonoro > lule and bonoro > daciolo):
    print(f"Bonoro ganhou a eleição com {bonoro} votos")

elif (lule > bonoro and lule > daciolo):
    print(f"Lule ganhou a eleição com {lule} votos") 

elif (daciolo > lule and daciolo > bonoro):
    print(f"Daciolo ganhou a eleição com {daciolo} votos")

elif (daciolo == lule):
    print(f"Daciolo fez {daciolo} votos empatando com Lule que fez {lule} votos também")

elif (daciolo == bonoro):
    print(f"Daciolo fez {daciolo} votos empatando com Bonoro que fez {bonoro} votos também")

elif (lule == bonoro):
    print(f"Lule fez {lule} votos empatando com Bonoro que fez {bonoro} votos também")
