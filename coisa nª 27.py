'''IMC Situação
Abaixo de 18,5 Abaixo do peso
Acima de 18,5 e menor que 25 Peso normal
A partir de 25 e menor que 30 Sobrepeso
Acima de 30 e menor que 35 Obesidade grau 1
Acima de 35 e menor que 40 Obesidade grau 2
Acima de 40 Obesidade grau 3'''

peso = int(input('iNFORME SEU PESO: '))
altura = float(input('INFORME SUA ALTURA: '))

imc = peso / altura

if imc < 18.5:
    print('Abaixo do peso')
elif imc >18.5  < 25:
    print('Peso normal')
elif imc >25 < 30:
    print('Sobrepeso')
elif imc >30 <35:
  print('Obesidade gra 1')
elif imc >35 <40:
    print('Obesidade grau 2')
else:
    print('Obesidade grau 3')