from parser import *
from lexer import *

"""-----> Los archivos de prueba se ponen en la carpeta test y se llama a la funcion con el nombre del archivo <----- """

""" Llamar la funcion desde la raiz del proyecto """


def analizarCodigo(nombre_archivo):
    # READ FILE
    document_to_compile = "test/" + nombre_archivo
    test = document_to_compile
    fp = codecs.open(test, 'r', None, 'strict', - 1)
    arr = fp.read()
    fp.close()

    # LEXER - LEXICAL ANALYSIS
    lexer.input(arr)
    print_lexer(arr)

    # PARSER - SYNTACTIC ANALYSIS
    parser = yacc.yacc()
    print(parser.parse(arr))

    # SEMANTIC ANALYSIS


analizarCodigo('prueba_if_else.tam')
