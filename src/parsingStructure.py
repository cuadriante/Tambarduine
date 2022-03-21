from msilib.schema import Class
from struct import Struct

from matplotlib.pyplot import step


class Structure:
    def __init__(self):
        self.returned   


class factor():
    def __init__(self, factor):
        self.factor = factor

class term(Structure):
    def __init__(self, term, operator, factor):
        self.term1 = term
        self.term2 = factor
        self.operator = operator

class arith_expr(Structure):
    def __init__(self, arith_expr, operator, term):
        self.term1 = arith_expr
        self.term2 = term
        self.operator = operator

class expression(Structure):
    def __init__(self, expression):
        self.expression = expression

class param(Structure):
    def __init__(self, expr_or_string, next_param = None):
        self.expr_or_string = expr_or_string
        if next_param:
            self.next_param = next_param
        

class semi_condition(Structure):
    def __init__(self, comparator, expression):
        self.comparator = comparator
        self.term = expression

class condition(Structure):
    def __init_(self, arith_expr, semi_condition):
        self.arith_expr = arith_expr
        self.semi_condition = semi_condition

class var_decl(Structure):
    def __init__(self, var_name, expression, next_var_decl = None):
        self.var_name = var_name
        self.expression = expression
        if next_var_decl:
            self.next_var_decl = next_var_decl

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

class switch_list0(Structure):
    def __init__(self, condition , statements, next_switch = None):
        self.condition = condition
        self.statements = statements
        if next_switch:
            self.next_switch = next_switch

class switch_list1(Structure):
    def __init__(self, semi_condition , statements, next_switch = None):
        self.semi_condition = semi_condition
        self.statements = statements
        if next_switch:
            self.next_switch = next_switch

class statement(Structure):
    def __init__(self, statement, next_statement = None):
        self.statement = statement
        self.next_statement = next_statement

class callable_function(Structure):
    def __init__(self, function, next_function = None):
        self.function = function
        self.next_function = next_function
class printer(Structure):
    def __init__(self, param):
        self.param = param
class abanico(Structure):
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
    def __init__(self, main):
        self.main = main
class program(Structure):
    def __init__(self, block):
        self.block = block



