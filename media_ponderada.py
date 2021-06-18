"""
Calcula a media ponderada com base em quatro notas.
"""

p1 = float(input("Prova Um: "))
p2 = float(input("Prova Dois: "))
t1 = float(input("Trabalho Um: "))
t2 = float(input("Trabalho Dois: "))

nota_final = (p1*0.3 + p2*0.4 + t1*0.1 + t2*0.2)/(0.3 + 0.4 + 0.1 + 0.2)

print(f"Sua Media neste semestre é {nota_final}")