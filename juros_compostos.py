"""
Determina o saldo de um investimento, considerando juros continuamente 
compostos, dados o capital, a taxa de juros e duracao do investimento
"""

p = float(input("Valor investido: "))
t = float(input("Tempo de investimento: "))
r = float(input("Taxa de juros anual: "))

i = p*(2.718281**(r*t))

print(f"O seu investimento será de R${i} caso invista {p} durante {t} anos a uma taxa anual de {r}")

