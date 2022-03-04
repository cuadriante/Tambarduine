import ply.lex as lex

reserved = {
    "abanico" : "ABANICO",
    "vertical" : "VERTICAL",
    "percutor" : "PERCUTOR",
    "golpe" : "GOLPE",
    "vibrato" : "VIBRATO",
    "metronomo" : "METRONOMO",
    "print!" : "PRINT!",
    "if" : "IF",
    "else" : "ELSE",
    "while" : "WHILE",
    "for" : "FOR",
}


tokens = [
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    "EXPONENTE",
    "DIVENTERA",
    'DIVIDE',
    "MODULO",
    'LPAREN',
    'RPAREN',
    "ID",
    "COMMENT"
] 

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_EXPONENTE = r"\*\*"
t_MODULO = r"%"
t_DIVENTERA = r"//"

t_ignore  = ' \t'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_COMMENT(t):
     r'\#.*'
     pass
     # No return value. Token discarded

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

""" 
# Test it out
data = " 3 + 4 * 10 + -20 *2"

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)
     """