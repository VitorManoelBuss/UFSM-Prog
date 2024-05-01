espetinho = 7.00
refri = 5.00

vendaE = int(input("Quantos espetinhos você vendeu? "))
vendaR = int(input("Quantos refris você vendeu? "))
valorTotal = (vendaE * espetinho) + (vendaR * refri)

print (f"o valor da venda é de R${valorTotal:,.2f}")


dinheiro = float(input("Quantos reais o cliente deu? "))
troco = dinheiro - valorTotal
if(dinheiro >= valorTotal):
    if(dinheiro != 0):
        print(f"Você deve dar de troco R${troco:,.2f}")

print (f"Você vendeu {vendaE} espetinho e {vendaR} refri")