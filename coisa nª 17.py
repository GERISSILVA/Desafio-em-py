esta1 = float(input('Informe a altura da primeira pessoa: '))
esta2 = float(input('Informe a altura de outra pessoa: '))
esta3 = float(input('Informe a altura de mais uma pessoa: '))

mais_alto = esta1
altur_media = esta1
mais_baixo = esta1

if esta1 > esta2 and esta1 > esta3:
   mais_alto = esta1
   if esta2 > esta3 :
      altur_media = esta2
      mais_baixo = esta3
   else:
      altur_media = esta3
      mais_baixo = esta2

elif esta2 > esta1 and esta2 > esta3:
   mais_alto = esta2
   if esta1 > esta3 :
      altur_media = esta1
      mais_baixo = esta3
   else:
      altur_media = esta3
      mais_baixo = esta1
else :
   mais_alto = esta3
   if esta1 > esta2:
      altur_media = esta1
      mais_baixo = esta2
   else:
      altur_media = esta2
      mais_baixo = esta1

print (f'\n{mais_alto}m, {altur_media}m e {mais_baixo}m')
