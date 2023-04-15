'''Uma imobiliária paga aos seus corretores um salário base
de R$ 1.500,00. Além disso, uma comissão de R$ 200,00 por
cada imóvel vendido e 5% do valor de cada venda. Construa
um programa que solicite o nome do corretor, a quantidade
de imóveis vendidos e o valor total de suas vendas. Ao fim, o
programa deve calcular e escrever o salário final do corretor de
imóveis.'''

nome = str(input('Qual seu nome? '))
quantidade_de_imoveis = int(input('Qual foi a quantidade de imoveis que você vendeu? '))
valor_das_vendas = int(input('Qual foi o valor total das vendas? '))

comissao =  valor_das_vendas * (5/100)
salario = 1500.00 + (200 * quantidade_de_imoveis) + comissao

print(f'{nome}, Você vendeu {quantidade_de_imoveis} imoveis, fazendo um total de {valor_das_vendas:.2f}, ganhando uma comissao de {comissao:.2f}.')
print(f'Seu salário total e de R${salario:.2f}')