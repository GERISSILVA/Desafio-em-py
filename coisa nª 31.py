a  =  int ( input ( "Digite a: " ))
b  =  int ( input ( "Dígito b: " ))
if a  <  b :
   soma  =  0
   for x  in range ( a , b  +  1 ):
    soma  +=  x
    print ( f"Soma dos inteiros no intervalo [ { a } , { b } ] é { soma } ." )
else :
   print ( "ERRO: a deve ser maior que b." )
