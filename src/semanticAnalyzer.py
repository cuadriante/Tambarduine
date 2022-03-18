import ply.yacc as yacc

from lexer import *
from symbolTable import symbol_table


class VarAccessNode:
    def __init__(self, var_name_tok):
        self.var_name_tok = var_name_tok


class VarAssignNode:
    def __init__(self, var_name_tok, value_node):
        self.var_name_tok = var_name_tok
        self.value_node = value_node


precedence = (  # evitar errores del analizador sintactico , definir prioridad de tokens
    ('right', 'ASSIGN'),
    ('left', 'LESSTHAN', 'LESSTHANE', 'MORETHAN', 'MORETHANE'),
    ("left", "NEGATIVE"),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'WHOLEDIVIDE', 'MODULE'),
    ('left', 'POWER'),
    ('left', 'TRUE', 'FALSE'),
)


def run_semantic_analysis(codigo):
    parser = yacc.yacc()
    parser.parse(codigo)


def is_number(variable):
    return (isinstance(variable, int) or isinstance(variable, float))


def is_boolean(variable):
    return (variable == 'True' or variable == 'False')


def validate_number_operation(simbolo1, simbolo2):
    if(is_boolean(simbolo1) or is_boolean(simbolo2)):
        raise Exception("No se pueden operar valores booleanos")

    try:
        eval(simbolo1)
        eval(simbolo2)
    except:
        raise Exception("Solamente se puede operar con numeros")


def p_progam_empty(p):
    "program : empty"


def p_progam_var_decls(p):
    "program : var_decls"


# Declaraciones
def p_var_decls(p):
    """var_decls : var_decl"""
    p[0] = p[1]


def p_var_decl(p):
    """var_decl : var_decls SET VAR ASSIGN expression SEMICOLON"""
    p[0] = p[5]


def p_var_decl_expression(p):
    """var_decl : SET VAR ASSIGN expression SEMICOLON"""
    p[0] = p[4]

# Expresiones


def p_expression_arith(p):
    'expression : arith-expression'
    p[0] = p[1]


def p_expression_boolean(p):
    'expression : BOOL'
    p[0] = p[1]

# Aritmeticas


def p_arith_plus(p):
    'arith-expression : arith-expression PLUS term'
    simbolo1 = str(p[1])
    simbolo2 = str(p[3])
    validate_number_operation(simbolo1, simbolo2)
    p[0] = eval(simbolo1) + eval(simbolo2)


def p_arith_minus(p):
    'arith-expression : arith-expression MINUS term'
    simbolo1 = str(p[1])
    simbolo2 = str(p[3])
    validate_number_operation(simbolo1, simbolo2)
    p[0] = eval(simbolo1) - eval(simbolo2)


def p_arith_term(p):
    'arith-expression : term'
    p[0] = p[1]


# TERM
def p_term_times(p):
    'term : term TIMES factor'
    simbolo1 = str(p[1])
    simbolo2 = str(p[3])
    validate_number_operation(simbolo1, simbolo2)
    p[0] = eval(simbolo1) * eval(simbolo2)


def p_term_exponente(p):
    'term : term POWER factor'
    simbolo1 = str(p[1])
    simbolo2 = str(p[3])
    validate_number_operation(simbolo1, simbolo2)
    p[0] = eval(simbolo1) ** eval(simbolo2)


def p_term_div(p):
    'term : term DIVIDE factor'
    simbolo1 = str(p[1])
    simbolo2 = str(p[3])
    validate_number_operation(simbolo1, simbolo2)
    p[0] = eval(simbolo1) / eval(simbolo2)


def p_term_mod(p):
    'term : term MODULE factor'
    simbolo1 = str(p[1])
    simbolo2 = str(p[3])
    validate_number_operation(simbolo1, simbolo2)
    p[0] = eval(simbolo1) % eval(simbolo2)


def p_term_wholediv(p):
    'term : term WHOLEDIVIDE factor'
    simbolo1 = str(p[1])
    simbolo2 = str(p[3])
    validate_number_operation(simbolo1, simbolo2)
    p[0] = eval(simbolo1) // eval(simbolo2)


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

# FACTOR


def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]


def p_factor_var(p):
    "factor : VAR"
    value = symbol_table.get(p[1])
    p[0] = value


def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]


def p_empty(p):
    "empty :"

# txt = " "
# cont = 0

# def increaseCont():
#     global cont
#     cont += 1
#     return "%d" % cont

# class Node():
#     pass

# class Program(Node):
#     """program = block"""
#     p[0] = ["program", p[1]]

# class Block(Node):
#     '''block : constDecl varDecl procDecl statement'''
#     p[0] = ["block", p[1], p[2], p[3], p[4]]

# # EXPR
# class ExpressionVar(Node):
#     """expression : RESERVED VAR ASSIGN expression SEMICOLON"""
#     if p[1] == "SET":
#         var_name = p[2]
#         value = p[4]
#         add_var(var_name, value)

# class ExpressionArith(Node):
#     """expression : arith-expression"""
#     p[0] = p[1]

# class ExpressionComp(Node):
#     """expression : condition"""
#     p[0] = p[1]

# class ExpressionIf(Node):
#     """expression : if-expression"""
#     p[0] = p[1]

# # IF-expression
# # "if-expression : IF condition LBRACE expression RBRACE"
# class If(ExpressionIf):
#     """if-expression : RESERVED condition expression RBRACE"""
#     if (p[1] == "if"):
#         condicion = p[3]
#         if (p[2] == condicion):

#             valor = p[2]
#             p[0] = valor
#         else:
#             pass
#     else:
#         print("error")

# # "if-expression : IF condition LBRACE expression RBRACE ELSE LBRACE expression RBRACE"
# class IfElse(ExpressionIf):
#     "if-expression : RESERVED condition expression RBRACE RESERVED expression RBRACE"
#     if (p[1] == "if" and p[5] == "else"):
#         condicion = p[3]
#         if (p[2] == condicion):
#             p[0] = p[3]
#         else:
#             p[0] = p[6]
#     else:
#         print("error")

# # condition
# class CondArith(ExpressionArith):
#     '''condition : arith-expression EQUALS arith-expression
#                 | arith-expression DIFFERENT arith-expression
#                 | arith-expression LESSTHAN arith-expression
#                 | arith-expression MORETHAN arith-expression
#                 | arith-expression LESSTHANE arith-expression
#                 | arith-expression MORETHANE arith-expression'''
#     if p[2] == "==":
#         p[0] = p[1] == p[3]
#     elif p[2] == "<>":
#         p[0] = p[1] != p[3]
#     elif p[2] == "<":
#         p[0] = p[1] < p[3]
#     elif p[2] == ">":
#         p[0] = p[1] > p[3]
#     elif p[2] == "<=":
#         p[0] = p[1] <= p[3]
#     elif p[2] == ">=":
#         p[0] = p[1] >= p[3]

# class CondNegative(Node):
#     "condition : NEGATIVE condition"
#     p[0] = not p[2]

# # arith-expr
# class ArithPlus(ExpressionArith):
#     'arith-expression : arith-expression PLUS term'
#     p[0] = p[1] + p[3]

# class ArithMinus(ExpressionArith):
#     'arith-expression : arith-expression MINUS term'
#     p[0] = p[1] - p[3]

# class ArithTerm(ExpressionArith):
#     'arith-expression : term'
#     p[0] = p[1]

# # TERM
# class TermTimes(Node):
#     'term : term TIMES factor'
#     p[0] = p[1] * p[3]

# class TermPower(p):
#     'term : term POWER factor'
#     p[0] = p[1] ** p[3]

# def p_term_div(p):
#     'term : term DIVIDE factor'
#     p[0] = p[1] / p[3]

# def p_term_mod(p):
#     'term : term MODULE factor'
#     p[0] = p[1] % p[3]

# def p_term_wholediv(p):
#     'term : term WHOLEDIVIDE factor'
#     p[0] = p[1] // p[3]

# def p_term_factor(p):
#     'term : factor'
#     p[0] = p[1]txt = " "
# cont = 0

# def increaseCont():
#     global cont
#     cont += 1
#     return "%d" % cont

# class Node():
#     pass

# class Program(Node):
#     """program = block"""
#     p[0] = ["program", p[1]]

# class Block(Node):
#     '''block : constDecl varDecl procDecl statement'''
#     p[0] = ["block", p[1], p[2], p[3], p[4]]

# # EXPR
# class ExpressionVar(Node):
#     """expression : RESERVED VAR ASSIGN expression SEMICOLON"""
#     if p[1] == "SET":
#         var_name = p[2]
#         value = p[4]
#         add_var(var_name, value)

# class ExpressionArith(Node):
#     """expression : arith-expression"""
#     p[0] = p[1]

# class ExpressionComp(Node):
#     """expression : condition"""
#     p[0] = p[1]

# class ExpressionIf(Node):
#     """expression : if-expression"""
#     p[0] = p[1]

# # IF-expression
# # "if-expression : IF condition LBRACE expression RBRACE"
# class If(ExpressionIf):
#     """if-expression : RESERVED condition expression RBRACE"""
#     if (p[1] == "if"):
#         condicion = p[3]
#         if (p[2] == condicion):

#             valor = p[2]
#             p[0] = valor
#         else:
#             pass
#     else:
#         print("error")

# # "if-expression : IF condition LBRACE expression RBRACE ELSE LBRACE expression RBRACE"
# class IfElse(ExpressionIf):
#     "if-expression : RESERVED condition expression RBRACE RESERVED expression RBRACE"
#     if (p[1] == "if" and p[5] == "else"):
#         condicion = p[3]
#         if (p[2] == condicion):
#             p[0] = p[3]
#         else:
#             p[0] = p[6]
#     else:
#         print("error")

# # condition
# class CondArith(ExpressionArith):
#     '''condition : arith-expression EQUALS arith-expression
#                 | arith-expression DIFFERENT arith-expression
#                 | arith-expression LESSTHAN arith-expression
#                 | arith-expression MORETHAN arith-expression
#                 | arith-expression LESSTHANE arith-expression
#                 | arith-expression MORETHANE arith-expression'''
#     if p[2] == "==":
#         p[0] = p[1] == p[3]
#     elif p[2] == "<>":
#         p[0] = p[1] != p[3]
#     elif p[2] == "<":
#         p[0] = p[1] < p[3]
#     elif p[2] == ">":
#         p[0] = p[1] > p[3]
#     elif p[2] == "<=":
#         p[0] = p[1] <= p[3]
#     elif p[2] == ">=":
#         p[0] = p[1] >= p[3]

# class CondNegative(Node):
#     "condition : NEGATIVE condition"
#     p[0] = not p[2]

# # arith-expr
# class ArithPlus(ExpressionArith):
#     'arith-expression : arith-expression PLUS term'
#     p[0] = p[1] + p[3]

# class ArithMinus(ExpressionArith):
#     'arith-expression : arith-expression MINUS term'
#     p[0] = p[1] - p[3]

# class ArithTerm(ExpressionArith):
#     'arith-expression : term'
#     p[0] = p[1]

# # TERM
# class TermTimes(Node):
#     'term : term TIMES factor'
#     p[0] = p[1] * p[3]

# class TermPower(p):
#     'term : term POWER factor'
#     p[0] = p[1] ** p[3]

# def p_term_div(p):
#     'term : term DIVIDE factor'
#     p[0] = p[1] / p[3]

# def p_term_mod(p):
#     'term : term MODULE factor'
#     p[0] = p[1] % p[3]

# def p_term_wholediv(p):
#     'term : term WHOLEDIVIDE factor'
#     p[0] = p[1] // p[3]

# def p_term_factor(p):
#     'term : factor'
#     p[0] = p[1]

# # FACTOR
# def p_factor_num(p):
#     'factor : NUMBER'
#     p[0] = p[1]

# def p_factor_var(p):
#     "factor : VAR"
#     value = get_var_value(p[1])
#     p[0] = value

# def p_factor_expr(p):
#     'factor : LPAREN expression RPAREN'
#     p[0] = p[2]

# def p_error(p):
#     if p == None:
#         token = "end of file"
#     else:
#         token = f"{p.type}({p.value}) on line {p.lineno}"

#     print(f"Syntax error: Unexpected {token}")

# # Build the parser

# """ ast = parser.parse('2 * 3 + 4 * (5 - 6)')
# print(ast) """

# """ while True:
#     try:
#         s = input('calc > ')
#     except EOFError:
#         break
#     if not s: continue
#     result = parser.parse(s)
#     print(result)
# """

# """
# Agrega una variable a la tabla de valores
# """

# def add_var(var_name, value):
#     symbol_table.set(var_name, value)

# """
# Retorna el valor de una variable
# """

# def get_var_value(var_name):
#     value = symbol_table.get(var_name)
#     if not value:
#         print("NO se encontró la variable")
#         return
#     return value

# # FACTOR
# def p_factor_num(p):
#     'factor : NUMBER'
#     p[0] = p[1]

# def p_factor_var(p):
#     "factor : VAR"
#     value = get_var_value(p[1])
#     p[0] = value

# def p_factor_expr(p):
#     'factor : LPAREN expression RPAREN'
#     p[0] = p[2]

# def p_error(p):
#     if p == None:
#         token = "end of file"
#     else:
#         token = f"{p.type}({p.value}) on line {p.lineno}"

#     print(f"Syntax error: Unexpected {token}")

# # Build the parser

# """ ast = parser.parse('2 * 3 + 4 * (5 - 6)')
# print(ast) """

# """ while True:
#     try:
#         s = input('calc > ')
#     except EOFError:
#         break
#     if not s: continue
#     result = parser.parse(s)
#     print(result)
# """

# """
# Agrega una variable a la tabla de valores
# """

# def add_var(var_name, value):
#     symbol_table.set(var_name, value)

# """
# Retorna el valor de una variable
# """

# def get_var_value(var_name):
#     value = symbol_table.get(var_name)
#     if not value:
#         print("NO se encontró la variable")
#         return
#     return value
