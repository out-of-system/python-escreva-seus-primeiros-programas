# O loop pode ser interrompido com o comando break, veja no exemplo a baixo


salario = input("Digite o salario: ")
salario = int(salario)

imposto = 27

while imposto > 0:
    imposto = input("Digite o imposto ou (s) para sair: ")
    if not imposto: 
        imposto = 27
    elif imposto == 's' or imposto == 'S':
        break
    else:
        imposto = float(imposto)
    print("Valor real: {0}".format(salario - (salario * (imposto * 0.01))))