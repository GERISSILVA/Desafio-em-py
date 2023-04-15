enfermeiro = 0
nutricionista = 0
medico = 0

cont = 0

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
        
    elif codigo == 3 :
        if salario > 4.500:
            cont+=1
        medico += 1
        
        

    
        



print(f'{cont} medicos tem salário superiores a 4.500R$. ')

