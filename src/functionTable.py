from symbolTable import SymbolTable
from symbolTable import symbol_table


class FunctionTable:
    def __init__(self):
        self.declared_functions = {}
        self.called_functions = []
        self.symbol_table = SymbolTable()

    def add(self, id, params, body):
        self.declared_functions[id] = [params, body]
        # for param in params:
        #     self.symbol_table.set(param, None)
    
    def delete_symbol_table(self):
        self.symbol_table.clear_table()

    def get_symbol_table(self):
        return self.symbol_table

    """
    Retorna el nombre de los parametros
    """
    def get_params(self, id):
        params = self.declared_functions[id]
        params = params[0]
        # print(params)
        return params
    
    def get_body(self, id):
        body = self.declared_functions[id]
        body = body[1]
        return body

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
                    if isinstance(symbol_values[i], str) or isinstance(symbol_values[i], int) or isinstance(symbol_values[i], bool):
                        print(str(symbol_keys[i]) + ": " +
                            str(symbol_values[i]))
                    else:
                        print(str(symbol_keys[i]) + ": " +
                            str(symbol_values[i].get_child()))
            print('--------------------------------------------------')


function_table = FunctionTable()
