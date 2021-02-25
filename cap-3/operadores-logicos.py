'''
Os operadores lógicos em Python são: and, or e not 
respectivamente são eles: e, ou e negação
veja o exemplo a baixo 
'''

imposto = float(input("Imposto: "))
if imposto < 10.:
    print("Baixo")
elif imposto >= 10. and imposto <= 27.:
    print("Médio")
elif imposto > 27. and imposto < 100:
    print("Alto")
else:
    print("Imposto Inválido")