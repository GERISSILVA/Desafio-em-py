'''Uma empresa, que presta serviço à companhia de energia
elétrica do estado, necessita de um programa que auxilie os
seus eletricistas no cálculo das principais grandezas da Eletricidade que são Tensão, Resistência e Corrente. Sabe-se que
U=Ri,
onde, U é a Tensão (em V), R é a Resistência (em Ώ) e i a Corrente
(em A).'''


print('='*30)
print('  CALCULO DE GRANDEZAS ELÉTRICAS      ')
print('='*30)
print('1- Tensão  (EM VOLT) \n2- Resistência (EM OHM) \n3- Corrente (EM AMPÉRE))')
print('='*30)
escolha = int(input('Qual grandeza deseja calcular? '))
if escolha == 1:
    resistencia = int(input('Informe o valor da corrente (em ohm) '))
    corrente = int(input('Informe o valor da corrente (em ampére) '))
    tensao = resistencia * corrente
    print(f'tensao = {tensao}')
elif escolha == 2:
    tensao = int(input('Informe o valor da tensão (em volt) '))
    corrente = int(input('Informe o valor da corrente em (em ampére) '))
    resistencia = tensao / corrente
    print(f'resistência = {resistencia}')
elif escolha == 3:
    resistencia = int(input('Informe o valor da corrente (em ohm) '))
    tensao = int(input('Informe o valor da tensão (em volt) '))
    corrente = tensao / resistencia 
    print(f'corrente = {corrente}')
else:
   print('Escolha invalida ')