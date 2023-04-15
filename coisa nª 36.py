altura = float(input('Informe a altura do aluno: '))
soma = altura
cont = 1
maior_altura = altura
menor_altura = altura

while True:
    altura = float(input('Informe a altura do aluno: '))
    cont += 1
    
    soma += altura
    if altura == 0:
        break
    if altura > maior_altura:
        maior_altura = altura
    if altura < menor_altura:
        menor_altura = altura
   
media = soma / cont

print(f'O aluno mais alto mede {maior_altura}.m')
print(f'O aluno mais baixo mede {menor_altura}.m')
print(f'A média de altura dos aluno é {media}')