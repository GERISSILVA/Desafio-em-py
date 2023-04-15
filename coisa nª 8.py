#Plano cartesiano
from math import sqrt

x1 = int(input('Informe o x1 do P1: '))
y1 = int(input('Informe o y1 do P1: '))
x2 = int(input('Informe o x2 do P2: '))
y2 = int(input('Inforem o y2 do P2: '))

distancia = ((x1 - x2) ** 2 ) + ( (y1 - y2) ** 2 )

valor = sqrt (distancia)

print(f'A distância entre P1 e P2 e = {valor:.2f}')