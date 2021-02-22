"""
Em Python quando queremos criar uma variável devemos usar a sintaxe 
variavel = expressão, esse sinal de igual '=' na programação 
recebe o nome de atribuição, por exemplo vamos fazer uma calculadora
simples
"""

imposto = 0.27
salario = 5000

salario = salario - (salario * imposto)
print(salario)

"""
Percebe-se que o resultado dessa operações é um float, como visto antes no 
capitulo de coerção 
"""

salario = 3000
print("Valor real: {0}".format(salario - (salario * imposto)))