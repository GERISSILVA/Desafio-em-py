Cargo = str(input('Qual seu cargo: ')).upper()
salario = int(input('Informe seu salário: '))

if Cargo == 'PROGRAMADORDESISTEMAS' :
    salario = salario + salario * (30/100)
    print(F'O seu salário agora é {salario}')
elif Cargo == 'ANALISTADESISTEMAS':
    salario = salario + salario * (20/100)
    print(f'O salário agora é {salario}')
elif Cargo == 'ANALISTADEBANCODEDADOS':
    salario = salario + salario * (15/100)
    print(f'O seu salário agora é {salario}')
else:
    print('Cargo inválido!!!!!')