from parserCop import *
from lexer import *

# READ FILE
document_to_compile = "prueba2.tam"
test = document_to_compile
fp = codecs.open(test, 'r', None, 'strict', - 1)
arr = fp.read()
fp.close()

# LEXER - LEXICAL ANALYSIS
lexer.input(arr)
print_lexer(arr)

# PARSER - SYNTACTIC ANALYSIS
parser = yacc.yacc()
print(parser.parse(arr))

# SEMANTIC ANALYSIS
