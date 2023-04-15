#medicamentos
soma_preco = 0
medicamento = (input('Informe o medicamento: '))
preco = float(input('Agora informe o valor: '))

mais_barato = medicamento
menor_preco = preco
soma_preco += preco

for geris in range (0,5):
    medicamento = (input('Informe o medicamento: '))
    preco = float(input('Agora informe o valor: '))

    
    if preco < menor_preco :
        menor_preco = preco
        mais_barato = medicamento

    soma_preco += preco
    media = soma_preco/5

print(f'O medicamento mais barato e {mais_barato} custa {menor_preco}R$.')
print(f'A média de preços e {media}R$.')
