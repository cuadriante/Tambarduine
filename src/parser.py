from numpy import negative
from pyparsing import line
import ply.yacc as yacc
from lexer import tokens
from parsingStructure import *
from symbolTable import SymbolTable, symbol_table
from functionTable import function_table

parser_error = False

precedence = (  # evitar errores del analizador sintactico , definir prioridad de tokens

    ('right', 'ASSIGN'),
    ('left', 'LESSTHAN', 'LESSTHANE', 'MORETHAN', 'MORETHANE'),
    ("left", "NEGATIVE"),
    ('left', 'MINUS', 'PLUS'),
    ('left', 'TIMES', 'DIVIDE', 'WHOLEDIVIDE', 'MODULE'),
    ('left', 'POWER'),
    ('left', 'TRUE', 'FALSE'),
)

parsing_symbol_table = SymbolTable()


# ROOT
def p_program(p):
    "program : block"
    # print(symbol_table.symbols)
    # function_table.print_declared_functions()
    # function_table.print_called_functions()
    # print(function_table.declared_functions)
    # print(function_table.called_functions)
    p[0] = program(p[1])


# BLOCK

def p_block(p):
    "block : function_decls main"
    p[0] = block(p[1], p[2])


# funciones


def p_function_decls(p):
    "function_decls : function_decl"
    p[0] = function_decls(p[1])


def p_function_decls_function_decl(p):
    "function_decls : function_decls function_decl"
    p[1].add(p[2])
    p[0] = p[1]


def p_functions_decl_empty(p):
    "function_decl : empty"
    p[0] = p[1]


def p_function_decl(p):
    "function_decl : DEF VAR LPAREN function_decl_params RPAREN LBRACE function_body RBRACE SEMICOLON"
    # function_table.add(p[2], p[4])
    # if p[7].statements != None:
    #     function_table.declare_new_variables(p[2], p[7].get_var_decls())
    p[0] = function_decl(p[2], p[4], p[7])


def p_function_decl_param_var(p):
    "function_decl_param : VAR"
    p[0] = function_decls_param(p[1])


def p_function_decl_param_empty(p):
    "function_decl_param : empty"
    p[0] = function_decls_param(p[1])


def p_function_decl_param_to_params(p):
    "function_decl_params : function_decl_param"
    p[0] = p[1]


def p_function_decl_params(p):
    "function_decl_params : function_decl_params ASSIGN function_decl_param"
    p[1].add(p[3])
    p[0] = p[1]


def p_function_body_statements(p):
    "function_body : statements"
    p[0] = function_body(p[1])


# MAIN) +


def p_main(p):
    "main : PRINCIPAL LPAREN RPAREN LBRACE statements RBRACE SEMICOLON"
    p[0] = main(p[5])


# statements


def p_statement_statements(p):
    """statements : statement"""
    p[0] = p[1]


def p_statements(p):
    """statements : statements statement"""
    p[1].add(p[2].statement_list[0])
    p[0] = p[1]


def p_statement(p):
    """statement : for_loop
                | if_statement
                | en_caso
                | var_decl
                | callable_function
                | bool_statement
                | function_call"""
    p[0] = statement(p[1])


def p_statement_empty(p):
    """statement : empty"""
    p[0] = p[1]


def p_negative(p):
    """factor : MINUS factor"""
    line = p.lineno(2)
    p[0] = negative(p[2], line)


# FUNCTION_CALL


def p_function_call(p):
    "function_call : EXEC VAR LPAREN params RPAREN SEMICOLON"
    # function_table.call(p[2], p[4])
    p[0] = function_call(p[2], p[4])


# VAR-DECL


def p_var_decl(p):
    """var_decl : SET VAR ASSIGN expression SEMICOLON"""
    parsing_symbol_table.set(p[2], p[4].exec())
    line = p.lineno(3)
    parsing_symbol_table.set_lineno(p[2], line)
    parsing_symbol_table.print()
    p[0] = var_decl(p[2], p[4], line)


# Funciones booleanas
def p_bool_statements(p):
    """bool_statement : boolean_neg
                    | boolean_true
                    | boolean_false"""
    p[0] = p[1]


def p_boolean_neg(p):
    'boolean_neg : SET VAR NEG SEMICOLON'
    p[0] = bool_statement(p[2], p[3])


def p_boolean_to_true(p):
    'boolean_true : SET VAR TRUE SEMICOLON'
    p[0] = bool_statement(p[2], p[3])


def p_boolean_to_false(p):
    'boolean_false : SET VAR FALSE SEMICOLON'
    p[0] = bool_statement(p[2], p[3])


# EXPR


def p_expression_arith(p):
    'expression : arith-expression'
    p[0] = expression(p[1])


def p_expression_boolean(p):
    'expression : BOOL'
    p[0] = expression(p[1])


# IF
def p_if(p):
    "if_statement : IF condition LBRACE statements RBRACE"
    p[0] = if_statement(p[2], p[4])


def p_if_else(p):
    "if_statement : IF condition LBRACE statements RBRACE ELSE LBRACE statements RBRACE"
    p[0] = if_statement(p[2], p[4], p[8])


def p_if_expr(p):
    "if_statement : IF expression LBRACE statements RBRACE"
    p[0] = if_statement(p[2], p[4])


def p_if_else_expr(p):
    "if_statement : IF expression LBRACE statements RBRACE ELSE LBRACE statements RBRACE"
    p[0] = if_statement(p[2], p[4], p[8])


"""
FOR
"""


def p_for_step(p):
    "for_loop : FOR VAR TO factor STEP NUMBER LBRACE statements RBRACE"
    p[0] = for_loop(p[2], p[4], p[8], p[6])


def p_for(p):
    "for_loop : FOR VAR TO factor LBRACE statements RBRACE"
    p[0] = for_loop(p[2], p[4], p[6])


# en_caso


def p_en_caso_0(p):
    "en_caso : ENCASO switch_list_0 SINO LBRACE statements RBRACE FINENCASO SEMICOLON"
    p[0] = en_caso(p[2], p[5])


def p_swich_0(p):
    "switch0 : CUANDO condition ENTONS LBRACE statements RBRACE"
    p[0] = switch0(p[2], p[5])


def p_switch0_to_list(p):
    "switch_list_0 : switch0"
    p[0] = switch_list0(p[1])


def p_swich_0_list(p):
    "switch_list_0 : switch_list_0 switch0"
    p[1].add(p[2])
    p[0] = p[1]


def p_en_caso_1(p):
    "en_caso : ENCASO expression switch_list_1 SINO LBRACE statements RBRACE FINENCASO SEMICOLON"
    p[0] = en_caso(p[3], p[6], p[2])


def p_switch_1(p):
    "switch1 : CUANDO semi_condition ENTONS LBRACE statements RBRACE"
    p[0] = switch1(p[2], p[5])


def p_switch1_to_list(p):
    "switch_list_1 : switch1"
    p[0] = switch_list1(p[1])


def p_swich_1_list(p):
    "switch_list_1 : switch_list_1 switch1"
    p[1].add(p[2])
    p[0] = p[1]


# condition


def p_cond_arith(p):
    "condition : arith-expression semi_condition"
    line = p.lineno(1)
    p[0] = condition(p[1], p[2], line)


# semi_condition


def p_semi_condition(p):
    """semi_condition : EQUALS expression
                | DIFFERENT expression
                | LESSTHAN expression
                | MORETHAN expression
                | LESSTHANE expression
                | MORETHANE expression"""
    line = p.lineno(2)
    p[0] = semi_condition(p[1], p[2], line)


# arith-expr


def p_arith_plus(p):
    """arith-expression : arith-expression PLUS term
                        | arith-expression MINUS term"""
    p[0] = arith_expr(p[3], p[1], p[2])


def p_arith_term(p):
    'arith-expression : term'
    p[0] = arith_expr(p[1])


# TERM
def p_term(p):
    """term : term TIMES factor
            | term DIVIDE factor
            | term MODULE factor
            | term WHOLEDIVIDE factor
            | term POWER factor"""
    p[0] = term(p[3], p[1], p[2])


def p_term_factor(p):
    'term : factor'
    p[0] = term(p[1])


# FACTOR


def p_factor_num(p):
    'factor : NUMBER'
    line = p.lineno(1)
    p[0] = factor(p[1], line)


def p_factor_var(p):
    "factor : VAR"
    line = p.lineno(1)
    p[0] = factor(p[1], line)


def p_factor_expr(p):
    'factor : LPAREN arith-expression RPAREN'
    line = p.lineno(2)
    p[0] = factor(p[2], line)


def p_empty(p):
    'empty : '
    pass


def p_callable_function(p):
    """callable_function : abanico
                        | vertical
                        | percutor
                        | golpe
                        | vibrato
                        | metronomo
                        | print   """
    p[0] = callable_function(p[1])


# FUNCIONES
def p_abanico(p):
    "abanico : ABANICO LPAREN params RPAREN SEMICOLON"
    p[0] = abanico(p[3])


def p_vertical(p):
    "vertical : VERTICAL LPAREN params RPAREN SEMICOLON"
    p[0] = vertical(p[3])


def p_percutor(p):
    "percutor : PERCUTOR LPAREN params RPAREN SEMICOLON"
    p[0] = percutor(p[3])


def p_golpe(p):
    "golpe : GOLPE LPAREN params RPAREN SEMICOLON"
    p[0] = golpe(p[3])


def p_vibrato(p):
    "vibrato : VIBRATO LPAREN params RPAREN SEMICOLON"
    p[0] = vibrato(p[3])


def p_metronomo(p):
    "metronomo : METRONOMO LPAREN params RPAREN SEMICOLON"
    p[0] = metronomo(p[3])


def p_print(p):
    "print : PRINT LPAREN params RPAREN SEMICOLON"
    p[0] = printer(p[3])


def p_params(p):
    """params : params ASSIGN param"""
    p[1].add(p[3])
    p[0] = p[1]


def p_params_param(p):
    "params : param"
    p[0] = p[1]


def p_params_string(p):
    """param : STRING
            | expression"""
    p[0] = param(p[1])


def p_params_empty(p):
    "param : empty"
    p[0] = p[1]


def p_error(p):
    global parser_error
    parser_error = True
    if p == None:
        token = "end of file"
    else:
        token = f"{p.type}({p.value}) on line {p.lineno}"
    raise Exception(f"Syntax error: Unexpected {token}")
    # print(f"Syntax error: Unexpected {token}")


def get_parser_error():
    global parser_error
    return parser_error

