"""
Em Python existem 3 tipos de números embutidos: float, int e complex.
Números inteiros são virtualmente ilimitados, e podem crescer até 
o limite da memória, os números float são implementados usando
o tipo double do C. Os números complexos não são usados no dia a dia
de um programador, eles são formados por duas partes float e são
utilizados em Estatistica
"""

# Gerando números a partir de funções

numero_inteiro = int('753') # gerando um número inteiro a partir de uma string
numero_ponto_flutuante = float(1.2)
numero_ponto_flutuante2 = float(1.) # tambem é um ponto flutuante
numero_complexo = complex(1,2)

print(numero_inteiro)
print(numero_ponto_flutuante)
print(numero_ponto_flutuante2)
print(numero_complexo)
