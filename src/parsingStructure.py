
from symbolTable import symbol_table

indentation = "   "
directives = []

class factor():
    def __init__(self, factor):
        self.factor = factor

    def printear(self, level):
        valor = str(self.factor)
        print(indentation * level + "Factor:")
        level += 1
        print(indentation*level + valor)

    def exec(self):
        factor = self.factor
        if isinstance(factor, int):
            return self.factor
        else:
            return symbol_table.get(self.factor)

    def get_child(self):
        return self.factor


class term():
    operator = None
    arith_expr = None

    def __init__(self, factor, term=None, operator=None):
        if term and operator:
            self.term = term
            self.operator = operator
        self.factor = factor

    def printear(self, level):
        print(indentation * level + "Term:")
        level += 1
        if hasattr(self, "term") and hasattr(self, "operator"):
            self.term.printear(level)
            print(indentation * level + self.operator)
        self.factor.printear(level)

    def exec(self):
        factor = self.factor.exec()
        result = 0
        if hasattr(self, "term") and hasattr(self, "operator"):
            term = self.term.exec()
            operator = self.operator
            if operator == "*":
                result = term * factor
            elif operator == "/":
                result = term / factor
            elif operator == "//":
                result = term // factor
            elif operator == "%":
                result = term % factor
            elif operator == "**":
                result = term ** factor
        else:
            result = factor
        return result
        # Buscar en la tabla de symbolos

    def get_child(self):
        if isinstance(self.factor, str) or isinstance(self.factor, bool):
            return self.factor
        else:
            return self.factor.get_child()


class arith_expr():
    factor = None
    operator = None
    def __init__(self, term, arith_expr=None, operator=None):
        if arith_expr and operator:
            self.arith_expr = arith_expr
            self.operator = operator
        self.term = term

    def printear(self, level):
        if arith_expr == None:
            print("xd")
        else:
            print(indentation * level + "Arith_expr:")
            level += 1
            if hasattr(self, "arith_expr") and hasattr(self, "operator"):
                self.arith_expr.printear(level)
                print(indentation * level + self.operator)
            self.term.printear(level)

    def exec(self):
        term = self.term.exec()
        result = 0
        if hasattr(self, "arith_expr") and hasattr(self, "operator"):
            arith_expr = self.arith_expr.exec()
            operator = self.operator

            if operator == "+":
                result = arith_expr + term
            elif operator == "-":
                result = arith_expr - term
        else:
            result = term
        return result

    def get_child(self):
        if isinstance(self.term, str) or isinstance(self.term, bool):
            return self.term
        else:
            return self.term.get_child()


class expression():
    arith_expr = None
    def __init__(self, arith_expr_or_bool):
        # print("Aqui", arith_expr_or_bool)
        if isinstance(arith_expr_or_bool, str):
            if (arith_expr_or_bool == "true" or "True"):
                self.arith_expr_or_bool = True
            elif (arith_expr_or_bool == "false" or "False"):
                self.arith_expr_or_bool = False
            else:
                pass
                # ERROR, NO DEBE LLEGAR UN STRING QUE NO SEA TRUE OR FALSE
        else:
            self.arith_expr_or_bool = arith_expr_or_bool
        # print("Then", self.arith_expr_or_bool)

    def printear(self, level):
        print(indentation*level + "Expression:")
        level += 1
        if self.isBool():
            print(indentation*level + str(self.arith_expr_or_bool))
        else:
            self.arith_expr_or_bool.printear(level)

    def exec(self):
        if self.isBool():
            return self.arith_expr_or_bool
        else:
            expression = self.arith_expr_or_bool.exec()
        return expression

    def isBool(self):
        return isinstance(self.arith_expr_or_bool, bool)

    def get_child(self):
        if isinstance(self.arith_expr_or_bool, str) or isinstance(self.arith_expr_or_bool, bool):
            return self.arith_expr_or_bool
        else:
            return self.arith_expr_or_bool.get_child()


class param():
    def __init__(self, expr_or_string):
        # print(expr_or_string)
        self.param_list = [expr_or_string]
        # print(self.param_list)

    def add(self, next_param):
        self.param_list.append(next_param)

    def printear(self, level):
        # print(self.param_list)
        for param in self.param_list:
            if self.isString(param):
                print(indentation*level + param)
            else:
                param.printear(level)

    def isString(self, param):
        return isinstance(param, str)

    def exec(self):
        param_list = []
        for param in self.param_list:
            if self.isString(param):
                param_list.append(param)
            else:
                expression = param.exec()
                param_list.append(expression)
        return param_list

    def get_params(self):
        result_params = []
        for param in self.param_list:
            if isinstance(param, str):
                result_params.append(param)
            else:
                result_params.append(param.get_child())
        return result_params

    def get_child(self):
        param = self.param_list[0]
        if isinstance(param, str) or isinstance(param, bool):
            return param
        else:
            return param.get_child()


class semi_condition():
    def __init__(self, comparator, expression):
        self.comparator = comparator
        self.expression = expression

    def printear(self, level):
        print(indentation*level + "Semi_condition:")
        level += 1
        print(indentation*level + self.comparator)
        self.expression.printear(level)

    def exec(self):
        expression = self.expression.exec()
        comparator = self.comparator

        return (comparator, expression)


class condition():
    def __init__(self, arith_expr, semi_condition):
        self.arith_expr = arith_expr
        self.semi_condition = semi_condition

    def printear(self, level):
        print(indentation*level + "Condition:")
        level += 1
        self.arith_expr.printear(level)
        self.semi_condition.printear(level)

    def exec(self):
        result = None
        elemento0 = self.arith_expr.exec()
        com_and_elem = self.semi_condition.exec()
        comparator = com_and_elem[0]
        elemento1 = com_and_elem[1]

        if comparator == "==":
            result = elemento0 == elemento1
        elif comparator == "<":
            result = elemento0 < elemento1
        elif comparator == ">":
            result = elemento0 > elemento1
        elif comparator == "<=":
            result = elemento0 <= elemento1
        elif comparator == ">=":
            result = elemento0 >= elemento1
        elif comparator == "<>":
            result = elemento0 != elemento1

        return result


class var_decl():
    condition = None
    step = None
    switch_list = None


    def __init__(self, var_name, expression):
        self.var_name = var_name
        self.expression = expression

    def printear(self, level):
        level += 1
        print(indentation * level + "Var_decl:")
        level += 1
        print(indentation * level + self.var_name)
        self.expression.printear(level)

    def exec(self):
        valor = self.expression.exec()
        symbol_table.set(self.var_name, valor)
    


class function_call():
    def __init__(self, function_name, params):
        self.function_name = function_name
        self.params = params


class bool_statement():
    def __init__(self, var_name, bool_function):
        self.var_name = var_name
        self.bool_function = bool_function

    def printear(self, level):
        level += 1
        print(indentation*level + "Bool_statement:")
        level += 1
        print(indentation*level + self.var_name)
        print(indentation*level + self.bool_function)

    def exec(self):
        function = self.bool_function
        var_name = self.var_name
        if function == ".Neg":
            var_value = symbol_table.get(self.var_name)
            symbol_table.change_value(var_name, not var_value)
        elif function == ".T":
            symbol_table.change_value(var_name, True)
        elif function == ".F":
            symbol_table.change_value(var_name, False)


class if_statement():
    expression = None
    var_decl = None
    var_name = None
    statements1 = None
    statements2 = None
    step = None
    switch_list = None

    def __init__(self, condition, statements1, statements2=None):
        self.condition = condition
        self.statements1 = statements1
        if statements2:
            self.statements2 = statements2

    def printear(self, level):
        level+=1
        print(indentation*level + "If_statement:")
        level += 1
        print(indentation*level + "If_statement:")
        level += 1
        self.condition.printear(level)
        self.statements1.printear(level)

        if self.statements2 and self.hasElse():
            self.statements2.printear(level)

    def hasElse(self):
        return hasattr(self, "statements2")

    def exec(self):
        condition = self.condition.exec()
        if condition:
            self.statements1.exec()
        if self.hasElse() and self.statements2 and not condition:
            self.statements2.exec()


class for_loop():
    condition = None
    expression = None
    switch_list = None

    def __init__(self, var_name, to_factor, statements, step_number=None, ):
        self.var_name = var_name
        self.to = to_factor
        self.statements = statements
        if step_number:
            self.step = step_number

    def printear(self, level):
        level += 1
        print(indentation*level + "For_loop:")
        level += 1
        print(indentation*level + self.var_name)
        self.to.printear(level)
        if self.hasStep():
            print(indentation*level + "Step " + str(self.step))
        self.statements.printear(level)

    def hasStep(self):
        return hasattr(self, "step")

    def exec(self):
        if not symbol_table.get(self.var_name):
            symbol_table.add(self.var_name, 1)
        var_value = symbol_table.get(self.var_name)
        to = self.to.exec()
        step = 1
        if self.hasStep():
            step = self.step
        while var_value < to:
            self.statements.exec()
            var_value += step  # FALTA QUE EL BICHO RECONOZCA SI EL FOR SE RECORRE HASTA EL INFINITO


class en_caso():
    step = None
    condition = None
    var_name = None
    def __init__(self, switch_list, sino_statements, expression=None):
        self.switch_list = switch_list
        self.sino = sino_statements
        if expression:
            self.expression = expression

    def printear(self, level):
        print(indentation*level + "En_caso:")
        level += 1
        if self.hasExpression():
            self.expression.printear(level)
        self.switch_list.printear(level)
        print(indentation*level + "Si_no:")
        level += 1
        self.sino.printear(level)

    def hasExpression(self):
        return hasattr(self, "expression")


    def exec(self):
        useSino = None
        if self.hasExpression():
            useSiNo = self.switch_list.exec(self.expression)
        else:
            useSiNo = self.switch_list.exec()
        if useSiNo:
            self.sino.exec()




class switch0():
    def __init__(self, condition, statements):
        self.condition = condition
        self.statements = statements

    def printear(self, level):
        print(indentation*level + "Switch0:")
        level += 1
        self.condition.printear(level)
        self.statements.printear(level)

    def exec(self):
        condition = self.condition.exec()
        useSiNo = None
        if condition:
            self.statements.exec()
            useSiNo = False
        else:
            useSiNo = True
        print(useSiNo)
        return useSiNo


class switch_list0():
    def __init__(self, switch0):
        self.switch_list = [switch0]

    def add(self, next_switch):
        self.switch_list.append(next_switch)

    def printear(self, level):
        print(indentation*level + "Switch_list0:")
        level += 1
        for switch in self.switch_list:
            switch.printear(level)

    def exec(self):
        useSiNo = True
        for switch in self.switch_list:
            bool_value = switch.exec()
            if not bool_value:
                useSiNo = False
        return useSiNo


class switch1():
    def __init__(self, semi_condition, statements):
        self.semi_condition = semi_condition
        self.statements = statements

    def printear(self, level):
        print(indentation*level + "Switch1:")
        level += 1
        self.semi_condition.printear(level)
        self.statements.printear(level)

    def exec(self, expression):
        """LAS CONDITION NO RECIBEN BOOLS COMO PRIMER ELEMENTO"""
        com_and_elem = self.semi_condition.exec()
        comparator = com_and_elem[0]
        elemento1 = com_and_elem[1]
        print(expression)
        elemento0 = expression.exec()
        print(elemento0, comparator, elemento1)
        if comparator == "==":
            result = elemento0 == elemento1
        elif comparator == "<":
            result = elemento0 < elemento1
        elif comparator == ">":
            result = elemento0 > elemento1
        elif comparator == "<=":
            result = elemento0 <= elemento1
        elif comparator == ">=":
            result = elemento0 >= elemento1
        elif comparator == "<>":
            result = elemento0 != elemento1

        useSiNo = None
        if result:
            self.statements.exec()
            useSiNo = False
        else:
            useSiNo = True
        return useSiNo

class switch_list1():
    def __init__(self, switch1):
        self.switch_list = [switch1]

    def add(self, next_switch):
        self.switch_list.append(next_switch)

    def printear(self, level):
        print(indentation*level + "Switch_list1:")
        level += 1
        for switch in self.switch_list:
            switch.printear(level)


    def exec(self, expression):
        useSiNo = True
        for switch in self.switch_list:
            bool_value = switch.exec(expression)
            if not bool_value:
                useSiNo = False
        return useSiNo


class statement():
    expression = None

    def __init__(self, statement):
        self.statement_list = [statement]

    def add(self, next_statement):
        self.statement_list.append(next_statement)

    def printear(self, level):
        print(indentation * level + "Statements:")
        for statement in self.statement_list:
            statement.printear(level)

    def exec(self):
        for statement in self.statement_list:
            statement.exec()


class callable_function():
    def __init__(self, function):
        self.function = function

    def printear(self, level):
        level += 1
        self.function.printear(level)

    def exec(self):
        self.function.exec()


class printer():
    def __init__(self, params):
        self.params = params

    def printear(self, level):
        print(indentation*level + "Printer:")
        level += 1
        self.params.printear(level)

    # DEBE DE GUARDAR EL PRINT Y EJECUTARSE JUNTO CON LAS FUNCIONES BUILD-IN
    def exec(self):
        param_list = self.params.exec()
        print(param_list)
        directives.append(("print", param_list))


class abanico():
    def __init__(self, param):
        self.param = param

    def printear(self, level):
        print(indentation*level + "Abanico:")
        level += 1
        self.param.printear(level)

    def exec(self):
        params = self.param.exec()
        function = "abanico"
        direction = params[0]
        directives.append((function, direction))





class vertical():
    def __init__(self, param):
        self.param = param

    def printear(self, level):
        print(indentation*level + "Vertical:")
        level += 1
        self.param.printear(level)

    def exec(self):
        params = self.param.exec()
        function = "vertical"
        direction = params[0]
        directives.append((function, direction))



class percutor():
    def __init__(self, param):
        self.param = param

    def printear(self, level):
        print(indentation*level + "Percutor:")
        level += 1
        self.param.printear(level)

    def exec(self):
        params = self.param.exec()
        function = "percutor"
        direction = params[0]
        directives.append((function, direction))



class golpe():
    def __init__(self, param):
        self.param = param

    def printear(self, level):
        print(indentation*level + "Golpe:")


    def exec(self):
        function = "golpe"
        directives.append((function))



class vibrato():
    def __init__(self, param):
        self.param = param

    def printear(self, level):
        print(indentation*level + "Vibrato:")
        level += 1
        self.param.printear(level)

    def exec(self):
        params = self.param.exec()
        function = "vibrato"
        cantidad = params[0]
        directives.append((function, cantidad))


class metronomo():
    def __init__(self, param):
        self.param = param

    def printear(self, level):
        print(indentation*level + "Metronomo:")
        level += 1
        self.param.printear(level)

    def exec(self):
        parametros = self.param.exec()

    def exec(self):
        params = self.param.exec()
        function = "metronomo"
        on_off = params[0]
        time_range = params[1]
        directives.append((function, on_off, time_range))



class main():
    def __init__(self, statements):
        self.statements = statements

    def printear(self, level):
        print(indentation * level + "Main:")
        self.statements.printear(level + 1)

    def exec(self):
        self.statements.exec()


class block():
    def __init__(self, function_decls, main):
        self.function_decls = function_decls
        self.main = main

    def printear(self, level):
        print(indentation * level + "Block:")
        self.main.printear(level + 1)

    def exec(self):
        # self.function_decls.exec()
        self.main.exec()


class function_decl():
    def __init__(self, function_name, function_decl_params, statements):
        self.function_name = function_name
        self.function_decl_params = function_decl_params
        self.function_body = function_body

    def add(self, next_function_decls):
        super().add(next_function_decls)

    def get_next(self):
        return super().get_next()

class function_decls():
    def __init__(self, function_decl):
        self.function_decl_list = [function_decl]

    def add(self, function_decl):
        self.function_decl_list.append(function_decl)


class function_decls_param():
    def __init__(self, var_name):
        self.param_list = [var_name]

    def add(self, next_param):
        self.param_list.append(next_param.param_list[0])

    def get_param_ids(self):
        return self.param_list


class function_body():
    def __init__(self, statements):
        self.statements = statements

    def get_var_decls(self):
        result = []
        for i in range(len(self.statements.statement_list)):
            statement = self.statements.statement_list[i]

            if isinstance(statement, var_decl):
                result.append(statement)

        return result


class program():
    def __init__(self, block):
        self.block = block

    def printear(self):
        print("Program:")
        self.block.printear(2)

    def exec(self):
        self.block.exec()
        print(symbol_table.symbols)
        return directives

    def get_block(self):
        return self.block
