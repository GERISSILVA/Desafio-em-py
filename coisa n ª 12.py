'''Construa um programa que solicite que o usuário informe 2
números inteiros positivos. O programa deve calcular:
a) O cubo do segundo número
b) A média geométrica entre o primeiro e o segundo número, isto é, '''

from math import sqrt

n1 = int(input('Informe um número: '))
n2 = int(input('Informe outro número: '))

cubo = n2 ** 3
media = n1 + n2 
media1 = sqrt(media)

print(f'O cubo de {n2} e {cubo} e a média entre o primeiro e segundo número e {media1:.1f}')