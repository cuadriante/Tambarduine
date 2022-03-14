from parser import *
from lexer import *

code = []
"""
code.append("SET @var1, 7")
code.append("@var1") 
code.append("if 1 < 7 {1 } else {0}")
code.append("SET, @var1, 7")  """

texto = "for @var1 to @var1 Step { 5}"

print_lexer(texto)
#code.append(texto)

parser = yacc.yacc()

for i in code:
    print(parser.parse(i))

