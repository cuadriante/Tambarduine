import ply.lex as lex
from symbolTable import symbol_table

lexer_error = False

# List of token names.   This is always required
tokens = (
    'IN',
    'BOOL',
    'NEG',
    'ID',
    'NUMBER',
    'PLUS',
    'MINUS',
    'NEGATIVE',
    'TIMES',
    'POWER',
    'DIVIDE',
    "MODULE",
    'WHOLEDIVIDE',
    'EQUAL',
    'EQUALS',
    'DIFFERENT',
    'LESSTHAN',
    'MORETHAN',
    'LESSTHANE',
    'MORETHANE',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'ASSIGN',
    'COMMENT',
    'VAR',
    'SEMICOLON',
    'FUNCTION',
    'TRUE',
    'FALSE',
    'STRING',
    'PARAM',
    'PRINTLN',
)

reserved = {
    "Principal": "PRINCIPAL",
    "SET": "SET",
    "Abanico": "ABANICO",
    "Vertical": "VERTICAL",
    "Percutor": "PERCUTOR",
    "Golpe": "GOLPE",
    "Vibrato": "VIBRATO",
    "Metronomo": "METRONOMO",
    "If": "IF",
    "Else": "ELSE",
    "for": "FOR",
    "to": "TO",
    "Step": "STEP",
    "EnCaso": "ENCASO",
    "EnTons": "ENTONS",
    "Cuando": "CUANDO",
    "SiNo": "SINO",
    "type" : "TYPE",
    "FinEnCaso": "FINENCASO",
    "Exec": "EXEC",
    "Def": "DEF",
}


tokens = tokens + tuple(reserved.values())
# tokens = tokens + reserved
# print(tokens)

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_NEGATIVE = r'-'
t_POWER = r'\*\*'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MODULE = r"%"
t_WHOLEDIVIDE = r'//'
t_EQUAL = r'='
t_EQUALS = r'=='
t_DIFFERENT = r'<>'
t_LESSTHAN = r'<'
t_MORETHAN = r'>'
t_LESSTHANE = r'<='
t_MORETHANE = r'>='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ASSIGN = r','
t_SEMICOLON = r';'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_ignore = ' \t'
t_TRUE = r'.T'
t_FALSE = r'.F'
t_STRING = r'".*"'
# t_STRING = r'[a-zA-Z?][a-zA-Z?]*'

# Declare the state


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Error handling rule
def t_error(t):
    global lexer_error
    lexer_error = True
    # raise Exception("Illegal character '%s'" % t.value[0])
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# A regular expression rule with some action code


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_BOOL(t):
    r'((t|T)rue)|((f|F)alse)'
    t.value = 'True' if (t.value == 'true' or t.value == 'True') else 'False'
    return t


def t_NEG(t):
    r'.Neg'
    return t


def t_COMMENT(t):
    r'\#.*'
    pass  # No return value. Token discarded


def t_VAR(t):
    r'@[a-zA-Z_0-9?]{3,10}'
    t.type = reserved.get(t.value, 'VAR')  # Check for reserved words
    # if not symbol_table.get(t.value):
    #     symbol_table.set(t.value, -1)
    return t


def t_PRINTLN(t):
    r'println!'
    t.type = reserved.get(t.value, 'PRINTLN')  # Check for reserved words
    # if not symbol_table.get(t.value):
    #     symbol_table.set(t.value, -1)
    return t

def t_ID(t):
    r'[a-zA-Z_0-9?][a-zA-Z_0-9?]*'
    if t.value in reserved:
        t.value = t.value.upper()
        t.type = t.value
        return t
    else:
        print("Illegal character '%s'" % t.value)
        t.lexer.skip(1)


# def get_lexer_error():
#     # global lexer_error
#     return lexer_error


lexer = lex.lex()
