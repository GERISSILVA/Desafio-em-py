n = int(input('Informe a quantidade de vezes para que o número se repita: '))
soma = 0
for c in range (n):
    num = float(input('digite um número: '))
    soma+= num
media = soma / n
print(f'a media e {media}')