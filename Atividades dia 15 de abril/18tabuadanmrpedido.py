"""Faça um programa que leia um número e escreva a sua tabuada."""

n = int(input("Tabuada de qual número você quer saber: "))

print(f"Tabuada do {n}\n")

for i in range (1,11):
    tabu = n * i
    print(f" {n} X {i} = {tabu}")