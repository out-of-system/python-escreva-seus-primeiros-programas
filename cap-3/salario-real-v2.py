'''
No Brasil, grande parte das pessoas paga a mesma cota de impostos,
podemos dizer que existe um valor padrão, e usa-lo caso o usuario não saiba.
Vamos utilizar um if e verificar se o usuario deixou o input vazio, caso ele
deixe vamos utilizar o valor padrão, se não vamos utilizar o valor que o usuario
digitou no input
'''


salario = input("Digite seu salario: ")
salario = int(salario)

imposto = input("Digite o imposto em % (exemplo 27.5%): ")

if imposto == '':
    imposto = 27.5
else:
    imposto = float(imposto)

print("Valor real: {0}".format(salario - (salario * (imposto * 0.01))))


'''
Caso o usuário não entre com um valor em imposto e apenas tecle Enter, a variavel
imposto ira armazenar uma string vazia ""  e vai entrar no primeiro bloco do if,
sendo assim atribuido o valor 27.5 a essa variavel, caso o usuario digite um valor
ele irá cair no segundo bloco, transformando o texto que ele digitou em um número
float
'''