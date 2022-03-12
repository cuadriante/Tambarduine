from parserCop import *
from lexer import *

code = []
code.append ("SET @var1, true")


parser = yacc.yacc()

for i in code:
    print(parser.parse(i))

