import codecs
# from hardwareCommunication import *

from lexer import *
from parser import *
from errorChecker import *
from semanticAnalyzer import run_semantic_analysis

from hardwareCommunication import *

parser = yacc.yacc()
error_output = None


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
    program.print()


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

    lexer_error_result = get_lexer_error()
    print("LEXER ERROR: " + str(lexer_error_result))

    # PARSER - SYNTACTIC ANALYSIS
    # El parser tiene que generar la tabla de simbolos para que el semantico sirva <------------
    program = parser.parse(arr)
    # print_arbol(program)

    lexer_error_result = get_lexer_error()
    print("LEXER ERROR: " + str(lexer_error_result))

    parser_error_result = get_parser_error()
    print("PARSER ERROR: " + str(parser_error_result))

    directives = program.exec()

    run_error_checker(program)

    semantic_error_result = eg.get_error()

    # print(directives)
    run_directives(directives)

    print("SEMANTIC ERROR: " + str(semantic_error_result))

    # error_output = run_error_checker(program)

    # SEMANTIC ANALYSIS
    # run_semantic_analysis(arr)


def run_directives(directives):
    if (error_output != None):
        return

    for directive in directives:
        if directive[0] == "abanico":
            print("entró Abanico")
            direction = directive[1]
            if direction == '"A"':
                print("abaniqueoA")
                abanicoA()
            elif direction == '"B"':
                abanicoB()
        elif directive[0] == "vertical":
            direction = directive[1]
            if direction == '"D"':
                print("Vertical D")
                verticalD()
            elif direction == '"I"':
                verticalI()
        elif directive[0] == "percutor":
            if direction == '"D"':
                print("percutor D")
                percutorD()
            elif direction == '"I"':
                percutorI()
            elif direction == '"DI"':
                percutorDI()
            elif direction == '"A"':
                percutorA()
            elif direction == '"B"':
                percutorB()
            elif direction == '"AB"':
                percutorAB()
        elif directive[0] == "golpe":
            print("golpe")
            golpe()
        elif directive[0] == "vibrato":
            cantidad = int(directive[1])
            print("vibrato", cantidad)
            vibrato_vertical(cantidad)
        elif directive[0] == "metronomo":
            activate = directive[1]
            if activate == '"D"':
                cantidad = 0
            elif activate == '"A"':
                cantidad = directive[2]
            print("metronomo", activate, cantidad)
            set_metronomo(cantidad)
        elif directive[0] == "print":
            # print("printeo")
            params = directive[1]
            text = "print( "
            for param in params:
                if not isinstance(param, str):
                    param = str(param)
                    text += param
                else:
                    text += param
                text += " "
            text += ")"
            print(text)
            # self.__text.insert("1.0", text)
        enviar_instrucciones()


# analizeCode("hola.tam") ### NO DA ERRORES ###
analizeCode("prueba_bool_statements.tam") ### NO DA ERRORES ###
# analizeCode('prueba_def.tam')
# analizeCode("prueba_en_caso.tam")
# analizeCode("prueba_for_loop.tam")
# analizeCode("prueba_funciones.tam")
# analizeCode("prueba_if_else.tam")
# analizarCodigo('prueba_semantico.tam')
# analizeCode('prueba_SET.tam')
# analizeCode('uwu.tam')


# analizeCode("prueba_for_loop.tam")

# print(symbol_table.symbols)
# analizeCode("prueba_def.tam")


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
