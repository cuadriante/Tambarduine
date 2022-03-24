from symbolTable import SymbolTable
from symbolTable import symbol_table


class FunctionTable:
    def __init__(self):
        self.declared_functions = {}
        self.called_functions = []

    def add(self, id, params):
        # symbol_table.remove(id)
        # for param in params.get_param_ids():
        #     if param != None:
        #         symbol_table.remove(param)

        self.declared_functions[id] = [params, None]

    def get(self, id):
        value = self.declared_functions.get(id)
        if value == None:
            raise Exception(
                "No existe una variable con el identificador " + id)
        else:
            return value

    def call(self, id, params):
        # symbol_table.remove(id)

        params = params.get_params()
        function_decl_params = self.declared_functions.get(id)[0]

        function_decl_param_ids = function_decl_params.get_param_ids()
        function_symbol_table = SymbolTable()

        for i in range(len(function_decl_param_ids)):
            param_id = function_decl_param_ids[i]
            function_symbol_table.set(param_id, params[i])

        self.called_functions.append({id: function_symbol_table})

    def declare_new_variables(self, id, var_decls):
        self.declared_functions.get(id)[1] = var_decls

    def print_declared_functions(self):
        function_keys = self.declared_functions.keys()
        function_values = self.declared_functions.values()

        if function_keys != None and function_values != None:
            print('--------------------------------------------------')
            for key in function_keys:
                print('funcion declarada: ' + key)
                print('parametros:')
                function_decl_params = self.declared_functions.get(key)[0]
                function_param_ids = function_decl_params.get_param_ids()
                print(function_param_ids)
                print('declaraciones:')
                function_decl_variables = self.declared_functions.get(key)[1]
                if function_decl_variables != None:
                    for var_decl in function_decl_variables:
                        print(var_decl.var_name + ": " +
                              str(var_decl.expression.get_child()))
                print('--------------------------------------------------')

    def print_called_functions(self):
        print('--------------------------------------------------')
        for function in self.called_functions:
            function_keys = function.keys()
            for key in function_keys:
                print('funcion llamada: ' + key)
                print('variables locales:')
                function_symbol_table = function.get(key)
                function_symbols = function_symbol_table.get_all()
                symbol_keys = function_symbols[0]
                symbol_values = function_symbols[1]
                for i in range(len(symbol_keys)):
                    print(str(symbol_keys[i]) + ": " + str(symbol_values[i]))
            print('--------------------------------------------------')


function_table = FunctionTable()
