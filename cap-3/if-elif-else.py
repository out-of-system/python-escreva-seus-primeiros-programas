'''
Em Python os blocos de condicionais if e elif são executados caso uma expressão
seja verdadeira, no caso de nenhuma expressão if ou elif ser verdadeira o bloco 
do else é executado 
'''


imposto = float(input("Imposto: "))

if imposto < 10:
    print("Médio")
elif imposto < 27.5:
    print("Alto")
else:
    print("Muito Alto!")
