from logging import exception
from sympy import symbols


class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self.parent = None

    def get(self, name):
        value = self.symbols.get(name, None)
        if value == None and self.parent:
            return self.parent(name)
        elif value == None and self.parent == None:
            # raise Exception(
            #    "No existe una variable con el identificador " + name)
            return False
        else:
            return value

    def get_all(self):
        return self.symbols.values()

    def set(self, name, value):
        self.symbols[name] = value

    def remove(self, name):
        del self.symbols[name]

    def change_value(self, name, new_value):
        self.symbols[name] = new_value


# La tabla de simbolos es la misma para el parser y el semantico
symbol_table = SymbolTable()
