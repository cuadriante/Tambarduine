class FunctionTable:
    def __init__(self):
        self.functions = {}

    def get(self, id):
        value = self.functions.get(id)
        if value == None:
            raise Exception(
                "No existe una variable con el identificador " + id)
        else:
            return value

    def add(self, id, params):
        self.functions[id] = params
        print(self.functions)


function_table = FunctionTable()
