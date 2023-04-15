# ESSE PROGRAMA CALCULAR A ÁREA DE UM CIRCUFERENCIA QUE PI * RAIO ELEVADO AO QUADRADO
from math import pi

print ('\033[31m----- CALCULANDO A CIRCUFERENCIA -----\033[m')
raio = float(input('Imforme o raio: '))
circuferencia = pi * raio ** 2
print(F'A circuferencia equivale a {circuferencia}')