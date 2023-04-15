n = int(input('Escreva um número: '))
n1 = int(input('Escreva outro número: '))

peso1 = 2
peso2 = 3
print('MENU')

print('''1. Média ponderada, com pesos 2 e 3, respectivamente
2. Quadrado da soma dos 2 números
3. Cubo do menor número
''')

opc = int(input('Escolha uma opção: '))
mediapoderana = 0
soma = 0
quadradodasoma = 0
maior = 0
menor = 0
cubo = 0
if opc == 1:
   mediapoderana = (((n * peso1) + (n1 * peso2 )) / (peso1 + peso2))
   print(f'A media poderana é {mediapoderana}')
elif opc == 2:
   soma = n + n1
   quadradodasoma = soma ** 2
   print(f'O quadrado da soma dos numeros = {quadradodasoma}')
elif opc == 3 :
    if n > n1:
       menor = n1
    else :
        menor = n
    cubo = menor ** 3
    print(f'O cubo de {menor} = {cubo}')
else: 
   print('OPÇÃO INVÁLIDA !')