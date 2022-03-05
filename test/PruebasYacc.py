from src.parser import *

operaciones = [
    "3 + 5 -2",
    "4*3/2",
    "(5-3)*3",
    "5%2",
    "5*5 -3",
    "15//2",
    "2**3",
    "3*4 + 2**2",
    "(2+1)**2"
]

soluciones = [
    6,
    6,
    6,
    1,
    22,
    7,
    8,
    16,
    9
]

parser = yacc.yacc()
resultados = []

for i in operaciones:
    resultados.append(parser.parse(i))
    
for i in range(len(resultados)):
    if resultados[i] == soluciones[i]:
        isCorrecta = True
    else:
        isCorrecta = False
    print(f"Operación:  {operaciones[i]}  |  Resultado: {resultados[i]}  |  Solución: {soluciones[i]}  |  Correcta: {isCorrecta} ")

