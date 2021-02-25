'''
O comando while em Python avalia uma expressão e executa um bloco de código
até que esta seja avaliada como False
'''


salario = input("Digite seu salario: ")
salario = int(salario)

imposto = 27

while imposto > 0:
    imposto = input("Digite o imposto ou (0) para sair: ")
    if not imposto:
        imposto = 27
    else:
        imposto = float(imposto)
    print("Valor real: {0}".format(salario - (salario * (imposto * 0.01))))