from sympy import symbols


class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self.parent = None
    
    def get(self, name):
        value = self.symbols.get(name, None)
        if value == None and self.parent:
            return self.parent(name) 
        else:
            return value

    def set(self, name, value):
        self.symbols[name] = value
    
    def remove(self, name):
        del symbols [name]