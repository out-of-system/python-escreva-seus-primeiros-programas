"""
Os principais métodos de strings em Python pode ser encontrado na documentação 
em [https://docs.python.org/3/library/stdtypes.html#string-methods], mas os métodos
mais utilizados são eles: capitalize, count, endswith, join, split, startswith e 
replace
"""

name = "out of system"

print(name.capitalize()) # o método capitalize() deixa a primeira letra em maiúscula
print(name.count('o')) 
# no método count() passamos como parâmetro uma letra, e o método diz quantas letras
# possui naquela string 
print(name.startswith('a')) 
# o método acima retorna True ou False, ele basicamente verifica se a string começa 
# com o parâmetros que passamos para a função
print(name.endswith('z')) # retorna False, pois a string não termina com Z
print("copa de 2014".split(" "))
# o método split() tira os espaços da string se passarmos um espaço no parâmetro
print(" ".join(["Copa","de","2014"]))
# o método join() se passarmos um espaço como parâmetro, ele adiciona na string