'''Construa um programa que receba do usuário o valor do
salário mínimo atual. Na sequência, o programa deve solicitar
que o usuário informe o valor do seu salário mensal. Ao fim, o
programa deve calcular a quantidade de salários mínimos recebidos pelo usuário. '''

salario_minimo = int(input('Qual o Sálario minimo atual? '))
salario = int(input('Qual o seu salário mensal? '))
total_de_salario =  salario / salario_minimo 

print(f"Você recebe {total_de_salario:.1f} salário minimos")