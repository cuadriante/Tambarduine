import ply.yacc as yacc
from lexer import tokens
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
    p[0] = p[1]


# BLOCK
# bloack : functions main


def p_block(p):
    "block : function_decls main"
    p[0] = p[1]

# funciones


def p_function_decls(p):
    "function_decls : function_decl"
    p[0] = p[1]


def p_function_decls_function_decl(p):
    "function_decls : function_decls function_decl"
    p[0] = p[1]


def p_functions_decl_empty(p):
    "function_decls : empty"
    p[0] = p[1]


def p_function_decl(p):
    "function_decl : DEF VAR LPAREN function_decl_params RPAREN LBRACE statements RBRACE SEMICOLON"
    params = p[4].split(',')
    function_table.add(p[2], params)
    p[0] = str(p[4])


def p_function_decl_params_var(p):
    "function_decl_params : VAR"
    p[0] = p[1]


def p_function_decl_params(p):
    "function_decl_params : function_decl_params ASSIGN VAR"
    p[0] = str(p[1]) + ', ' + str(p[3])


def p_function_call(p):
    "function_call : EXEC VAR LPAREN params RPAREN SEMICOLON"
    p[0] = str(p[2]) + ',' + str(p[4])
    params = p[4].split(',')
    function_table.call(p[2], params)

# MAIN) +


def p_main(p):
    "main : PRINCIPAL LPAREN RPAREN LBRACE statements RBRACE SEMICOLON"
    print("main")
    p[0] = p[5]

# statements


def p_statements_empty(p):
    """statements : empty"""


def p_statements(p):
    """statements : statement
                | statements statement"""


def p_statement(p):
    """statement : for_loop
                | if_statement
                | en_caso
                | var_decls
                | callable_function
                | bool_statement
                | function_call"""
    print("statement")
    p[0] = p[1]

# #MINI_STATEMENTS
# def p_mini_statements(p):
#     """mini_statements : var_decls
#                     | callable_function
#                     | bool_statement"""

# VAR-DECL


def p_var_decl(p):
    """var_decl : SET VAR ASSIGN expression SEMICOLON"""
    symbol_table.set(p[2], p[4])
    print("Variable")


def p_var_decls(p):
    """var_decls : var_decls var_decl"""
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


def p_boolean_neg(p):
    'boolean_neg : SET VAR NEG SEMICOLON'
    # valor_original = symbol_table.get(p[2])

    # if valor_original == 'True':
    #     symbol_table.cambiar_valor(p[2], 'False')
    # else:
    #     symbol_table.cambiar_valor(p[2], 'True')


def p_boolean_to_true(p):
    'boolean_true : SET VAR TRUE SEMICOLON'
    # symbol_table.cambiar_valor(p[2], 'True')


def p_boolean_to_false(p):
    'boolean_false : SET VAR FALSE SEMICOLON'
    # symbol_table.cambiar_valor(p[2], 'False')

# EXPR


def p_expression_arith(p):
    'expression : arith-expression'
    p[0] = p[1]


def p_expression_boolean(p):
    'expression : BOOL'
    p[0] = p[1]


# IF
def p_if(p):
    "if_statement : IF condition LBRACE statements RBRACE"
    print("if")
    condicion = p[2]
    if(condicion == True):

        valor = p[4]
        p[0] = valor
    else:
        pass


def p_if_else(p):
    "if_statement : IF condition LBRACE statements RBRACE ELSE LBRACE statements RBRACE"
    print("elseif")
    condicion = p[2]
    if(condicion == True):
        p[0] = p[4]
    else:
        p[0] = p[8]


"""
FOR
"""


def p_for(p):
    "for_loop : FOR VAR TO factor STEP NUMBER LBRACE statements RBRACE"
    print("for_loop")


# en_caso
def p_en_caso_0(p):
    "en_caso : ENCASO switch_list_0 SINO LBRACE statements RBRACE FINENCASO SEMICOLON"


def p_swich_0(p):
    "switch_list_0 : CUANDO condition ENTONS LBRACE statements RBRACE"


def p_swich_0_list(p):
    "switch_list_0 : switch_list_0 CUANDO condition ENTONS LBRACE statements RBRACE"


def p_en_caso_1(p):
    "en_caso : ENCASO expression switch_list_1 SINO LBRACE statements RBRACE FINENCASO SEMICOLON"


def p_switch_1(p):
    "switch_list_1 : CUANDO semi_condition ENTONS LBRACE statements RBRACE"


def p_switch_1_list(p):
    "switch_list_1 : switch_list_1 CUANDO semi_condition ENTONS LBRACE statements RBRACE"


# condition


def p_cond_arith(p):
    "condition : arith-expression semi_condition"
    print("condition")
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

# semi_condition


def p_semi_condition(p):
    """semi_condition : EQUALS expression
                | DIFFERENT expression
                | LESSTHAN expression
                | MORETHAN expression
                | LESSTHANE expression
                | MORETHANE expression"""
    print("semi_condition")
    p[0] = (p[1], p[2])


# arith-expr
def p_arith_plus(p):
    'arith-expression : arith-expression PLUS term'
    p[0] = str(p[1]) + str(p[2]) + str(p[3])


def p_arith_minus(p):
    'arith-expression : arith-expression MINUS term'
    p[0] = str(p[1]) + str(p[2]) + str(p[3])


def p_arith_term(p):
    'arith-expression : term'
    p[0] = str(p[1])


# TERM
def p_term_times(p):
    'term : term TIMES factor'
    p[0] = str(p[1]) + str(p[2]) + str(p[3])


def p_term_exponente(p):
    'term : term POWER factor'
    p[0] = str(p[1]) + str(p[2]) + str(p[3])


def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = str(p[1]) + str(p[2]) + str(p[3])


def p_term_mod(p):
    'term : term MODULE factor'
    p[0] = str(p[1]) + str(p[2]) + str(p[3])


def p_term_wholediv(p):
    'term : term WHOLEDIVIDE factor'
    p[0] = str(p[1]) + str(p[2]) + str(p[3])


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
    p[0] = str(p[1]) + str(p[2]) + str(p[3])


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
    print("función llamable")


# FUNCIONES
def p_abanico(p):
    "abanico : ABANICO LPAREN params RPAREN SEMICOLON"
    print(p[1])


def p_vertical(p):
    "vertical : VERTICAL LPAREN params RPAREN SEMICOLON"
    print(p[1])


def p_percutor(p):
    "percutor : PERCUTOR LPAREN params RPAREN SEMICOLON"
    print(p[1])


def p_golpe(p):
    "golpe : GOLPE LPAREN params RPAREN SEMICOLON"
    print(p[1])


def p_vibrato(p):
    "vibrato : VIBRATO LPAREN params RPAREN SEMICOLON"
    print(p[1])


def p_metronomo(p):
    "metronomo : METRONOMO LPAREN params RPAREN SEMICOLON"
    print(p[1])


def p_print(p):
    "print : PRINT LPAREN params RPAREN SEMICOLON"
    p[0] = p[3]


def p_params(p):
    """params : params ASSIGN param"""
    p[0] = str(p[1]) + ',' + str(p[3])


def p_params_param(p):
    "params : param"
    p[0] = p[1]


def p_param_num(p):
    "param : expression"
    p[0] = p[1]


def p_params_string(p):
    "param : STRING"
    string_con_comillas = p[1]
    # string_sin_comillas = string_con_comillas.split('"')[1]
    p[0] = string_con_comillas


def p_params_empty(p):
    "param : empty"
    p[0] = p[1]


def p_error(p):
    if p == None:
        token = "end of file"
    else:
        token = f"{p.type}({p.value}) on line {p.lineno}"

    print(f"Syntax error: Unexpected {token}")
