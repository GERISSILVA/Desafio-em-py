print('====== TABELA VERDADE ======\n1- Operaador AND \n2- Operador OR \n3- Operador NOT')
opc = int(input('Escolha uma opção: '))

if opc == 1:
    bit1 = bool(int(input('Digite um bit (0 ou 1): ')))
    bit2 = bool(int(input('Digite outro bit (0 ou 1): ')))
    resultado = bit1 and bit2
    print(f'{resultado}')
elif opc == 2:
    bit1 = bool(int(input('Digite um bit (0 ou 1): ')))
    bit2 = bool(int(input('Digite outro bit (0 ou 1): ')))
    resultado = bit1 or bit2
    print(f'{resultado}')
elif opc == 3:
    bit = bool(int(input('Informe um bit (0 ou 1): ')))
    resultado = not bit
    print(f'{resultado}')
else:
    print('OPÇÃO INVPALIDA!!!')
    