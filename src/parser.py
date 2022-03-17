from ast import parse
from cgi import print_arguments
from lib2to3.pgen2.token import NUMBER

from matplotlib.pyplot import get

from symbolTable import SymbolTable
import ply.yacc as yacc
import os
import codecs
import re
from lexer import tokens
from sys import stdin


class VarAccessNode:
    def __init__(self, var_name_tok):
        self.var_name_tok = var_name_tok


class VarAssignNode:
    def __init__(self, var_name_tok, value_node):
        self.var_name_tok = var_name_tok
        self.value_node = value_node


symbol_table = SymbolTable()

precedence = (  # evitar errores del analizador sintactico , definir prioridad de tokens
    ('right', 'ASSIGN'),
    ('left', 'LESSTHAN', 'LESSTHANE', 'MORETHAN', 'MORETHANE'),
    ("left", "NEGATIVE"),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'WHOLEDIVIDE', 'MODULE'),
    ('left', 'POWER'),
    ('left', 'TRUE', 'FALSE'),
)


# ROOT
def p_program(p):
    "program : block"
    p[0] = p[1]


# BLOCK
# bloack : functions main


def p_block(p):
    "block : main"
    p[0] = p[1]


""" 
#FUNCTIONS
def p_functions(p):
    "functions : empty"
"""

# MAIN


def p_main(p):
    "main : line"
    p[0] = p[1]


# line
def p_line_expr(p):
    """line : expression
        | var_decl"""
    p[0] = p[1]


def p_line_boolean_neg(p):
    "line : boolean_neg"
    p[0] = p[1]




# VAR-DECL
def p_var_decl(p):
    """var_decl : SET var_assigment_list SEMICOLON"""


# VAR-ASSIGMENT-LIST
def p_var_assigment(p):
    """var_assigment_list : VAR ASSIGN expression """
    var_name = p[1]
    value = p[3]
    add_var(var_name, value)


def p_var_assigment_list(p):
    """var_assigment_list : var_assigment_list VAR ASSIGN expression """
    print("multiple")
    var_name = p[2]
    value = p[4]
    add_var(var_name, value)


# Negacion
def p_boolean_neg(p):
    'boolean_neg : SET VAR NEG SEMICOLON'
    valor_original = symbol_table.get(p[2])

    if valor_original == 1:
        symbol_table.cambiar_valor(p[2], 0)
    else:
        symbol_table.cambiar_valor(p[2], 1)


# EXPR


def p_expression_arith(p):
    'expression : arith-expression'
    p[0] = p[1]


def p_expression_boolean(p):
    'expression : BOOL'
    p[0] = p[1]


def p_expression_comp(p):
    'expression : condition'
    p[0] = p[1]


def p_expression_if(p):
    'expression : if-expression'
    p[0] = p[1]


def p_expression_for(p):
    'expression : for-loop'
    p[0] = p[1]


# IF-expression
def p_if(p):
    "if-expression : IF condition LBRACE expression RBRACE"
    condicion = p[2]
    if(condicion == True):

        valor = p[4]
        p[0] = valor
    else:
        pass

def p_if_else(p):
    "if-expression : IF condition LBRACE expression RBRACE ELSE LBRACE expression RBRACE"
    condicion = p[2]
    if(condicion == True):
        p[0] = p[4]
    else:
        p[0] = p[8]

"""
FOR
"""
#Sin variable declarada antes
def p_for(p):
    "for-loop : FOR VAR TO factor STEP NUMBER LBRACE expression RBRACE" 
    variable_name = p[2]
    if symbol_table.get(variable_name):
        pass
    else:
        add_var(variable_name, 0)


# condition
def p_cond_arith(p):
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


def p_cond_negative(p):
    "condition : NEGATIVE condition"
    p[0] = not p[2]


# arith-expr
def p_arith_plus(p):
    'arith-expression : arith-expression PLUS term'
    p[0] = p[1] + p[3]


def p_arith_minus(p):
    'arith-expression : arith-expression MINUS term'
    p[0] = p[1] - p[3]


def p_arith_term(p):
    'arith-expression : term'
    p[0] = p[1]


# TERM
def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]


def p_term_exponente(p):
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
    value = symbol_table.get(p[1])
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


""" def p_empty(p):
    '''
    empty :
    '''
    pass """

"""
Agrega una variable a la tabla de valores
"""


def add_var(var_name, value):
    symbol_table.set(var_name, value)
