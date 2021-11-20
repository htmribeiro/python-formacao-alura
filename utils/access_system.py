print('*'*50)
print('*{:^48}*'.format(' Access System '))
print('*'*50, end="\n")
print()

usuario = input('Informe o usuário do sistema!\n').capitalize()

if(usuario == "Flávio"):
  print("Seja bem-vindo {}".format(usuario))
elif(usuario == "Douglas"):
    print("Seja bem-vindo {}".format(usuario))
elif(usuario == "Nico"):
  print("Seja bem-vindo {}".format(usuario))
else:
  print("Usuário ({}) não identificado!".format(usuario.upper()))

print('\n{:*^50}'.format(' fim do programa ', end="\n"))
