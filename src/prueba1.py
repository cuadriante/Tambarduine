from pyparsing import line
from parser import *
from lexer import *

parser = yacc.yacc()

# code = []

# code.append("SET @var1, True;")
# code.append("SET @var1.Neg;")
# # code.append("@var1")
# # code.append("@var1")
# # code.append("SET @var2, 7-3;")
# # code.append("SET @234, 8 @luz, 56;")
# # code.append("@234")
# # code.append("@luz")
# # code.append("@var2")
# # code.append("if 1 < 7 {1 } else {0}")
# # code.append("if 10 < 7 {1 } else {0}")
# # code.append("if 4 < 7 {1 }")
# # code.append("for @var1 to @var1 Step 4 { 5}")

# # print_lexer(texto)
# # code.append(texto)

# for i in code:
#     print_lexer(i)
#     # result = parser.parse(i)
#     # print(result)


'''Hay que correr la prueba desde src para que encuentra prueba.txt'''

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
