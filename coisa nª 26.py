venda = int(input('Qual Foi o valor total da venda? '))

print('---- COMO DESEJA PAGAR ----')
print('='*30 ,'\n1- Á vsita (em espécie) \n2- Cartão de débito \n3- Cartão de crédito (Vencimento)')
print('='*30)

opc = int(input('Escolha uma opção: '))

if opc == 1:
    total = venda - venda * (15/100) 
    print(f'O valor total é {total}')
elif opc == 2:
    total = venda - venda * (10/100)
    print(f'O valor total é {total}')
elif opc == 3:
    total = venda - venda * (5/100)
    print(f'O valor total é {total}')
else:
    print('Opção inválida')