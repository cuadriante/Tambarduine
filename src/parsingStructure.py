
from ast import operator
from unittest import result
from matplotlib.pyplot import step, text
from symbolTable import symbol_table

identation = "   "


class Structure:
    pass


class factor():
    def __init__(self, factor):
        self.factor = factor

    def printear(self, level):
        valor = str(self.factor)
        print(identation*level + "Factor:")
        level += 1
        print(identation*level + valor)
    
    def exec(self):
        factor = self.factor
        if isinstance(factor, int):
            return self.factor
        else:
            pass
            #Buscar en la tabla de symbolos

class term(Structure):
    def __init__(self, factor, term=None, operator=None):
        if term and operator:
            self.term = term
            self.operator = operator
        self.factor = factor

    def printear(self, level):
        print(identation*level + "Term:")
        level +=1
        if hasattr(self, "term") and hasattr(self, "operator"):
            self.term.printear(level)
            print(identation*level + self.operator)
        self.factor.printear(level)
    
    def exec(self):
        factor = self.factor.exec()
        result = 0
        if hasattr(self, "term") and hasattr(self, "operator"):
            term = self.term.exec()
            operator = self.operator
            if operator == "*":
                result = term * factor
                print(term, factor, result)
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
            #Buscar en la tabla de symbolos

class arith_expr(Structure):
    def __init__(self, term, arith_expr=None, operator=None):
        if arith_expr and operator:
            self.arith_expr = arith_expr
            self.operator = operator
        self.term = term

    def printear(self, level):
        print(identation*level + "Arith_expr:")
        level +=1
        if hasattr(self, "arith_expr") and hasattr(self, "operator"):
            self.arith_expr.printear(level)
            print(identation*level + self.operator)
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

class expression(Structure):
    def __init__(self, arith_expr_or_bool):
        self.arith_expr_or_bool = arith_expr_or_bool
    
    def printear(self, level):
        print(identation*level + "Expression:" )
        self.arith_expr_or_bool.printear(level + 1)
    
    def exec(self):
        expression = self.arith_expr_or_bool.exec()
        return expression

class param():
    def __init__(self, expr_or_string):
        self.param_list = [expr_or_string]
    
    def add(self, next_param):
        self.param_list.append(next_param)
    



class semi_condition(Structure):
    def __init__(self, comparator, expression):
        self.comparator = comparator
        self.term = expression


class condition(Structure):
    def __init_(self, arith_expr, semi_condition):
        self.arith_expr = arith_expr
        self.semi_condition = semi_condition

class var_decl():
    def __init__(self, var_name, expression):
        self.var_name = var_name
        self.expression = expression

    def printear(self, level):
        level += 1
        print(identation*level + "Var_decl:")
        level += 1
        print(identation*level + self.var_name)
        self.expression.printear(level)
    
    def exec(self):
        valor = self.expression.exec()
        symbol_table.set(self.var_name, valor)
    


class function_call():
    def __init__(self, function_name, params):
        self.function_name = function_name
        self.params = params


class bool_statement(Structure):
    def __init__(self, var_name, bool_function):
        self.var_name = var_name
        self.bool_function = bool_function


class if_statement(Structure):
    def __init__(self, condition, statements1, statements2=None):
        self.condition = condition
        self.statements1 = statements1
        if statements2:
            self.statements2 = statements2


class for_loop(Structure):
    def __init__(self, var, to_factor, statements, step_number=None, ):
        self.var = var
        self.to = to_factor
        self.statements = statements
        if step_number:
            self.step = step_number


class en_caso(Structure):
    def __init__(self, switch_list, sino_statements, expression=None):
        self.switch_list = switch_list
        self.sino = sino_statements
        if expression:
            self.expression = expression

class switch0():
    def __init__(self, condition , statements):
        self.condition = condition
        self.statements = statements

class switch_list0():
    def __init__(self, switch0):
        self.switch_list = [switch0]


    def add(self, next_switch):
        self.switch_list.append(next_switch)
    

class switch1():
    def __init__(self, semi_condition , statements):
        self.semi_condition = condition
        self.statements = statements

class switch_list1():
    def __init__(self, switch1):
        self.switch_list = [switch1]

    def add(self, next_switch):
        self.switch_list.append(next_switch)


class statement():
    def __init__(self, statement):
        self.statement_list = [statement]
    
    def add(self, next_statement):
        self.statement_list.append(next_statement)
    
    def printear(self, level):
        print(identation*level + "Statements:")
        for statement in self.statement_list:
            statement.printear(level)
    
    def exec(self):
        for statement in self.statement_list:
            statement.exec()


class callable_function(Structure):
    def __init__(self, function):
        self.function = function

    def add(self, next_function):
        super().add(next_function)

    def get_next(self):
        return super().get_next()


class printer(Structure):
    def __init__(self, param):
        self.param = param


class abanico(Structure):
    def __init__(self, param):
        self.param = param


class vertical(Structure):
    def __init__(self, param):
        self.param = param


class percutor(Structure):
    def __init__(self, param):
        self.param = param


class golpe(Structure):
    def __init__(self, param):
        self.param = param


class vibrato(Structure):
    def __init__(self, param):
        self.param = param


class metronomo(Structure):
    def __init__(self, param):
        self.param = param


class main(Structure):
    def __init__(self, statements):
        self.statements = statements

    def printear(self, level):
        print(identation*level + "Main:")
        self.statements.printear(level+1)
    
    def exec(self):
        self.statements.exec()

class block(Structure):
    def __init__(self, function_decls, main):
        self.function_decls = function_decls
        self.main = main

    def printear(self, level):
        print(identation*level + "Block:")
        self.main.printear(level + 1)

    def exec(self):
        # self.function_decls.exec()
        self.main.exec()        

class function_decl(Structure):
    def __init__(self, function_name, function_decl_params, statements):
        self.function_name = function_name
        self.function_decl_params = function_decl_params
        self.statements = statements

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
        self.param_list.append(next_param)



class program(Structure):
    def __init__(self, block):
        self.block = block
    
    def printear(self):
        print("Program:")
        self.block.printear(2)

    def exec(self):
        self.block.exec()
        print(symbol_table.symbols)



