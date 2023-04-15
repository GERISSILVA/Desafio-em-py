enfermeiro = 0
nutricionista = 0
medico = 0

soma = 0

while True:
    codigo = int(input('Informe o codigo do cargo: '))
    if codigo == 0:
        break    
    salario = float(input('Informe o salário: '))

    print('-='*20)
    print('Digite 0 para encerar o programa.')

    if codigo == 1:
        enfermeiro += 1
    elif codigo == 2:
        nutricionista += 1
        soma += salario
    elif codigo == 3:
        medico += 1
    
        

media_nutri = soma / nutricionista

print(f'A media de salário dos nutricionista e {media_nutri}R$. ')

