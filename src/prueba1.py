from pyparsing import line
from parser import *
from lexer import *

parser = yacc.yacc()

# code = []

# code.append("SET @var1, True;")
# code.append("SET @var1.Neg;")
# code.append("SET @var1, true;")
# code.append("SET @234, 8 @luz, 56;")
# code.append("@234")
# code.append("@luz")
# code.append("@var1")
# code.append("if 1 < 7 {1 } else {0}")
# code.append("if 10 < 7 {1 } else {0}")
# code.append("if 4 < 7 {1 }")
# code.append("for @var1 to @var1 Step 4 { 5}")
# code.append("EnCaso 45 Cuando == 45 Entons {1 } Cuando == 3 Entons {7 } SiNo { 0} FinEnCaso;")


'''Hay que correr la prueba desde src para que encuentre prueba.txt'''

archivo = open('prueba.txt')
codigo = archivo.read()
instrucciones = codigo.split(';')

# print_lexer(codigo)
# print(parser.parse(codigo))

for i in range(len(instrucciones) - 1):
    instruccion = instrucciones[i] + ';'
    print(instruccion)
    # print_lexer(instruccion)
    result = parser.parse(instruccion)
    print(result)
