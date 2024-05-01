pastel_carne = 5.00
pastel_frango = 4.00

q_carne = int(input("Pasteis de carne: "))
q_frango = int(input("Pasteis de frango: "))

conta_c = pastel_carne * q_carne
conta_f = pastel_frango * q_frango

v_total = conta_c + conta_f

print(f"O valor total da venda foi de R${v_total:,.2f}")