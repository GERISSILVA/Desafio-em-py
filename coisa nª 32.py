print('='*40)
razao = int(input('Informe a Razão da PA: '))
pt    = int(input('Informe a primeiro termo da PA: '))
quantidade_de_termo = int(input('Informe a quantidade de termo da PA: '))
print('='*40)

for pa in range (0 , quantidade_de_termo ):
    print(pa * razao,'..', end='')

print('\n','='*40)