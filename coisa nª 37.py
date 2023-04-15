idade = int(input('INFORME A IDADE DO ALUNO: '))

soma = 0
cont = 0
maior_idade = idade
menor_idade = idade

while True:
    idade = int(input('INFORME A IDADE DO ALUNO: '))
    
    if idade < 0:
        break
    if idade > maior_idade:
        maior_idade = idade
    if idade < menor_idade:
        menor_idade = idade
    if idade > menor_idade and idade < maior_idade:
        soma += idade
        cont += 1
    
media = soma / cont
#print(soma , cont)
print(f'O aluno mais novo tem {menor_idade} anos.')
print(f'O aluno mais velho tem {maior_idade} anos. ')
print(f'A média de idade e de {media:.2f} anos.')