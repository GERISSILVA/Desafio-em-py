
maiordeidade = 0
mulheres = 0

while True :
    idade = int(input('Qual idade do aluno? '))
    if idade < 0:
        break
   
    sexo  = input('Qual o sexo do aluno? [M/F]')
   
    if sexo == 'F' or sexo == 'f':
        mulheres +=1
    
    elif idade > 18 :
        if sexo == 'm' or sexo == 'M':
            maiordeidade +=1

       
print(f'Foram informados {maiordeidade} homens maiores de idade. ')
print(f'Foram informados {mulheres} mulheres.')
