from symbolTable import *

indentation = "     "


def run_error_checker(program):
    if program.block.main:
        print("valid main found.")
        if program.block.main.statements:
            print(indentation + "valid statement(s) found.")
            for s in program.block.main.statements.statement_list:
                print(2 * indentation + "statement found.")
                if s.expression:
                    print(3 * indentation + "expression found.")
                    if s.expression.arith_expr_or_bool:
                        check_arith_expr(s.expression.arith_expr_or_bool)
                else:
                    print(4 * indentation + "no expression found.")
                    # hacer algo
            # eg.raise_exception("miss", "stat")
    else:
        eg.raise_exception("miss", "prin")


def check_arith_expr(s_term):
    print(3 * indentation + "arithmetic or boolean expression found.")
    valid = True
    if s_term.operator:
        if s_term.arith_expr:
            print("bajando arith " + str(s_term.factor))
            valid = check_arith_expr(s_term.arith_expr)
            print("subiendo arith " + str(s_term.factor))
        if s_term.term.operator:
            print("bajando term " + str(s_term.factor))
            valid = check_arith_expr(s_term.term)
            print("subiendo term " + str(s_term.factor))
        if s_term.operator == "//" or s_term.operator == "/":
            if s_term.factor.factor == 0:
                eg.raise_exception("inv_arith", "div")
    if not valid:
        eg.raise_exception("inv_param", "")
    return True


def is_number(variable):
    return isinstance(variable, int) or isinstance(variable, float)


def is_boolean(variable):
    return variable == 'True' or variable == 'False'


def validate_number_operation(simbolo1, simbolo2):
    if is_boolean(simbolo1) or is_boolean(simbolo2):
        eg.raise_exception("inv_dt_bool", "bool")
    try:
        eval(simbolo1)
        eval(simbolo2)
    except:
        eg.raise_exception("inv_dt", "")


def check_for_var_in_symbol_table(var):
    if not is_number(var) or is_boolean(var):
        eg.raise_exception("inv_dt", "")
    if symbol_table.get(var):
        return True
    else:
        eg.raise_exception("inv_var", "un")


def check_if_validity(comparison):  # que comparison sea una lista
    if is_number(comparison[0]):
        comp_type = int
    elif is_boolean(comparison[0]):
        comp_type = bool
    else:
        comp_type = int
        eg.raise_exception("unex", "dt")
    for i in comparison:
        if not isinstance(i, comp_type):
            eg.raise_exception("inv_comp", "dt")
    return True


class ExceptionGenerator(Exception):

    def raise_exception(self, exc_num, exc_spec):
        match exc_num:
            case "inv_dt":
                msg = "INVALID DATATYPE"
                if exc_spec == "bool":
                    msg = msg + ": BOOL."
            case "inv_dt_arith_proc":
                msg = "INVALID DATATYPE DURING ARITHMETIC PROCEDURE."
            case "inv_arith":
                msg = "INVALID ARITHMETIC PROCEDURE"
                if exc_spec == "div":
                    msg = msg + ": CANNOT DIVIDE BY ZERO."
            case "inv_comp":
                msg = "INVALID COMPARISON"
                if exc_spec == "dt":
                    msg = msg + "DUE TO MISMATCHED DATATYPES."
            case "inv_var":
                msg = "INVALID VARIABLE"
                if exc_spec == "un":
                    msg = msg + ": UNASSIGNED VARIABLE CALLED."
            case "inv_param":
                raise Exception("INVALID PARAMETER.")
            case "unex":
                msg = "UNEXPECTED"
                if exc_spec == "dt":
                    msg = msg + "DATATYPE."
                if exc_spec == "2_prin":
                    msg = msg + ": MORE THAN ONE PRINCIPAL DECLARED."

            case "miss":
                msg = "MISSING"
                if exc_spec == "prin":
                    msg = msg + ": PRINCIPAL."
                if exc_spec == "stat":
                    msg = msg + ": STATEMENT(S)."
                if exc_spec == "expr":
                    msg = msg + ": EXPRESSION"
            case _:
                return 0  # 0 is the default case if x is not found
        raise Exception("ERROR: " + msg)


# error types:
# 1: invalid data type
# 2: invalid data type during arithmetic procedure
# 3: invalid comparison due to mismatched data types
# que no haya principal
# que el principal este dos veces

eg = ExceptionGenerator()

# check_for_var_in_symbol_table(1)
check_if_validity([1, 2])
