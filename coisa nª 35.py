soma_tempo = 0
print('\033[31m-='*40)
nome = input('\033[mQual o nome do nadador? ')
tempo = int(input('Qual foi o tempo dele? '))
print('\033[31m-='*40)
#entre 12 e 15 seg 
tempo_entre_12_e_15_seg = 0


if tempo >12 and tempo <15:
    tempo_entre_12_e_15_seg += 1

soma_tempo += tempo
#melhores tempo

melhor_tempo = tempo
melhor_nadador = nome
#piore tempo

pior_tempo = tempo
pior_nadador = nome

for geris in range(6):
    nome = input('\033[mQual o nome do nadador? ')
    tempo = int(input('\033[mpQual foi o tempo dele? '))
    print('\033[31m-='*40)
    soma_tempo += tempo

    
    if tempo >12 and tempo <15:
        tempo_entre_12_e_15_seg += 1

    if tempo < melhor_tempo:
        melhor_tempo = tempo
        melhor_nadador = nome
    if tempo > pior_tempo :
        pior_tempo = tempo
        pior_nadador = nome
    
    tempo_medio = soma_tempo / 7

print('\033[36m-='*40)
print(f'\033[mO melhor nadador foi {melhor_nadador} com tempo de {melhor_tempo} seg.')
print('\033[36m-='*40)
print(f'\033[mO pior nadador foi {pior_nadador} com o tempo de {pior_tempo} seg.')
print('\033[36m-='*40)
print(f'\033[mA média de tempo foi {tempo_medio}')
print('\033[36m-='*40)
print(f'\033[m{tempo_entre_12_e_15_seg} Nadadores completaram a prova entre 12 e 15 seg.')
print('\033[36m-='*40)