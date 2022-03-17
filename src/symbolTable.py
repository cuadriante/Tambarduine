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
            raise Exception("No existe una variable con el nombre ingresado")
        else:
            return value

    def set(self, name, value):
        self.symbols[name] = value

    def remove(self, name):
        del symbols[name]

    def cambiar_valor(self, name, new_value):
        self.symbols[name] = new_value
