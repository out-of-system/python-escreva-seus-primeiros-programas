'''
Em Python, quando queremos que o usuário digite um valor, usamos a função input()
com essa função, podemos guardar em uma variável qualquer valor que o usuário digitar
'''

name = input("Digite seu nome: ")
name = name.capitalize() # aqui estamos deixando a primeira letra do nome em maiuscula
print("Olá %s, é um prazer conhece-lo ;)" %(name))
