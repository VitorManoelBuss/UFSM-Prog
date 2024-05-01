"""Faça um programa que escreva os 10 primeiros termos da série de Fibonacci. Essa série é uma sequência de 
números inteiros, começando por 0 e 1, na qual cada termo subsequente corresponde à soma dos dois anteriores. 
0, 1, 1, 2, 3 ..."""

pen = 0
ult = 1
print(pen)
print(ult)
for i in range(8):
    t = ult + pen
    print(t)
    pen = ult
    ult = t