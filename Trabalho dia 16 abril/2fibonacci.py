"""A Sequência de Fibonacci é uma sucessão de números. Esta sucessão obedece um padrão onde cada elemento 
subsequente é o resultado da soma dos dois elementos anteriores, sendo que o primeiro elemento é 0 e o 
segundo é 1. Faça um programa que escreva os 10 primeiros termos da série de Fibonacci (0, 1, 1, 2, 3, 5...)"""


pen = 0
ult = 1
print(pen)
print(ult)
for i in range(8):
    t = ult + pen
    pen = ult
    ult = t
    print(t)