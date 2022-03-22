from msilib.schema import Class
from struct import Struct

from matplotlib.pyplot import step

class Structure:
    pass
    # def print(self, params):
    #     for i in params:
    #         params.print()

class Many:
    def set_next(self, next):
        self.next = next

    def get_many(self):
        return self.next

class factor():
    def __init__(self, factor):
        self.factor = factor

class term(Structure):
    def __init__(self, factor, term = None, operator = None):
        if term and operator:
            self.term = term
            self.operator = operator
        self.factor = factor

class arith_expr(Structure):
    def __init__(self, term, arith_expr = None, operator = None):
        if arith_expr and operator:
            self.arith_expr = arith_expr
            self.operator = operator
        self.term = term
            

class expression(Structure):
    def __init__(self, arith_expr_or_bool):
        self.arith_expr_or_bool = arith_expr_or_bool

class param(Many):
    def __init__(self, expr_or_string):
        self.expr_or_string = expr_or_string
    
    def set_next(self, next_param):
        super().set_next(next_param)
    
    def get_next(self):
        return super().get_next()

class semi_condition(Structure):
    def __init__(self, comparator, expression):
        self.comparator = comparator
        self.term = expression

class condition(Structure):
    def __init_(self, arith_expr, semi_condition):
        self.arith_expr = arith_expr
        self.semi_condition = semi_condition

class var_decl(Many):
    def __init__(self, var_name, expression):
        self.var_name = var_name
        self.expression = expression
    
    def set_next(self, next_var_decl):
        super().set_next(next_var_decl)
    
    def get_next(self):
        return super().get_next()

class function_call(Many):
    def __init__(self, function_name, params):
        self.function_name = function_name
        self.params = params
    
    def set_next(self, next_var_decl):
        super().set_next(next_var_decl)
    
    def get_next(self):
        return super().get_next()

class bool_statement(Structure):
    def __init__(self, var_name, bool_function):
        self.var_name = var_name
        self.bool_function = bool_function

class if_statement(Structure):
    def __init__(self, condition, statements1, statements2 = None):
        self.condition = condition
        self.statements1 = statements1
        if statements2:
            self.statements2 = statements2

class for_loop(Structure):
    def __init__(self, var , to_factor, statements, step_number = None, ):
        self.var = var
        self.to = to_factor
        self.statements = statements
        if step_number:
            self.step = step_number

class en_caso(Structure):
    def __init__(self, switch_list , sino_statements, expression = None):
        self.switch_list = switch_list
        self.sino = sino_statements
        if expression:
            self.expression = expression

class switch_list0(Many):
    def __init__(self, condition , statements):
        self.condition = condition
        self.statements = statements

    def set_next(self, next_switch):
        super().set_next(next_switch)
    
    def get_next(self):
        return super().get_next()

class switch_list1(Many):
    def __init__(self, semi_condition , statements):
        self.semi_condition = semi_condition
        self.statements = statements

    def set_next(self, next_switch):
        super().set_next(next_switch)
    
    def get_next(self):
        return super().get_next()

class statement(Many):
    def __init__(self, statement):
        self.statement = statement
    
    def set_next(self, next_statement):
        super().set_next(next_statement)
    
    def get_next(self):
        return super().get_next()

class callable_function(Structure):
    def __init__(self, function):
        self.function = function

    def set_next(self, next_function):
        super().set_next(next_function)
    
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
        self.statemnts = statements
class block(Structure):
    def __init__(self, function_decls, main):
        self.function_decls = function_decls
        self.main = main

class function_decl(Structure):
    def __init__(self, function_name, function_decl_params, statements):
        self.function_name = function_name
        self.function_decl_params = function_decl_params
        self.statements = statements
    def set_next(self, next_function_decls):
        super().set_next(next_function_decls)
    def get_next(self):
        return super().get_next()

class function_decls_param(Structure):
    def __init__(self, var_name):
        self.var_name = var_name
    def set_next(self, next_function_params):
        super().set_next(next_function_params)
    def get_next(self):
        return super().get_next()

class program(Structure):
    def __init__(self, block):
        self.block = block



