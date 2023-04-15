#Sistema de caixa eletronico frentista
cont = 0
nome = input('Qual seu nome? ')
senha = 123456
while True:
    senha = int(input(f'Qual sua senha, {nome}? '))
    cont += 1
    
    if senha == 123456:
        print(f'Olá, {nome}. Seja Bem-Vindo ao nosso banco!')
        break
    if senha != 123456:
            if cont == 1:
                 print('"SENHA INCORRETA!", Você ainda tem 2 tentativas.')
            if cont == 2:
                 print('"SENHA INCORRETA!", Você ainda tem 1 tentativas.')
            if cont == 3:
                
                 print('SUA SENHA FOI BLOQUEADA, por favor dirija-se a um dos caixas.')
                 break
