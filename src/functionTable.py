from symbolTable import SymbolTable
from symbolTable import symbol_table


class FunctionTable:
    def __init__(self):
        self.declared_functions = {}
        self.called_functions = []

    def add(self, id, params):
        symbol_table.remove(id)
        for param in params.get_param_ids():
            symbol_table.remove(param)

        self.declared_functions[id] = params

    def get(self, id):
        value = self.declared_functions.get(id)
        if value == None:
            raise Exception(
                "No existe una variable con el identificador " + id)
        else:
            return value

    def call(self, id, params):
        symbol_table.remove(id)

        params = params.get_params()
        function_decl_params = self.declared_functions.get(id)

        function_decl_param_ids = function_decl_params.get_param_ids()
        function_symbol_table = SymbolTable()

        for i in range(len(function_decl_param_ids)):
            param_id = function_decl_param_ids[i]
            function_symbol_table.set(param_id, params[i])

        self.called_functions.append({id: function_symbol_table})

    def print_declared_functions(self):
        function_keys = self.declared_functions.keys()
        print('--------------------------------------------------')
        for key in function_keys:
            print('funcion declarada: ' + key)
            print('parametros:')
            function_decl_params = self.declared_functions.get(key)
            function_param_ids = function_decl_params.get_param_ids()
            print(function_param_ids)
            print('--------------------------------------------------')

    def print_called_functions(self):

        print('--------------------------------------------------')
        for function in self.called_functions:
            function_keys = function.keys()
            for key in function_keys:
                print('funcion llamada: ' + key)
                print('parametros:')
                function_symbol_table = function.get(key)
                function_symbols = function_symbol_table.get_all()
                for symbol in function_symbols:
                    print(symbol)
            print('--------------------------------------------------')


function_table = FunctionTable()
