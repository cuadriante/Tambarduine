from symbolTable import *
from parsingStructure import *

indentation = "     "



# pendiente : validar tipos de datos en aritmetica
#               variables bool

def run_error_checker(prog):
    if prog.block.main:
        print("valid main found.")
        if prog.block.main.statements:
            print(indentation + "valid statement(s) found.")
            check_statement_list(prog.block.main.statements.statement_list)
            # eg.raise_exception("miss", "stat")
    else:
        eg.raise_exception("miss", "prin")


# no se puede hacer isinstance para chequear el tipo pq ocuparia los parametros
def check_statement_list(statement_list):
    for s in statement_list:
        print(2 * indentation + "statement found.")
        if s.step:  # FOR
            print(3 * indentation + "for loop found.")
            check_for(s)
        if s.condition:  # IF
            print(3 * indentation + "if condition found.")
            check_if(s)
        if s.var_name:  # VAR DECLARATION
            print(3 * indentation + s.var_name + " found in symbol table.")
            check_var(s)
        if s.expression:  # ARITHMETIC OR BOOL EXPRESSION
            print(3 * indentation + "expression found.")
            if s.expression.arith_expr_or_bool:
                check_arith_or_bool_expr(s.expression.arith_expr_or_bool)
        else:
            print(4 * indentation + "no expression found.")
            # hacer algo


def check_for(for_st): # ninguno de estos errores se puede probar, aun
    if not is_number(for_st.step):
        eg.raise_exception(eg.INV_DT, eg.S_STEP)
    if for_st.step <= 0:
        eg.raise_exception(eg.INV_DT, eg.S_STEP_N)
    if not is_number(for_st.to.factor):
        eg.raise_exception(eg.INV_DT, eg.S_TO)
    pass


def check_if(if_st):
    arith_con = False
    arith_semi_con = False

    if if_st.condition.arith_expr:
        arith_con = check_arith_or_bool_expr(if_st.condition.arith_expr)
    if if_st.condition.semi_condition.comparator:
        if if_st.condition.semi_condition.expression.arith_expr_or_bool:
            arith_semi_con = check_arith_or_bool_expr(if_st.condition.semi_condition.expression.arith_expr_or_bool)
            if arith_con != arith_semi_con:
                eg.raise_exception(eg.INV_DT, eg.S_IF)
    if if_st.statements1:
        check_statement_list(if_st.statements1.statement_list)
    if if_st.statements2:
        check_statement_list(if_st.statements2.statement_list)


def check_var(s):
    if check_for_var_in_symbol_table(s.var_name):
        if s.expression:
            print(3 * indentation + "expression found.")
            if s.expression.arith_expr_or_bool:
                check_arith_or_bool_expr(s.expression.arith_expr_or_bool)


def check_arith_or_bool_expr(s_term):
    print(4 * indentation + "arithmetic or boolean expression found.")
    valid = True
    if is_boolean(s_term):
        return False
    else:
        if s_term.operator:
            if s_term.arith_expr:
                valid = check_arith_or_bool_expr(s_term.arith_expr)
            if s_term.term.operator:
                valid = check_arith_or_bool_expr(s_term.term)
            if s_term.operator == "//" or s_term.operator == "/":
                if s_term.factor.factor == 0:
                    eg.raise_exception("inv_arith", "div")
        elif s_term.term.operator:
            valid = check_arith_or_bool_expr(s_term.term)
        elif s_term.term.factor.factor:
            if not is_number(s_term.term.factor.factor):
                check_for_var_in_symbol_table(s_term.term.factor.factor)
                var_value = check_var_value_in_symbol_table(s_term.term.factor.factor)
                if is_boolean(var_value): # es una variable
                    return False
        if not valid:
            eg.raise_exception("inv_param", "")
        return True


def is_number(variable):
    return isinstance(variable, int) or isinstance(variable, float)


def is_boolean(variable):
    return isinstance(variable, bool)


def validate_number_operation(simbolo1, simbolo2):
    if is_boolean(simbolo1) or is_boolean(simbolo2):
        eg.raise_exception("inv_dt_bool", "bool")
    try:
        eval(simbolo1)
        eval(simbolo2)
    except:
        eg.raise_exception("inv_dt", "")


def check_for_var_in_symbol_table(var):
    if symbol_table.get(var):
        return True
    else:
        eg.raise_exception("inv_var", "un")

def check_var_value_in_symbol_table(var):
    return symbol_table.get(var)

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
    #   HACER ESTO MAS BONITO CON LA LISTA DE COMANDOS
    INV_DT = "inv_dt"
    S_STEP = "step"
    S_STEP_N = "step_neg"
    S_TO = "to"
    S_IF = "if"

    def raise_exception(self, exc_num, exc_spec):
        match exc_num:
            case "inv_dt":
                msg = "INVALID DATATYPE"
                if exc_spec == "bool":
                    msg = msg + ": BOOL."
                if exc_spec == "step":
                    msg = msg + ": 'STEP' DURING FOR LOOP MUST BE A NUMBER."
                if exc_spec == "step_neg":
                    msg = msg + ": 'STEP' DURING FOR LOOP MUST BE A NATURAL NUMBER."
                if exc_spec == "to":
                    msg = msg + ": 'FOR' DURING FOR LOOP MUST BE A NUMBER."
                if exc_spec == "if":
                    msg = msg + " : MISMATCH DURING COMPARISON."
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
