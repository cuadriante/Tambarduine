import codecs
import hardwareCommunication

from lexer import *
from parser import *
from errorChecker import *
from semanticAnalyzer import run_semantic_analysis

# from hardwareCommunication import *

parser = yacc.yacc()


def print_lexer():
    print("--------LISTA DE TOKENS-------")
    while True:
        token = lexer.token()
        if not token:
            break
        print(token)
    print("------------------------------")


def print_arbol(program):
    print("-----------Arbol------------")
    program.printear()


"""-----> Los archivos de prueba se ponen en la carpeta test y se llama a la funcion con el nombre del archivo <-----"""

"""-----> Correr el programa desde la raiz del proyecto <-----"""


def analizeCode(nombre_archivo):
    # READ FILE
    document_to_compile = 'test/' + nombre_archivo
    test = document_to_compile
    fp = codecs.open(test, 'r', None, 'strict', - 1)
    arr = fp.read()
    fp.close()

    # LEXER - LEXICAL ANALYSIS
    lexer.input(arr)
    # print_lexer()

    # PARSER - SYNTACTIC ANALYSIS
    # El parser tiene que generar la tabla de simbolos para que el semantico sirva <------------
    program = parser.parse(arr)
    print_arbol(program)
    directives = program.exec()
    # print(directives)

    # run_error_checker(program)

    # SEMANTIC ANALYSIS
    # run_semantic_analysis(arr)


# analizarCodigo('prueba_if_else.tam')
# analizeCode('prueba_def.tam')
# analizarCodigo('prueba_declaraciones.tam')
# analizarCodigo('prueba_semantico.tam')
# analizarCodigo("prueba_for_loop.tam")
# analizeCode("hola.tam")
# print(symbol_table.symbols)
# analizeCode("prueba_def.tam")
# analizeCode("prueba_en_caso")
# analizeCode("prueba_bool_statements.tam")

# Hardware
# hardwareCommunication.set_metronomo(0.75)

# hardwareCommunication.percutorA()
# hardwareCommunication.percutorD()
# hardwareCommunication.golpe()
# hardwareCommunication.percutorAB()
# hardwareCommunication.percutorB()
# hardwareCommunication.percutorI()
# hardwareCommunication.golpe()
# hardwareCommunication.percutorAB()
# hardwareCommunication.percutorDI()
# hardwareCommunication.set_metronomo(0.4)
# hardwareCommunication.percutorA()
# hardwareCommunication.percutorD()
# hardwareCommunication.golpe()
# hardwareCommunication.percutorDI()
# hardwareCommunication.golpe()
# hardwareCommunication.percutorB()
# hardwareCommunication.percutorI()
# hardwareCommunication.percutorAB()
# hardwareCommunication.percutorA()
# hardwareCommunication.golpe()
# hardwareCommunication.percutorD()
# hardwareCommunication.percutorB()
# hardwareCommunication.percutorI()
# hardwareCommunication.golpe()

# hardwareCommunication.enviar_instrucciones()
