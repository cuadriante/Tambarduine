from parser import *

operaciones = [
    ("3 + 5 -2", 6),
    ("4*3/2", 6),
    ("(5-3)*3", 6),
    ("5%2", 1),
    ("5*5 -3", 22),
    ("15//2", 7),
    ("2**3", 8),
    ("3*4 + 2**2", 16),
    ("(2+1)**2", 9),
    ("5*(10//5 + 3) + 24 == 7**2", True),
    (" 5 == 7", False),
    ("4 <> 2", True),
    ("6 <> 6", False),
    ("7 + 5 < 10", False),
    ("10 > 7", True),
    ("8<=10", True),
    ("10>=10", True),
]

parser = yacc.yacc()

resultados = []

for i in operaciones:
    resultados.append(parser.parse(i[0]))

for i in range(len(operaciones) - 1):
    if resultados[i] == operaciones[i][1]:
        isCorrecta = True
    else:
        isCorrecta = False
    print(
        f"Operación:  {operaciones[i][0]}  |  Resultado: {resultados[i]}  |  Solución: {operaciones[i][1]}  |  Correcta: {isCorrecta} ")
