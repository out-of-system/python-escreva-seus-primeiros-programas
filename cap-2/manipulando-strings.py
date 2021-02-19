"""
Em Python a string é um tipo ou uma classe, diferente da linguagem C,
em python não existe o tipo char, que ocupa o espaço de 1 byte para 
representar um valor da tabela ASCII, portanto uma string é uma sequencia
de caracteres
"""


"""
Em python é normal usarmos aspas simples ou duplas para declarar uma string,
mas também existe a possibilidade de usarmos as multiline strings, basicamente são 
três aspas simples ou duplas, essa formatação é bastante usada para saida no console
"""

print("""\
Uso: consulta_base [OPCOES]

    -h                        exibe saida de ajuda
    -U url                    url do dataset
    
""")


"""
Como dito anteriormente as string em Python é uma sequência de caracteres
e podemos acessar a posição de cada caractere dentro dessa string com a sintaxe
'nome_variavel[index]', o index é a posição que queremos acessar, lembre-se que
a primeira posição começa no 0 (zero)
"""

name = "out of system"
print(name[0]) # acessando a primeira posição da string

"""
Antes de querermos acessar a posição de um alguma string, é importante saber 
qual o tamanho dela, pra isso usamos a função len(str)
"""

tamanho_string = len(name)
print(tamanho_string)

print(name[-13]) # acessando a primeira posição de tras para frente


"""
Em Python existe um termo conhecido como 'slice notation', podemos pegar
alguns trechos de uma string, por exemplo vamos pegar apenas as três primeiras
letras do meu nick 
"""
print(name[:3]) # a saida sera >> out


# printando somente 'system'
print(name[7:]) # a saida sera >> system

# printando somente 'of'
print(name[4:-7])


"""
Além dos indices e slice notation no Python também podemos realizar outras
operações com as strings como: x in y (se x está em y ), x not in y ( se x não esta em y),
x + y ( concatenação de x com y ) e x * y ( repetições de x em y)
"""

print("m" in name) # retorna True, pois M está na ultima posição da string
print("g" not in name) # retorna True, por G NÃO está na string
print("outofsystem" * 3) # usando o operador aritmetico para replicar a string