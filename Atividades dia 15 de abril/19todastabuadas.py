"""Faça um programa que escreva as tabuadas do 1 até o 10"""



for j in range(1,11):
    print(f"\nTabuada do {j}")
    for i in range (1,11):
        tabu = j * i
        print(f" {j} X {i} = {tabu}")