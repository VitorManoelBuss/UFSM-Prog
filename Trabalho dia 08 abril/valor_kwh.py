"""Faça um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. 
Leia a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para 
comércios.
Calcule o preço a pagar de acordo com a tabela a seguir:

- Residencial Até 100kWh: R$ 0,50 por kWh
- Residencial acima de 100kWh: R$ 0,75 por kWh
- Comercial: R$ 0,65 por kWh 
- Industrial: R$ 0,55 por kWh"""

kWh = float(input("Informe os kWh gastos: "))
inst = (input(
"""De acordo com a tabela informe seu tipo de instalação
(R) Residencial
(I) Industrial
(C) Comercial
"""
))



if (inst == "r") or (inst =="R"):
    if (kWh <= 100):
        vkWh = kWh * 0.5
    elif (kWh > 100):
        vkWh = 100 * 0.5 + (kWh - 100) * 0.75
elif (inst == "c") or (inst == "C"):
    vkWh = kWh * 0.65
elif (inst == "i") or (inst == "I"):
    vkWh = kWh * 0.55


print(f"Você deve pagar R${vkWh:.2f}")