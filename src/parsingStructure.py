
from symbolTable import symbol_table
from functionTable import function_table

indentation = "   "
directives = []

class factor():
    def __init__(self, factor, lineno):
        self.lineno = lineno
        self.factor = factor

    def print(self, level):
        print(indentation * level + "Factor:")
        level += 1
        if self.isArithExpr():
            self.factor.print(level)
        else:
            valor = str(self.factor)
            print(indentation*level + valor)

    def exec(self):
        factor = self.factor
        if isinstance(factor, int):
            return self.factor
        elif self.isArithExpr():
            return self.factor.exec()
        else:
            return symbol_table.get(self.factor)

    def get_child(self):
        return self.factor
    
    def isArithExpr(self):
        return isinstance(self.factor, arith_expr)

class negative():
    def __init__(self, factor, line):
        self.factor = factor
        self.line = line


    def print(self, level):
        print(indentation * level + "NEGATIVE:")
        level += 1
        self.factor.print(level)
        # print(indentation * level + str(self.factor))
    
    def exec(self):
        #SI LA EXPRESIÓN ES BOOL DEBE MANDAR ERROR 
        factor = self.factor.exec()
        return - factor






class term():
    operator = None
    arith_expr = None

    def __init__(self, factor, term=None, operator=None):
        if term and operator:
            self.term = term
            self.operator = operator
        self.factor = factor

    def print(self, level):
        print(indentation * level + "Term:")
        level += 1
        if hasattr(self, "term") and hasattr(self, "operator"):
            self.term.print(level)
            print(indentation * level + self.operator)
        self.factor.print(level)

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

    def print(self, level):
        if arith_expr == None:
            print("xd")
        else:
            print(indentation * level + "Arith_expr:")
            level += 1
            if hasattr(self, "arith_expr") and hasattr(self, "operator"):
                self.arith_expr.print(level)
                print(indentation * level + self.operator)
            self.term.print(level)

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
            # print(arith_expr_or_bool == "False")
            if (arith_expr_or_bool == "True"):
                self.arith_expr_or_bool = True
            elif (arith_expr_or_bool == "False"):
                self.arith_expr_or_bool = False
            else:
                pass
                # ERROR, NO DEBE LLEGAR UN STRING QUE NO SEA TRUE OR FALSE
        else:
            self.arith_expr_or_bool = arith_expr_or_bool
        # print("Then", self.arith_expr_or_bool)

    def print(self, level):
        print(indentation*level + "Expression:")
        level += 1
        if self.isBool():
            print(indentation*level + str(self.arith_expr_or_bool))
        else:
            self.arith_expr_or_bool.print(level)

    def exec(self):
        if self.isBool():
            # print(self.arith_expr_or_bool)
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
        self.param_list.append(next_param.param_list[0])

    def print(self, level):
        # print(self.param_list)
        for param in self.param_list:
            if self.isString(param):
                print(indentation*level + param)
            else:
                param.print(level)

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
    def __init__(self, comparator, expression, line):
        self.line = line
        self.comparator = comparator
        self.expression = expression

    def print(self, level):
        print(indentation*level + "Semi_condition:")
        level += 1
        print(indentation*level + self.comparator)
        self.expression.print(level)

    def exec(self):
        expression = self.expression.exec()
        comparator = self.comparator

        return (comparator, expression)


class condition():
    def __init__(self, arith_expr, semi_condition, line):
        self.line = line
        self.arith_expr = arith_expr
        self.semi_condition = semi_condition

    def print(self, level):
        print(indentation*level + "Condition:")
        level += 1
        self.arith_expr.print(level)
        self.semi_condition.print(level)

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
    condition_or_expression = None
    step = None
    switch_list = None


    def __init__(self, var_name, expression, line):
        self.line = line
        self.var_name = var_name
        self.expression = expression

    def print(self, level):
        print(indentation * level + "Var_decl:")
        level += 1
        print(indentation * level + self.var_name)
        self.expression.print(level)

    def exec(self, function_symbol_table = None):
        valor = self.expression.exec()
        # print(valor)
        if function_symbol_table:
            function_symbol_table.set(self.var_name, valor)
        else:
            symbol_table.set(self.var_name, valor)



class bool_statement():
    def __init__(self, var_name, bool_function):
        self.var_name = var_name
        self.bool_function = bool_function

    def print(self, level):
        print(indentation*level + "Bool_statement:")
        level += 1
        print(indentation*level + self.var_name)
        print(indentation*level + self.bool_function)

    def exec(self, function_symbol_table = None):
        function = self.bool_function
        var_name = self.var_name
        value = None
        if function == ".Neg":
            if function_symbol_table:
                var_value = function_symbol_table.get(self.var_name)
            else:
                var_value = symbol_table.get(self.var_name)
            value = not var_value
        elif function == ".T":
            value = True
        elif function == ".F":
            value = False

        if function_symbol_table:
            function_symbol_table.change_value(var_name, value)
        else:
            symbol_table.change_value(var_name, value)


class if_statement():
    expression = None
    var_decl = None
    var_name = None
    statements1 = None
    statements2 = None
    step = None
    switch_list = None


    def __init__(self, condition_or_expression, statements1, statements2=None):
        self.condition_or_expression = condition_or_expression
        self.statements1 = statements1
        if statements2:
            self.statements2 = statements2

    def print(self, level):
        print(indentation*level + "If_statement:")
        level += 1
        self.condition_or_expression.print(level)
        self.statements1.print(level)

        if self.statements2 and self.hasElse():
            self.statements2.print(level)

    def hasElse(self):
        return hasattr(self, "statements2")

    def exec(self):
        condition_or_expression = self.condition_or_expression.exec()
        if condition_or_expression:
            self.statements1.exec()
        if self.hasElse() and self.statements2 and not condition_or_expression:
            self.statements2.exec()


class for_loop():
    condition_or_expression = None
    expression = None
    switch_list = None

    def __init__(self, var_name, to_factor, statements, step_number=None, ):
        self.var_name = var_name
        self.to = to_factor
        self.statements = statements
        if step_number:
            self.step = step_number

    def print(self, level):
        print(indentation*level + "For_loop:")
        level += 1
        print(indentation*level + self.var_name)
        self.to.print(level)
        if self.hasStep():
            print(indentation*level + "Step " + str(self.step))
        self.statements.print(level)

    def hasStep(self):
        return hasattr(self, "step")

    def exec(self):
        if not symbol_table.get(self.var_name):
            symbol_table.set(self.var_name, 1)
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

    def print(self, level):
        print(indentation*level + "En_caso:")
        level += 1
        if self.hasExpression():
            self.expression.print(level)
        self.switch_list.print(level)
        print(indentation*level + "Si_no:")
        level += 1
        self.sino.print(level)

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

    def print(self, level):
        print(indentation*level + "Switch0:")
        level += 1
        self.condition.print(level)
        self.statements.print(level)

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

    def print(self, level):
        print(indentation*level + "Switch_list0:")
        level += 1
        for switch in self.switch_list:
            switch.print(level)

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

    def print(self, level):
        print(indentation*level + "Switch1:")
        level += 1
        self.semi_condition.print(level)
        self.statements.print(level)

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

    def print(self, level):
        print(indentation*level + "Switch_list1:")
        level += 1
        for switch in self.switch_list:
            switch.print(level)


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

    def print(self, level):
        print(indentation * level + "Statements:")
        level += 1
        for statement in self.statement_list:
            statement.print(level)

    def exec(self, symbol_table = None):
        for statement in self.statement_list:
            if isinstance(statement, var_decl) or isinstance(statement, bool_statement):
                statement.exec(symbol_table)
            else:
                statement.exec()


class callable_function():
    def __init__(self, function):
        self.function = function

    def print(self, level):
        self.function.print(level)

    def exec(self):
        self.function.exec()


class printer():
    def __init__(self, params):
        self.params = params

    def print(self, level):
        print(indentation*level + "Printer:")
        level += 1
        self.params.print(level)

    # DEBE DE GUARDAR EL PRINT Y EJECUTARSE JUNTO CON LAS FUNCIONES BUILD-IN
    def exec(self):
        param_list = self.params.exec()
        directives.append(("print", param_list))


class abanico():
    def __init__(self, param):
        self.param = param

    def print(self, level):
        print(indentation*level + "Abanico:")
        level += 1
        self.param.print(level)

    def exec(self):
        params = self.param.exec()
        function = "abanico"
        direction = params[0]
        directives.append((function, direction))

class vertical():
    def __init__(self, param):
        self.param = param

    def print(self, level):
        print(indentation*level + "Vertical:")
        level += 1
        self.param.print(level)

    def exec(self):
        params = self.param.exec()
        function = "vertical"
        direction = params[0]
        directives.append((function, direction))



class percutor():
    def __init__(self, param):
        self.param = param

    def print(self, level):
        print(indentation*level + "Percutor:")
        level += 1
        self.param.print(level)

    def exec(self):
        params = self.param.exec()
        function = "percutor"
        direction = params[0]
        directives.append((function, direction))



class golpe():
    def __init__(self, param):
        self.param = param

    def print(self, level):
        print(indentation*level + "Golpe:")


    def exec(self):
        function = "golpe"
        directives.append((function, None))



class vibrato():
    def __init__(self, param):
        self.param = param

    def print(self, level):
        print(indentation*level + "Vibrato:")
        level += 1
        self.param.print(level)

    def exec(self):
        params = self.param.exec()
        function = "vibrato"
        cantidad = params[0]
        directives.append((function, cantidad))


class metronomo():
    def __init__(self, param):
        self.param = param

    def print(self, level):
        print(indentation*level + "Metronomo:")
        level += 1
        self.param.print(level)

    def exec(self):
        parametros = self.param.exec()

    def exec(self):
        params = self.param.exec()
        print(params)
        function = "metronomo"
        on_off = params[0]
        time_range = params[1]
        directives.append((function, on_off, time_range))



class main():
    def __init__(self, statements):
        self.statements = statements

    def print(self, level):
        print(indentation * level + "Main:")
        self.statements.print(level + 1)

    def exec(self):
        self.statements.exec()




class function_call():
    def __init__(self, function_name, params):
        self.function_name = function_name
        self.params = params

    def print(self, level):
        print(indentation * level + "Function_call:")
        level += 1
        print(indentation * level + self.function_name)

    def exec(self):
        #ERROR LA FUNCION NO EXISTE
        params = function_table.get_params(self.function_name)
        statements = function_table.get_body(self.function_name)
        attri = self.params.exec()
        print(params)

        function_symbol_table = function_table.get_symbol_table()
        symbol_table.set_child_table(function_symbol_table)

        for i in range(len(params)):
            function_symbol_table.set(params[i], attri[i])

        print(function_symbol_table.symbols)
        statements.exec(function_symbol_table)

        # symbol_table.print()

        #elimina tabla de la función
        function_table.delete_symbol_table()
        symbol_table.delete_child_table()

        # symbol_table.print()

class function_decl():
    def __init__(self, function_name, function_decl_params, statements):
        self.function_name = function_name
        self.function_decl_params = function_decl_params
        self.function_body = statements

    def print(self, level):
        print(indentation * level + "Function_decl:")
        level +=1
        print(indentation * level + self.function_name)
        self.function_decl_params.print(level)
        self.function_body.print(level)

    def exec(self):
        params = self.function_decl_params.exec()
        function_table.add(self.function_name, params, self.function_body)

        # function_table.add_function(self.function_name, self.function_decl_params.param_list)
        # function_table.print()
        # ERROR: EL BODY DE LA FUNCION NO DEBE ESTAR VACIO
        # function_table.declare_new_variables(self.function_name, self.function_body.get_var_decls())

class function_decls():
    def __init__(self, function_decl):
        self.function_decl_list = [function_decl]

    def add(self, function_decl):
        self.function_decl_list.append(function_decl)

    def print(self, level):
        # print(self.function_decl_list)
        print(indentation * level + "Function_decls:")
        level += 1
        for function_decl in self.function_decl_list:
            function_decl.print(level)

    def exec(self):
        for function_decl in self.function_decl_list:
            function_decl.exec()


class function_decls_param():
    def __init__(self, var_name):
        print(var_name)
        self.param_list = [var_name]

    def add(self, next_param):
        # print(next_param)
        self.param_list.append(next_param.param_list[0])

    def get_param_ids(self):
        return self.param_list

    def print(self, level):
        for param in self.param_list:
            print(indentation*level + param)

    def exec(self):
        param_list = []
        for param in self.param_list:
            param_list.append(param)
        return param_list

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

    def print(self, level):
        print(indentation * level + "Function_dody:")
        level += 1
        self.statements.print(level)

    def exec(self, function_symbol_table):
        self.statements.exec(function_symbol_table)

class block():
    def __init__(self, function_decls, main):
        self.function_decls = function_decls
        self.main = main

    def print(self, level):
        print(indentation * level + "Block:")
        level += 1
        if self.hasFunct():
            self.function_decls.print(level)
        self.main.print(level)

    def exec(self):
        if self.hasFunct():
            self.function_decls.exec()
        self.main.exec()

    def hasFunct(self):
        return self.function_decls.function_decl_list[0] != None

class program():
    def __init__(self, block):
        self.block = block

    def print(self):
        print("Program:")
        self.block.print(2)

    def exec(self):
        self.block.exec()
        symbol_table.print()
        return directives

    def get_block(self):
        return self.block
