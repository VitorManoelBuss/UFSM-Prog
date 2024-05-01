#Osmar Vado vende bugigangas para os turistas. Ele aceita pagamento em Real, Euro e em Dólar e para facilitar a cobrança ele usa os seguintes valores de cotação: 1 Euro = 6 Reais; 1 Dólar = 5 Reais. Faça um algoritmo/programa em Python que leia o valor da venda e escreva os valores correspondentes em Euro e em Dólar.

real = float(input("Qual o valor da compra em real? R$: "))
euro = real / 6
dolar = real / 5

print (f"Real R${real:,.2f}") 
print (f"Euro €{euro:,.2f}")
print (f"Dólar ${dolar:,.2f}")