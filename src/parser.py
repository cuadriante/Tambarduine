from numpy import _2Tuple
import ply.yacc as yacc
from lexer import tokens
from parsingStructure import *
from symbolTable import symbol_table
from functionTable import function_table


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


# ROOT
def p_program(p):
    "program : block"
    print(symbol_table.symbols)
    program = program(p[1])
    p[0] = program


# BLOCK
# bloack : functions main

def p_block(p):
    "block : function_decls main"
    block = block(p[1], p[2])
    p[0] = block
    p[0] = p[1]

# funciones


def p_function_decls(p):
    "function_decls : function_decl"
    p[0] = p[1]


def p_function_decls_function_decl(p):
    "function_decls : function_decls function_decl"
    p[1].next(p[2])
    p[0] = p[1]


def p_functions_decl_empty(p):
    "function_decls : empty"
    p[0] = p[1]


def p_function_decl(p):
    "function_decl : DEF VAR LPAREN function_decl_params RPAREN LBRACE statements RBRACE SEMICOLON"
    params = p[4].split(',')
    function_table.add(p[2], params)
    function_decl = function_decl(p[2], p[4], p[7])
    p[0] = function_decl


def p_function_decl_param_var(p):
    "function_decl_param : VAR"
    function_decls_param = function_decls_param(p[1])
    p[0] = function_decls_param

def p_function_decl_params(p):
    "function_decl_params : function_decl_param"
    p[0] = p[1]
def p_function_decl_params(p):
    "function_decl_params : function_decl_params function_decl_param"
    p[1].next(p[1])
    p[0] = p[1]




# MAIN) +



def p_main(p):
    "main : PRINCIPAL LPAREN RPAREN LBRACE statements RBRACE SEMICOLON"
    print("main")
    main = main(p[5])
    p[0] = main

# statements


def p_statements_empty(p):
    """statements : empty"""


def p_statements(p):
    """statements : statement"""
    p[0] = p[1]

def p_statements(p):
    """statements : statements statement"""
    p[1].set_next(p[2])
    p[0] = p[1]


def p_statement(p):
    """statement : for_loop
                | if_statement
                | en_caso
                | var_decls
                | callable_functions
                | bool_statement
                | function_call"""
    print("statement")
    statement = statement(p[1])
    p[0] = statement

#FUNCTION_CALL

def p_function_call(p):
    "function_call : EXEC VAR LPAREN params RPAREN SEMICOLON"
    p[0] = str(p[2]) + ',' + str(p[4])
    params = p[4].split(',')
    function_table.call(p[2], params)
    function_call = function_call(p[2], p[4])
    p[0] = function_call
# VAR-DECL


def p_var_decl(p):
    """var_decl : SET VAR ASSIGN expression SEMICOLON"""
    var_decl = var_decl(p[2], p[4])
    p[0] = var_decl


def p_var_decls(p):
    """var_decls : var_decls var_decl"""
    p[1].set_next(p[2])
    p[0] = p[1]
    print("Variables")

def p_var_trans(p):
    """var_decls : var_decl"""
    print("varToVars")
    p[0] = p[1]


# Funciones booleanas
def p_bool_statements(p):
    """bool_statement : boolean_neg
                    | boolean_true
                    | boolean_false"""
    p[0] = p[1]


def p_boolean_neg(p):
    'boolean_neg : SET VAR NEG SEMICOLON'
    bool_statement = bool_statement(p[2], p[3])
    p[0] = bool_statement

def p_boolean_to_true(p):
    'boolean_true : SET VAR TRUE SEMICOLON'
    bool_statement = bool_statement(p[2], p[3])
    p[0] = bool_statement


def p_boolean_to_false(p):
    'boolean_false : SET VAR FALSE SEMICOLON'
    bool_statement = bool_statement(p[2], p[3])
    p[0] = bool_statement

# EXPR


def p_expression_arith(p):
    'expression : arith-expression'
    expression = expression(p[1])
    p[0] = expression


def p_expression_boolean(p):
    'expression : BOOL'
    expression = expression(p[1])
    p[0] = expression


# IF
def p_if(p):
    "if_statement : IF condition LBRACE statements RBRACE"
    print("if")
    if_statement = if_statement(p[2], p[4])
    p[0] = if_statement



def p_if_else(p):
    "if_statement : IF condition LBRACE statements RBRACE ELSE LBRACE statements RBRACE"
    print("elseif")
    if_statement = if_statement(p[2], p[4], p[8])
    p[0] = if_statement


"""
FOR
"""
def p_for_step(p):
    "for_loop : FOR VAR TO factor STEP NUMBER LBRACE statements RBRACE"
    print("for_loop_step")
    for_loop = for_loop(p[2], p[4], p[8], p[6])
    p[0] = for_loop

def p_for(p):
    "for_loop : FOR VAR TO factor LBRACE statements RBRACE"
    print("for_loop")
    for_loop = for_loop(p[2], p[4], p[8])
    p[0] = for_loop

# en_caso
def p_en_caso_0(p):
    "en_caso : ENCASO switch_list_0 SINO LBRACE statements RBRACE FINENCASO SEMICOLON"
    en_caso = en_caso(p[2], p[5])
    p[0] = en_caso
    print("en_caso0")

def p_swich_0(p):
    "switch0 : CUANDO condition ENTONS LBRACE statements RBRACE"
    switch_list0 = switch_list0(p[2], p[5])
    p[0] = switch_list0
    print("switch_list0")


def p_swich_0_list(p):
    "switch_list_0 : switch_list_0 switch0"
    p[1].next(p[2])
    p[0] = p[1]
    print("switch_list0")    

def p_en_caso_1(p):
    "en_caso : ENCASO expression switch_list_1 SINO LBRACE statements RBRACE FINENCASO SEMICOLON"
    en_caso = en_caso(p[3], p[6], p[2])
    p[0] = en_caso
    print("en_caso1")

def p_switch_1(p):
    "switch1 : CUANDO semi_condition ENTONS LBRACE statements RBRACE"
    switch_list1 = switch_list1(p[2], p[5])
    p[0] = switch_list1
    print("switch_list1")

def p_swich_1_list(p):
    "switch_list_1 : switch_list_1 switch1"
    p[1].next(p[2])
    p[0] = p[1]
    print("switch_list1")   


# condition


def p_cond_arith(p):
    "condition : arith-expression semi_condition"
    if p[2][0] == "==":
        p[0] = p[1] == p[2][1]
    elif p[2][0] == "<>":
        p[0] = p[1] != p[2][1]
    elif p[2][0] == "<":
        p[0] = p[1] < p[2][1]
    elif p[2][0] == ">":
        p[0] = p[1] > p[2][1]
    elif p[2][0] == "<=":
        p[0] = p[1] <= p[2][1]
    elif p[2][0] == ">=":
        p[0] = p[1] >= p[2][1]
    print("condition")
    condition = condition(p[1], p[2])
    p[0] = condition

# semi_condition


def p_semi_condition(p):
    """semi_condition : EQUALS expression
                | DIFFERENT expression
                | LESSTHAN expression
                | MORETHAN expression
                | LESSTHANE expression
                | MORETHANE expression"""
    print("semi_condition")
    semi_condition = semi_condition(p[1], p[2])
    p[0] = semi_condition


# arith-expr
def p_arith_plus(p):
    """arith-expression : arith-expression PLUS term
                        | arith-expression MINUS term"""
    arith_expr = arith_expr(p[1], p[2], p[3])
    p[0] = arith_expr

def p_arith_term(p):
    'arith-expression : term'
    arith_expr = arith_expr(p[1])
    p[0] = arith_expr


# TERM
def p_term(p):
    """term : term TIMES factor
            | term DIVIDE factor
            | term MODULE factor
            | term WHOLEDIVIDE factor
            | term POWER factor"""
    term = term(p[1], p[2], p[3])
    p[0] = term


def p_term_factor(p):
    'term : factor'
    term = term(p[1])
    p[0] = term

# FACTOR


def p_factor_num(p):
    'factor : NUMBER'
    factor = factor(p[1])
    p[0] = factor


def p_factor_var(p):
    "factor : VAR"
    factor = factor(p[1])
    p[0] = factor



def p_factor_expr(p):
    'factor : LPAREN arith-expression RPAREN'
    factor = factor(p[2])
    p[0] = factor



def p_empty(p):
    'empty :'
    pass


def p_callable_function(p):
    """callable_function : abanico
                        | vertical
                        | percutor
                        | golpe
                        | vibrato
                        | metronomo
                        | print   """
    callable_function = callable_function(p[1])
    p[0] = callable_function
    print("función llamable")


# FUNCIONES
def p_abanico(p):
    "abanico : ABANICO LPAREN params RPAREN SEMICOLON"
    abanico = abanico(p[3])
    p[0] = abanico
    print(p[1])


def p_vertical(p):
    "vertical : VERTICAL LPAREN params RPAREN SEMICOLON"
    vertical = vertical(p[3])
    p[0] = vertical
    print(p[1])


def p_percutor(p):
    "percutor : PERCUTOR LPAREN params RPAREN SEMICOLON"
    percutor = percutor(p[3])
    p[0] = percutor
    print(p[1])


def p_golpe(p):
    "golpe : GOLPE LPAREN params RPAREN SEMICOLON"
    golpe = golpe(p[3])
    p[0] = golpe
    print(p[1])


def p_vibrato(p):
    "vibrato : VIBRATO LPAREN params RPAREN SEMICOLON"
    vibrato = vibrato(p[3])
    p[0] = vibrato
    print(p[1])


def p_metronomo(p):
    "metronomo : METRONOMO LPAREN params RPAREN SEMICOLON"
    metronomo = metronomo(p[3])
    p[0] = metronomo
    print(p[1])


def p_print(p):
    "print : PRINT LPAREN params RPAREN SEMICOLON"
    printer = printer(p[3])
    p[0] = printer

def p_params(p):
    """params : params ASSIGN param"""
    p[1].next(p[3])
    p[0] = p[1]

def p_params_param(p):
    "params : param"
    p[0] = p[1]

def p_params_string(p):
    """param : STRING
            | expression"""
    param = param(p[1])
    p[0] = param


def p_params_empty(p):
    "param : empty"
    p[0] = p[1]


def p_error(p):
    if p == None:
        token = "end of file"
    else:
        token = f"{p.type}({p.value}) on line {p.lineno}"

    print(f"Syntax error: Unexpected {token}")
