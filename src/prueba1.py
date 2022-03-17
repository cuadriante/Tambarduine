from parser import *
from lexer import *

code = []


code.append("SET @var1, True;")
code.append("@var1")
code.append("SET @var1.T;")
code.append("@var1")
# code.append("SET @var2, 7-3;")
# code.append("SET @234, 8 @luz, 56;")
# code.append("@234")
# code.append("@luz")
# code.append("@var1")
# code.append("if 1 < 7 {1 } else {0}")
# code.append("if 10 < 7 {1 } else {0}")
# code.append("if 4 < 7 {1 }")
# code.append("for @var1 to @var1 Step 4 { 5}")


# print_lexer(texto)
# code.append(texto)

parser = yacc.yacc()

for i in code:
    # print_lexer(i)
    result = parser.parse(i)
    print(result)
