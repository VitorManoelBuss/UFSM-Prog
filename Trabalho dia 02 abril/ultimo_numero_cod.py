codigo = int(input("Digite o código do produto: "))

ult_dgt = codigo % 10

if (ult_dgt == 1):
    print("Alimento não perecível")

elif (ult_dgt >= 2 and ult_dgt <=4 ):
    print("Alimento perecível")

elif (ult_dgt >= 5 and ult_dgt <= 6 ):
    print("Vestuário")

elif (ult_dgt >= 7 and ult_dgt <= 9 ):
    print("Limpeza")

if (ult_dgt == 0):
    print("Eletroeletrônico")

    