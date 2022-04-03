import codecs
from ctypes import get_last_error
# from hardwareCommunication import *

from lexer import *
from parser import *
from errorChecker import *
# from combinerClass import *
from semanticAnalyzer import run_semantic_analysis

from hardwareCommunication import *
parser = yacc.yacc()


class Compiler:
    def __init__(self, nombre_archivo):
        # self.nombre_archivo = nombre_archivo
        self.nombre_archivo = "./test/" + nombre_archivo  # no borren esto o me enojo
        self.thereWasAnError = False
        self.error = ''
        self.directives = []
        self.program = None

    """-----> Los archivos de prueba se ponen en la carpeta test y se llama a la funcion con el nombre del archivo <-----"""
    """-----> Correr el programa desde la raiz del proyecto <-----"""

    def compile(self):
        document_to_compile = self.nombre_archivo
        test = document_to_compile
        fp = codecs.open(test, 'r', None, 'strict', - 1)
        arr = fp.read()
        fp.close()

        lexer.input(arr)
        # self.print_lexer()

        self.program = parser.parse(arr)

        if self.program:
            eg.set_error()
            run_error_checker(self.program)
            self.error = eg.get_error()
            # print("Inicia error: ################\n" + self.error + "\nTermina error ##############")
            self.print_arbol()

        if not self.thereWasAnError and not error:
            self.directives = self.program.exec()
            return None

        else:
            return self.send_error()

    def print_lexer(self):
        print("--------LISTA DE TOKENS-------")
        while True:
            token = lexer.token()
            if not token:
                break
            print(token)
        print("------------------------------")

    def exec(self):
        self.run_directives()

    def compile_exec(self):
        self.compile()
        self.exec()
    
    def check_for_errors(self):
        parser_error = get_parser_error()
        lexer_error = get_lexer_error()
        if parser_error == True:
            self.thereWasAnError = True
        elif lexer_error == True:
            self.thereWasAnError = True
        

    def run_directives(self):
        for directive in self.directives:
            if directive[0] == "abanico":
                direction = directive[1]
                if direction == '"A"':
                    abanicoA()
                elif direction == '"B"':
                    abanicoB()
            elif directive[0] == "vertical":
                direction = directive[1]
                if direction == '"D"':
                    verticalD()
                elif direction == '"I"':
                    verticalI()
            elif directive[0] == "percutor":
                if direction == '"D"':
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
                golpe()
            elif directive[0] == "vibrato":
                cantidad = int(directive[1])
                vibrato_vertical(cantidad)
            elif directive[0] == "metronomo":
                activate = directive[1]
                if activate == '"D"':
                    cantidad = 0
                elif activate == '"A"':
                    cantidad = directive[2]
                set_metronomo(cantidad)
            elif directive[0] == "print":
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
                # self.__text.insert("1.0", text)
            enviar_instrucciones()

    def set_nombre_archivo(self, nombre):
        self.nombre_archivo = nombre

    def print_arbol(self):
        print("-----------Arbol------------")
        if self.program:
            self.program.print()

    def send_error(self):
        # print("Errores: " + self.error)
        return self.error

    def print_directives(self):
        print(self.directives)


# archivo = "hola.tam" ### FUNCIONA BIEN ###
# archivo = "prueba_bool_statements.tam" ### FUNCIONA BIEN ###
# archivo = 'prueba_def.tam'
# archivo = "prueba_en_caso.tam"  ### FUNCIONA BIEN ###
# archivo = "prueba_for_loop.tam" ### FUNCIONA BIEN ###
# archivo = "prueba_funciones.tam"
# archivo = "prueba_if_else.tam" ### FUNCIONA BIEN !! da error  de mismatch si se asigna la variable en if y else con tipos diferentes
# archivo = 'prueba_SET.tam' ###da error sintactico
# archivo = 'uwu.tam' ### FUNCIONA BIEN !! no se puede asignar una variable a otra variable

# c = Compiler(archivo)  # no me lo borren por fis
# c.compile()  # tampoco este
