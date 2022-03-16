from parserCop import *
from lexer import *

code = []


code.append("SET @var1, 7-3;")
code.append("SET @234, 8 @luz, 56;")
code.append("@var1") 
code.append("@234") 
code.append("@luz") 
#code.append("if 1 < 7 {1 } else {0}")
#code.append("for @var1 to @var1 Step { 5}")


texto = "for @var1 to @var1 Step { 5}"

#print_lexer(texto)
#code.append(texto)

parser = yacc.yacc()

for i in code:
    #print_lexer(i)
    print(parser.parse(i))

