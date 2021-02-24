salario = int(input("Salario ?\n-> "))

imposto = float(input("Imposto em % (ex: 27.5%) ? \n-> "))

print("Valor real: {0}".format(salario - (salario * (imposto * 0.01))))

# com o decorrer da leitura, vamos aprimorando esse programa com condicionais e loops