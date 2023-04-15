'''• Até 5 camisas, desconto de 3%
• Acima de 5 camisas e até 10 camisas, desconto de
5%; e
• Acima de 10 camisas, desconto de 7%.
o preço da camisa é R$ 12,50'''

'''camisa = int(input('Óla, quantas camisas você comprou? '))

preço = 12,50 
desconto = preço
ptotal = preço * camisa

if camisa <= 5:
  ptotal = ptotal * (1 - 3/100)
  print (f'Você comprou {camisa}, que da um total de R${ptotal}')
else:
  if camisa  <=10 :
    ptotal = ptotal * (1 - 5/100)
    print (f'Você comprou {camisa}, que da um total de R${ptotal}')
  else :
    ptotal = ptotal * (1 - 7/100)
    print (f'Você comprou {camisa}, que da um total de R${ptotal}')
'''

numeroCamisas = int(input("Quantidade de camisas: "))
valorCamisa = 12.50
valorFinal = numeroCamisas * valorCamisa
if numeroCamisas <= 5:
 valorFinal = valorFinal * (1 - 3/100)
else:
 if numeroCamisas <= 10:
  valorFinal = valorFinal * (1 - 5/100)
 else:
  valorFinal = valorFinal * (1 - 7/100)
print(f"Valor final: R$ {valorFinal:.2f}")