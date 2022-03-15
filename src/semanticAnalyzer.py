txt = " "
cont = 0


def increaseCont():
    global cont
    cont += 1
    return "%d" % cont


class Node():
    pass


class Program(Node):
    """program = block"""
    p[0] = ["program", p[1]]


class Block(Node):
    '''block : constDecl varDecl procDecl statement'''
    p[0] = ["block", p[1], p[2], p[3], p[4]]

# EXPR
class ExpressionVar(Node):
    """expression : RESERVED VAR ASSIGN expression SEMICOLON"""
    if p[1] == "SET":
        var_name = p[2]
        value = p[4]
        add_var(var_name, value)


class ExpressionArith(Node):
    """expression : arith-expression"""
    p[0] = p[1]


class ExpressionComp(Node):
    """expression : condition"""
    p[0] = p[1]


class ExpressionIf(Node):
    """expression : if-expression"""
    p[0] = p[1]


# IF-expression
# "if-expression : IF condition LBRACE expression RBRACE"
class If(ExpressionIf):
    """if-expression : RESERVED condition expression RBRACE"""
    if (p[1] == "if"):
        condicion = p[3]
        if (p[2] == condicion):

            valor = p[2]
            p[0] = valor
        else:
            pass
    else:
        print("error")


# "if-expression : IF condition LBRACE expression RBRACE ELSE LBRACE expression RBRACE"
class IfElse(ExpressionIf):
    "if-expression : RESERVED condition expression RBRACE RESERVED expression RBRACE"
    if (p[1] == "if" and p[5] == "else"):
        condicion = p[3]
        if (p[2] == condicion):
            p[0] = p[3]
        else:
            p[0] = p[6]
    else:
        print("error")


# condition
class CondArith(ExpressionArith):
    '''condition : arith-expression EQUALS arith-expression
                | arith-expression DIFFERENT arith-expression
                | arith-expression LESSTHAN arith-expression
                | arith-expression MORETHAN arith-expression
                | arith-expression LESSTHANE arith-expression
                | arith-expression MORETHANE arith-expression'''
    if p[2] == "==":
        p[0] = p[1] == p[3]
    elif p[2] == "<>":
        p[0] = p[1] != p[3]
    elif p[2] == "<":
        p[0] = p[1] < p[3]
    elif p[2] == ">":
        p[0] = p[1] > p[3]
    elif p[2] == "<=":
        p[0] = p[1] <= p[3]
    elif p[2] == ">=":
        p[0] = p[1] >= p[3]


class CondNegative(Node):
    "condition : NEGATIVE condition"
    p[0] = not p[2]


# arith-expr
class ArithPlus(ExpressionArith):
    'arith-expression : arith-expression PLUS term'
    p[0] = p[1] + p[3]


class ArithMinus(ExpressionArith):
    'arith-expression : arith-expression MINUS term'
    p[0] = p[1] - p[3]


class ArithTerm(ExpressionArith):
    'arith-expression : term'
    p[0] = p[1]


# TERM
class TermTimes(Node):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]


class TermPower(p):
    'term : term POWER factor'
    p[0] = p[1] ** p[3]


def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]


def p_term_mod(p):
    'term : term MODULE factor'
    p[0] = p[1] % p[3]


def p_term_wholediv(p):
    'term : term WHOLEDIVIDE factor'
    p[0] = p[1] // p[3]


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


# FACTOR
def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]


def p_factor_var(p):
    "factor : VAR"
    value = get_var_value(p[1])
    p[0] = value


def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]


def p_error(p):
    if p == None:
        token = "end of file"
    else:
        token = f"{p.type}({p.value}) on line {p.lineno}"

    print(f"Syntax error: Unexpected {token}")


# Build the parser


""" ast = parser.parse('2 * 3 + 4 * (5 - 6)')
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

"""
Agrega una variable a la tabla de valores
"""


def add_var(var_name, value):
    symbol_table.set(var_name, value)


"""
Retorna el valor de una variable
"""


def get_var_value(var_name):
    value = symbol_table.get(var_name)
    if not value:
        print("NO se encontró la variable")
        return
    return value
