pares = 0
impar = 0
for c in range (0,5):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        pares +=1
    else:
        impar +=1

print(f'Você digitou {pares} números pares.')