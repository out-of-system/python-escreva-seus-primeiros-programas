"""
Em Python as strings são imutaveis, ou seja elas tem seu valor atribuido na
hora da criação, e novas strings são criadas a partir das operações com elas,
se tentarmos mudar o valor de uma posição ou um trecho, o Python retorna um erro
"""

minha_string = "livro python 3"
# minha_string[13] = "2" essa parte do código retorna um erro!

# mas existem outras formas de alterar uma string
print(len(minha_string)) # printando o tamanho da string
minha_string = minha_string[0:13] + "2" # aqui estamos atribuindo o valor da variavel a ela mesma e somando + 2
print(minha_string)

minha_string = "livro python 3"
minha_string = minha_string.replace("3", "2")
# a função acima replace(old, new), recebe dois parametros, o antigo que é o primeiro, e o novo que vai substituir o antigo
print(minha_string)