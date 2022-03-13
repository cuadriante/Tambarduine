from parserCop import *
from lexer import *

code = []
code.append("SET @var1, 5")
code.append("@var1") 
code.append("if 90 < 7 1} else 0}") 
#texto = "if 90 < 7 1} else 0}"

#print_lexer(texto)
#code.append(texto)

parser = yacc.yacc()

for i in code:
    print(parser.parse(i))

