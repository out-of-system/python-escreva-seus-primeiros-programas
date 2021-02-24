'''
No exercicio anterior, usamos o comando if e o operador de igualdade == para verificar
se o usuario entrou com um valor ou não, acontece que uma string vazia em um bloco if
equivale a False, assim como uma lista vazia, poderiamos mudar o if do código anterior
para algo como o código abaixo
'''


salario = input("Digite seu salario: ")
salario = int(salario)


imposto = input("Digite o imposto em % (exemplo 27.5%): ")

if not imposto:
    imposto = 27.5
else:
    imposto = float(imposto)


print("Valor real: {0}".format(salario - (salario * (imposto * 0.01))))
