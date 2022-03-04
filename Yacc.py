import ply.yacc as yacc
from Lexer import tokens

# Get the token map from the lexer.  This is required.


def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_exponente(p):
    'term : term EXPONENTE factor'
    p[0] = p[1] ** p[3]

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_mod(p):
    'term : term MODULO factor'
    p[0] = p[1] % p[3]

def p_term_divent(p):
    'term : term DIVENTERA factor'
    p[0] = p[1] // p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', "MODULO", "DIVENTERA"),
    ("left", "EXPONENTE")
)


# Build the parser
""" parser = yacc.yacc()


ast = parser.parse('2 * 3 + 4 * (5 - 6)')
print(ast) """

""" while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
 """

