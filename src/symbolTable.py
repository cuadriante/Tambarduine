

class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self.lineno = {}
        self.child_table = None

    def get(self, name):
        value = self.symbols.get(name, None)
        if value == None and self.child_table:
            return self.child_table.get(name)
        elif value == None and self.child_table == None:
            return None
        else:
            return value
    
    def is_in(self, name):
        if name in self.symbols:
            return True
        else:
            return False
    
    def set_lineno(self, name, lineno):
        self.lineno[name] = lineno       

    def get_lineno(self, name):
        return self.lineno[name]

    def get_all(self):
        return (
            list(self.symbols.keys()),
            list(self.symbols.values())
        )

    def set_child_table(self, symbol_table):
        self.child_table = symbol_table

    def set(self, name, value):
        self.symbols[name] = value

    def remove(self, name):
        del self.symbols[name] 

    def change_value(self, name, new_value):
        # if self.symbols[name]:
        #     self.symbols[name] = new_value
        # else:
        #     print("No existe esa variable")
        self.symbols[name] = new_value

    def print(self):
        print("Principal :" )
        print( self.symbols)
        if self.child_table:
            print("Secundario: ")
            print(self.child_table.symbols)
    
    def delete_child_table(self):
        self.child_table.clear_table()
    
    def clear_table(self):
        self.symbols = {}

symbol_table = SymbolTable()
