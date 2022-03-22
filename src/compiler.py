
import codecs

from parser import *
from lexer import *
from semanticAnalyzer import run_semantic_analysis


parser = yacc.yacc()


def print_lexer():
    print("--------LISTA DE TOKENS-------")
    while True:
        token = lexer.token()
        if not token:
            break
        print(token)
    print("------------------------------")


"""-----> Los archivos de prueba se ponen en la carpeta test y se llama a la funcion con el nombre del archivo <-----"""

"""-----> Correr el programa desde la raiz del proyecto <-----"""


def analizarCodigo(nombre_archivo):
    # READ FILE
    document_to_compile = nombre_archivo
    test = document_to_compile
    fp = codecs.open(test, 'r', None, 'strict', - 1)
    arr = fp.read()
    fp.close()

    # LEXER - LEXICAL ANALYSIS
    lexer.input(arr)
    print_lexer()

    # PARSER - SYNTACTIC ANALYSIS
    # El parser tiene que generar la tabla de simbolos para que el semantico sirva <------------
    parser.parse(arr)

    # SEMANTIC ANALYSIS
    # run_semantic_analysis(arr)


# analizarCodigo('prueba_if_else.tam')
# analizarCodigo('prueba_declaraciones.tam')
# analizarCodigo('prueba_semantico.tam')
# analizarCodigo("prueba_for_loop.tam")
analizarCodigo("hola.tam")
print(symbol_table.symbols)