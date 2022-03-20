from msilib.schema import Class


class Structure:
    def lala():
        pass


class factor(Structure):
    def __init__(self, factor):
        pass

class termOperation(Structure):
    def __init__(self, term1, operator ,term2):
        self.term1 = term1
        self.term2 = term2
        self.operator = operator

class arith_exprOperation(Structure):
    def __init__(self, term1, operator ,term2):
        self.term1 = term1
        self.term2 = term2
        self.operator = operator

class semi_condition(Structure):
    def __init__(self, comparator ,term):
        self.comparator = comparator
        self.term = term

class condition(Structure):
    


