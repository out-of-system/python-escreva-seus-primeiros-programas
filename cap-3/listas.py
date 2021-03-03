'''
Vamos agora aprender a primeira estrutura de dados em Python: Listas!
para declarar uma lista devemos usar [] ex: lista1 = [1,2,3]
diferente de algumas linguagem tipadas como C por exemplo, em Python
uma lista pode ter varios dados de tipos diferentes, e não necessariamente 
de um mesmo tipo, nas listas cada elemento é separado por vírgulas, veja
alguns exemplos de listas abaixo
'''

irmaos = ["Yasmin","Pedro","Mateus"]
idades = [15,10,9]

# também é possivel adicionar uma lista dentro de outra lista 

lista_dois = ["imposto","salario",[1,2,3]]

'''
As listas em Python é uma sequência, assim como as strings somos capazes
de acessar o indice ou algum trecho das listas 
'''

print(irmaos[0])

'''
Por serem mutáveis, podemos atribuir novos valores em uma posição, e substituir
o antigo, por exemplo:
'''
irmaos[0] = "out of system"

print(irmaos)

# para saber o tamanho de uma lista usamos a função len()

print("O tamanho da lista é %i" %(len(irmaos)))

print("A lista dois possui %i elementos!" %(len(lista_dois)))


'''
Quando criamos uma lista vazia, o Python entende isso como sendo False
por exemplo: 
'''

lista = []
if lista:
    print("Nunca vou ser executado!")
else:
    print("Sempre serei executado!")

