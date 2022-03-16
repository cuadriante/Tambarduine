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

precedence = ( # evitar errores del analizador sintactico , definir prioridad de tokens
    ('right', 'ASSIGN'),
    ('left', 'LESSTHAN', 'LESSTHANE', 'MORETHAN', 'MORETHANE'),
    ("left", "NEGATIVE"),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'WHOLEDIVIDE', 'MODULE'),
    ('left', 'POWER'),
    ('left', 'TRUE', 'FALSE'),
    )
    

#ROOT
def p_program(p):
    "program : block"
    p[0] = p[1]

#BLOCK
#bloack : functions main
def p_block(p):
    "block : main"
    p[0] = p[1]

""" 
#FUNCTIONS
def p_functions(p):
    "functions : empty"
"""

#MAIN
def p_main(p):
    "main : line"
    p[0] = p[1]


#line 
def p_line(p):
    """line : expression
        | var_decl"""
    p[0] = p[1]

""" #expression_list
def p_expression_list(p):
    expression_list : expression
                    |expression_list expression
    p[0] = p[1]
"""

#VAR-DECL
def p_var_decl(p):
    """var_decl : SET var_assigment_list SEMICOLON"""
    

#VAR-ASSIGMENT-LIST
def p_var_assigment(p):
    """var_assigment_list : VAR ASSIGN expression """
    print("una")
    var_name = p[1]
    value = p[3]
    add_var(var_name, value)

def p_var_assigment_list(p):
    """var_assigment_list : var_assigment_list VAR ASSIGN expression """ 
    print("multiple")
    var_name = p[2]
    value = p[4]
    add_var(var_name, value)

#EXPR
def p_expression_arith(p):
    'expression : arith-expression'
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





#IF-expression
#"if-expression : IF condition LBRACE expression RBRACE"
def p_if(p):
    "if-expression : RESERVED condition expression RBRACE"
    if(p[1] == "if"):
        condicion = p[3]
        if(p[2] == condicion):
            
            valor = p[2]
            p[0] = valor
        else:
            pass
    else:
        print("error")
#"if-expression : IF condition LBRACE expression RBRACE ELSE LBRACE expression RBRACE"
def p_if_else(p):
    "if-expression : RESERVED condition expression RBRACE RESERVED expression RBRACE"
    if(p[1] == "if" and p[5]=="else"):
        condicion = p[3]
        if(p[2] == condicion):
            p[0] = p[3]
        else:
            p[0] = p[6]
    else:
        print("error")

"""
FOR
"""
def p_for(p):
    "for-loop : RESERVED VAR RESERVED factor RESERVED NUMBER expression RBRACE"
    print("Hola")
    variable_name = p[2]
    if get_var_value(variable_name):
        pass
    else:
        add_var(variable_name, 0)




#condition
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


#arith-expr
def p_arith_plus(p):
    'arith-expression : arith-expression PLUS term'
    p[0] = p[1] + p[3]
def p_arith_minus(p):
    'arith-expression : arith-expression MINUS term'
    p[0] = p[1] - p[3]
def p_arith_term(p):
    'arith-expression : term'
    p[0] = p[1]




#TERM
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

#FACTOR
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

"""
Retorna el valor de una variable
"""
def get_var_value(var_name):
    value = symbol_table.get(var_name)
    if not value:
        return 
    return value



