from symbolTable import SymbolTable


class FunctionTable:
    def __init__(self):
        self.functions = {}
        self.called_functions = []

    def get(self, id):
        value = self.functions.get(id)
        if value == None:
            raise Exception(
                "No existe una variable con el identificador " + id)
        else:
            return value

    def add(self, id, params):
        self.functions[id] = params

    def call(self, id, params):
        function_decl_params = self.functions.get(id)
        symbol_table = SymbolTable()
        for i in range(len(function_decl_params)):
            param_id = function_decl_params[i]
            symbol_table.set(param_id, params[i])

        self.called_functions.append({id: symbol_table})


function_table = FunctionTable()
