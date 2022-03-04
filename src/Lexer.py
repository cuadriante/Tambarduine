import ply.lex as lex
import re
import codecs
import os
import sys

tokens = [
    'BOOL', 'NUMBER', 'AT', 'ASSIGN',
    'PLUS', 'MINUS', 'NEGATIVE', 'TIMES',
    'POWER', 'DIVIDE', 'WHOLEDIVIDE', 'MODULE',
    'LPAREN', 'RPAREN', 'ID', 'COMMENT', 'TRUE', 'FALSE',
]

reserved = {
    "set": "SET",
    "abanico": "ABANICO",
    "vertical": "VERTICAL",
    "percutor": "PERCUTOR",
    "golpe": "GOLPE",
    "vibrato": "VIBRATO",
    "metronomo": "METRONOMO",
    "print!": "PRINT!",
    "if": "IF",
    "else": "ELSE",
    "while": "WHILE",
    "for": "FOR",
}

tokens = tokens + list(reserved.values())

t_PLUS = r'\+'
t_ASSIGN = r','
t_MINUS = r'-'
t_NEGATIVE = r'-'
t_TIMES = r'\*'
t_POWER = r'\*\*'
t_DIVIDE = r'/'
t_WHOLEDIVIDE = r'//'
t_MODULE = r'%'
t_LPAREN = r'\('
t_RPAREN = r'\)'

t_ignore = ' \t'


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_ID(t):
    r'@[a-zA-Z_0-9?]^3[a-zA-Z_0-9?]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
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
        doc_number = input('\nInstructions: ')  # Choose which file to execute
        for file in files:
            if file == files[int(doc_number) - 1]:
                result = True
                break

    print("Executing \"%s\" \n") % files[int(doc_number) - 1]

    return files[int(doc_number) - 1]


directory = "./test"
document = find_doc(directory)
test = directory + document
fp = codecs.open(test, "r", "utf-8")
arr = fp.read()
fp.close()

lexer = lex.lex()
lexer.input(arr)

while True:
    token = lexer.token()
    if not token:
        break
    print(token)

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
