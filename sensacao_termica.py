"""
Determina a senação térmica com base na temperatura (C) e na velocidade
do vento (km/h)
"""

t = float(input("Temperatura do Ambiente: "))
v = float(input("Velocidade do Vento: "))

w = 13.12 + 0.6215*t - 11.37*(v**0.16) + 0.3965*t*(v**0.16)

print(f"O indice de Resfriamento do local é {w} quando a Temperatura é {t} e a velocidade do vento é {v}")
