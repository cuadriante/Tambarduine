import ply.lex as lex
from ply.lex import TOKEN
import re
import codecs
import os
import sys

# List of token names.   This is always required
tokens = (
    'IN',
    'BOOL',
    'NUMBER',
    'PLUS',
    'MINUS',
    'NEGATIVE',
    'TIMES',
    'POWER',
    'DIVIDE',
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
    'RESERVED',
    'VAR',
    'SEMICOLON',
    'CCODE',
    'FUNCTION',
    'TRUE',
    'FALSE',
)

reserved = {
    "set": "SET",
    "abanico": "ABANICO",
    "vertical": "VERTICAL",
    "percutor": "PERCUTOR",
    "golpe": "GOLPE",
    "vibrato": "VIBRATO",
    "metronomo": "METRONOMO",
    "if": "IF",
    "else": "ELSE",
    "while": "WHILE",
    "for": "FOR",
    "enCaso": "ENCASO",
    "entons": "ENTONS",
    "cuando": "CUANDO",
    "siNo": "SINO",
    "finEnCaso": "FINENCASO",
    "def": "DEF",
    "exec": "EXEC",
}

tokens = tokens + tuple(reserved.values())

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_NEGATIVE = r'-'
t_POWER = r'\*\*'
t_TIMES = r'\*'
t_DIVIDE = r'/'
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
t_ccode_ignore = " \t\n"
t_TRUE = r'.t'
T_FALSE = r'.f'

# Declare the state
states = (
    ('ccode', 'inclusive'),
)

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_ccode_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def t_ccode_error(t):
    print("Illegal character in bracket '%s'" % t.value[0])
    t.lexer.skip(1)


# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_BOOL(t):
    r'(1+0)*(1+0)'
    t.value = int(t.value)
    return t


def t_COMMENT(t):
    r'\#.*'
    pass # No return value. Token discarded


def t_VAR(t):
    r'@[a-zA-Z_0-9?][a-zA-Z_0-9?]*'
    t.type = reserved.get(t.value, 'VAR')  # Check for reserved words
    return t


def t_RESERVED(t):
    r'[a-zA-Z_0-9?][a-zA-Z_0-9?]*'
    if reserved.get(t.value):
        var = t.type == reserved.get(t.value, 'RESERVED')  # Check for reserved words
        return t
    else:
        print("Illegal character '%s'" % t.value)
        t.lexer.skip(1)

def t_FUNCTION(t):
    r'[a-zA-Z_0-9?][a-zA-Z_0-9?]*()'
    var = t.type == reserved.get(t.value, 'RESERVED')  # Check for reserved words
    return t



# Match the first {. Enter ccode state.
def t_ccode(t):
    r'\{'
    t.lexer.code_start = t.lexer.lexpos  # Record the starting position
    t.lexer.level = 1  # Initial brace level
    t.lexer.begin('ccode')  # Enter 'ccode' state


# Rules for the ccode state
def t_ccode_lbrace(t):
    r'\{'
    t.lexer.level += 1


def t_ccode_rbrace(t):
    r'\};'
    t.lexer.level -= 1

    # If closing brace, return the code fragment
    if t.lexer.level == 0:
        t.value = t.lexer.lexdata[t.lexer.code_start:t.lexer.lexpos + 1]
        t.type = "CCODE"
        t.lexer.lineno += t.value.count('\n')
        t.lexer.begin('INITIAL')
        return t


def find_doc(direc):
    global files
    docs = []
    doc_number = ''
    result = False
    cont = 1

    for base, dirs, files in os.walk(direc):
        docs.append(files)

    for file in files:
        print(str(cont) + ". " + file)
        cont = cont + 1

    while not result:
        doc_number = input('\nChoose which file to execute: ')  # Choose which file to execute
        for file in files:
            if file == files[int(doc_number) - 1]:
                result = True
                break

        print("Executing \"%s\" \n" % files[int(doc_number) - 1])

    return files[int(doc_number) - 1]


directory = "./test/"
document = find_doc(directory)
test = directory + document
fp = codecs.open(test, 'r', None, 'strict', - 1)
# fp = codecs.open(test, "r", "utf-8")
arr = fp.read()
fp.close()

lexer = lex.lex()
lexer.input(arr)

while True:
    token = lexer.token()
    if not token:
        break
    print(token)
