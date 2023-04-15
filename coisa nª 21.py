#login 1
usuario = 'procopio'
senha = 12345

#login 2
usuario = 'paiva'
senha = 54321

usuario = str(input('Informe seu usuario: ')) 
senha = int(input('Informe a senha: '))

if usuario == "procopio" and senha == 12345:
    print('Seja bem-vindo!')
elif usuario == 'paiva' and senha == 54321:
    print('Seja bem-vindo')
else:
    print('Usuario e senha não conferem ')