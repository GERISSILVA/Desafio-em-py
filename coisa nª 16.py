'''a) todos os lados sejam maiores que zero e;
b) um dos lados seja menor que a soma dos outros dois e maior
que o valor absoluto da diferença entre os lados. Veja as restrições:'''
from math import sqrt

x1 = float(input('Qual o x1? '))
y1 = float(input('Qual o y1? '))

x2 = float(input('Qual o x2? '))
y2 = float(input('Qual o y2? '))

x3 = float(input('Qual o x3?'))
y3 = float(input('Qual o y3?'))

distancia = (x1 - x2) ** 2 + (y2 - y1) ** 2
lado1 = sqrt(distancia)

lado2 = sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)

lado3 = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)

cond1 = True
cond2 = True
cond3 = True

if lado1 == 0 or lado2 == 0 or lado3 ==0 :
    cond1 = False
if lado1 > (lado2 + lado3) or lado2 > (lado1 + lado3) or lado3 > (lado1 + lado2):
    cond2 = False
if lado1 <= abs(lado2 - lado3) or lado2 <= abs(lado1 - lado3) or lado3 <= abs(lado1 - lado2):
    cond3 = False

triangulo = True

if cond1 == False or cond2 == False or cond3 == False:
    triangulo = False
    print('\nNenhum triãngulo encontrado motivo(s) : ')
    if cond1 == False:
        print('Pelo menos um dos lados e ingual a 0.')
    if cond2 == False:
        print('Pelo menos um dos lados e ingual a soma dos outros.')
    if cond3 == False:
        print('Um dos lados e ingual ou menor que o módulo da diferença')

elif lado1 == lado2 == lado3 :
    print('\ntriângulo equilatero')
elif lado1 != lado2 or lado1 != lado3 or lado3 != lado2:
    print('\ntriângulo escaleno')
else:
    print('\ntriãngulo isóceles')

if triangulo:
    print(f'medida do lado 1 : {lado1:.2f}')
    print(f'medida do lado 2 : {lado2:.2f}')
    print(f'medida do lado 3 : {lado3:.2f}')