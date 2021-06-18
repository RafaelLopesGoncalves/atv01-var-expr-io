"""
Determina o dia da semana com base no dia, mes e ano.
"""

d = int(input("Dia: "))
m = int(input("Mes: "))
a = int(input("Ano: "))

y = a - ((14 - m)/12)
x = y + y/4 - y/100 + y/400
M = m + 12*((14 - m)/12) - 2
D = (d + x +(31*M)/12)%7

print (f"O dia da semana em {d}.{m}.{a} é {D}")



