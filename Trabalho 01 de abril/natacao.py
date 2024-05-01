idade = int(input("Digite sua idade "))

if (idade >= 7 and idade <= 11 ):
    print ("Sua categoria é a infantil")

elif (idade >= 12 and idade <= 17 ):
    print ("Sua categoria é a juvenil")

elif (idade >= 18 and idade <= 25 ):
    print ("Sua categoria é a adulto")

else : print("Idade fora das faixas etárias contempladas")