"""Faça um programa que escreva os 10 primeiros termos da série:
1, 4, 9, 12, 17, 20, 25 ..."""

t = 1
r = 3
for i in range(1, 11):
    print(t)
    t = t + r
    if i%2==0:
        r = 3
    else:
        r = 5