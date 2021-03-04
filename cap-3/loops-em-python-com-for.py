'''
O comando for é o responsável por fazer o que é conhecido como loop, na programação
na maioria das vezes queremos repetir mais de um comando, sem ter que escrever ele
varias vezes. A sintaxe do comando for é simples, se quisermos percorrer uma lista 
devemos passar o nome de uma variavel e uma lista, como no exemplo a baixo 
'''

paises = ["Canadá","Rússia","Noruega","Japão","Índia"]


"""
for pais in paises:
    print("Um dia eu quero conhecer {}".format(pais))
"""



'''
Outro recurso interessante no comando for é a utilização do comando continue, no
exemplo a baixo, percorremos uma lista e logo em seguida fazemos um if com a condição
se o pais da lista terminar com "a", ele vai pular para o proximo elemento, ou seja
quando estiver acontecendo o loop, o python vai verificar se aquela variavel termina
com "a", se for verdadeiro ele ignora e pula para a proxima variavel
'''

'''
for pais in paises:
    if pais.endswith("a"):
        continue
    
    print(pais)

'''

'''
Imprimindo os números de 1 ate 10
'''

'''
numeros = [1,2,3,4,5,6,7,8,9,10]

for numero in numeros:
    print(numero)

'''
'''
Mas e se quisermos imprimir do 0 ate o 100 ? Iamos escrever todos os numeros ?
claro que não, para isso usamos uma função chamada range(), com ela é possivel
determinarmos o inicio e o fim de uma sequencia de numeros 
'''
'''
for i in range(5):
    print(i)
'''

'''
É interessante notarmos que se se passar 5 para a função range, ela não ira ir ate
o número 5, ela simplesmente para no 4, quando para ir do 0 ate o 10 por exemplo
deveremos declarar assim na função range(0,11) ou range(11)
'''
'''
for i in range(11):
    print(i)
'''



'''
Se não passarmos o inicio do range, por padrão o python inicializa em 0
ou podemos passar um valor inicial por exemplo range(5,10)
'''
'''
for i in range(5,10):
    print(i)
'''


'''
Algumas vezes precisamos imprimir o conteudo de uma lista, e sua posição nela,
para isso usamos uma função chamado enumerate()
'''


for posicao, pais in enumerate(paises):
    print(posicao,pais)
