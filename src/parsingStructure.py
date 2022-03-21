from msilib.schema import Class


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

class semi_condition(Structure):
    def __init__(self, comparator, expression):
        self.comparator = comparator
        self.term = expression

class condition(Structure):
    def __init_(self, arith_expr, semi_condition):
        self.arith_expr = arith_expr
        self.semi_condition = semi_condition

class var_decl(Structure):
    def __init__(self, name, expression):
        self.name
        self.expression

class if_statement(Structure):
    def __init__(self, condition, statement1, statement2 = None):
        self.condition = condition
        self.statement1 = statement1
        if statement2:
            self.statement2 = statement2

class for_loop(Structure):
    def __init__(self, condition, statement1, statement2 = None):
        self.condition = condition
        self.statement1 = statement1
        if statement2:
            self.statement2 = statement2