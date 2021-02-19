"""
A função type(Obj), passamos um parâmetro para ela, e ela retorna o tipo
ou a Classe de um objeto, na dúvida use-a para descobrir o tipo de um objeto
referenciado por uma variável 
"""

name = "out of system"
age = 19
isHuman = True

print(type(name))
print(type(age))
print(type(isHuman))


'''
A função isinstance() é uma função que diz se um objeto pertence a uma classe,
no exemplo a baixo, perguntamos para a função se a variavel 'name' é uma instancia
da classe 'string' e ela retorna True ou False
'''

teste = isinstance(name, str)
print(teste)
teste2 = isinstance(name, int)
print(teste2)