"""Faça um programa que escreva os 10 primeiros termos da série:
1, 2, 4, 7, 11, 16 ..."""

t = 1 # termo começa com 1
r = 1 # razão começa com 1
for i in range(1, 11):
    print(t)  # escreve o termo
    t = t + r # gera o próximo termo (termo + razão)
    r = r + 1 # incrementa a razão a cada passada