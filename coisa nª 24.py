altura = float(input('Informe a estatura da primeira pessoa: '))
altura2 = float(input('Informe a estatura de outra pessoa: '))
altura3 = float(input('Informe outra estatura: '))
maior = 0

if altura == altura2 or altura2 == altura3 or altura == altura3:
    print('Há, pelo menos, 2 pessoas com a mesma estatura')
else:
    if altura > altura2 or altura > altura3 :
         maior = altura
    if altura2 > altura or altura2 > altura3 :
         maior = altura2
    if altura3 > altura or altura3 > altura2:
         maior = altura3
    
    print(f'A maior altura é {maior}')