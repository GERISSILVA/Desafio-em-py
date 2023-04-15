n = int(input('Digite um número: '))

total = 0

if n % 2 == 0:
    total = n ** 2
    print(f' {n} elevado ao quadrado e = {total}')
    # conferindo se o número e par
else :
    total = n ** 3
    print(f' {n} elevado ao quadrado e = {total}')
    #conferindo se o número e impar