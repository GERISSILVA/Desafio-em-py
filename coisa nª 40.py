reprovado = 0
aprovado = 0
prova_final = 0

for geris in range (5):
    nota1 = float(input('\033[mQual foi a primeira nota do aluno? ' ))
    nota2 = float(input('Qual foi a segunda nota do aluno? ' ))
    print('\033[32m-='*40)
    media = (nota1 + nota2 ) / 2

    if media < 2:
        reprovado += 1
    if media > 2 and media <6:
        prova_final += 1
    if media >6:
        aprovado += 1 

print(f'\033[m{prova_final} alunos vão fazer prova final.  ')
print('\033[35m-='*40)
print(f'\033[m{aprovado} alunos foram aprovados. ')
print('\033[35m-='*40)
print(f'\033[m{reprovado} alunos foram reprovados.')