from distutils.log import error
from parser import parsing_symbol_table
from functionTable import *
from parsingStructure import *

indentation = "     "


# pendiente : validar tipos de datos en aritmetica
#               variables bool


def run_error_checker(prog):
    if prog.block:
        if len(prog.block.function_decls.function_decl_list) > 1:
            eg.line += 1
            check_function_decls(prog.block.function_decls.function_decl_list)
        if prog.block.main:
            print("valid main found.")
            if prog.block.main.statements:
                print(indentation + "valid statement(s) found.")
                check_statement_list(prog.block.main.statements.statement_list)
                # eg.raise_exception("miss", "stat")
        else:
            eg.raise_exception(eg.MISS, eg.S_PRIN)
    else:
        eg.raise_exception(eg.MISS, eg.S_PRIN)
    


# no se puede hacer isinstance para chequear el tipo pq ocuparia los parametros
def check_statement_list(statement_list, isFunction=None):
    eg.line += 1
    for s in statement_list:
        eg.line += 1
        check_statement(s, isFunction)


def check_statement(s, isFunction=None):
    print(2 * indentation + "statement found.")
    if is_boolean(s):
        print(3 * indentation + "en caso found.")
        check_bool_statement(s)
    if isinstance(s, bool_statement):
        check_bool_statement(s, True, isFunction)
    if isinstance(s, callable_function):  # las predeterminadas
        check_callable_function(s)
    if isinstance(s, function_call):
        check_function_call(s)
    if isinstance(s, if_statement):
        print(3 * indentation + "if condition found.")
        check_if(s)
    if isinstance(s, en_caso):
        print(3 * indentation + "en caso found.")
        check_en_caso(s)
    if isinstance(s, for_loop):  # FOR
        print(3 * indentation + "for loop found.")
        check_for_loop(s)
    if isinstance(s, var_decl):  # VAR DECLARATION
        print(3 * indentation + s.var_name + " found in symbol table.")
        check_var(s)
    if isinstance(s, expression):  # ARITHMETIC OR BOOL EXPRESSION
        print(3 * indentation + "expression found.")
        if s.expression.arith_expr_or_bool:
            check_arith_or_bool_expr(s.expression.arith_expr_or_bool)
    if isinstance(s, callable_function):
        print(3 * indentation + "en caso found.")
        check_callable_function(s)
    else:
        print(4 * indentation + "no expression found.")
        # hacer algo


def check_bool_statement(s, assignation=None, isFunction=None):
    if not assignation:
        if not is_boolean(s.var_name):
            if not is_number(s.var_name, True):
                return True
            else:
                eg.raise_exception(eg.INV_DT, eg.S_BOOL, s.var_name)
    else:
        if s.var_name:
            var = get_var_value_in_symbol_table(s.var_name)
            if var is None:
                if not isFunction:
                    eg.raise_exception(eg.INV_VAR, eg.S_UN, s.var_name, eg.line)
            else:
                if not is_boolean(var):
                    eg.raise_exception(eg.INV_DT, eg.S_MISMATCH_AS, s.var_name)



def check_function_decls(fd):
    eg.line += 1
    for f in fd:
        eg.line += 1
        check_function_call(f)
    eg.line += 1


def check_function_call(f):
    if f.function_name:
        check_for_func_in_function_table(f.function_name)
    if f.function_body:
        if f.function_body.statements.statement_list:
            check_statement_list(f.function_body.statements.statement_list, True)
    if f.function_decl_params:
        for p in f.function_decl_params.param_list:
            if check_for_var_in_symbol_table(p, True):
                eg.raise_exception(eg.INV_FUNC, eg.S_FUNC_PARAM)
                eg.line += 1
                check_arith_or_bool_expr(p.arith_expr_or_bool)
    else:
        for p in f.params.param_list:
            if check_for_var_in_symbol_table(p, True):
                eg.raise_exception(eg.INV_FUNC, eg.S_FUNC_PARAM)
                eg.line += 1
                check_arith_or_bool_expr(p.arith_expr_or_bool)


def check_callable_function(s):
    if isinstance(s.function, vibrato):
        if s.function.param.param_list[0]:
            if not isinstance(s.function.param.param_list[0], expression):
                eg.raise_exception(eg.INV_FUNC, eg.S_VIBRATO, None, eg.line)
            if isinstance(s.function.param.param_list[0].arith_expr_or_bool.term.factor, negative):
                eg.raise_exception(eg.INV_FUNC, eg.S_VIBRATO, None, eg.line)
            else:
                if s.function.param.param_list[0].arith_expr_or_bool.term.factor.factor <= 0:
                    eg.raise_exception(eg.INV_FUNC, eg.S_VIBRATO, None, eg.line)
                if check_for_var_in_symbol_table(s.function.param.param_list[0].arith_expr_or_bool.term.factor.factor, True):
                    check_line_validity(s.function.param.param_list[0].arith_expr_or_bool.term.factor.factor, s.function.param.param_list[0].arith_expr_or_bool.term.factor.lineno)
    elif isinstance(s.function, metronomo):
        if s.function.param.param_list[0]:
            p = s.function.param.param_list
            if not (p[0] == '"D"' or p[0] == '"I"' or p[0] == '"A"' or p[0] == '"B"' or p[0] == '"DI"' or p[0] == '"AB"'):
                eg.raise_exception(eg.INV_FUNC, eg.S_METRO, None, eg.line)
            if isinstance(p[1], expression):
                if isinstance(p[1].arith_expr_or_bool.term.factor, negative):
                    eg.raise_exception(eg.INV_FUNC, eg.S_METRO, None, eg.line)
                if p[1].arith_expr_or_bool.term.factor.factor == 0:
                    eg.raise_exception(eg.INV_FUNC, eg.S_METRO, None, eg.line)
                if check_for_var_in_symbol_table(p[1].arith_expr_or_bool.term.factor.factor,
                                                 True):
                    check_line_validity(p[1].arith_expr_or_bool.term.factor.factor,
                                        p[1].arith_expr_or_bool.term.factor.lineno)
            else:
                eg.raise_exception(eg.INV_FUNC, eg.S_METRO, None, eg.line)
    elif isinstance(s.function, abanico):
        for p in s.function.param.param_list:
            if not (p == '"A"' or p == '"B"'):
                eg.raise_exception(eg.INV_FUNC, eg.S_ABANICO, None, eg.line)
    elif isinstance(s.function, vertical):
        for p in s.function.param.param_list:
            if not (p == '"D"' or p == '"I"'):
                eg.raise_exception(eg.INV_FUNC, eg.S_VERTICAL, None, eg.line)
    elif isinstance(s.function, percutor):
        for p in s.function.param.param_list:
            if not (p == '"D"' or p == '"I"'or p == '"A"' or p == '"B"' or p == '"DI"' or p == '"AB"'):
                eg.raise_exception(eg.INV_FUNC, eg.S_PERCUTOR, None, eg.line)
    elif isinstance(s.function, golpe):
        if s.function.param:
            eg.raise_exception(eg.INV_FUNC, eg.S_GOLPE, None, eg.line)




def check_en_caso(s):
    condition_type = False
    if check_for_var_in_symbol_table(s.expression.arith_expr_or_bool.term.factor.factor):
        if not check_line_validity(s.expression.arith_expr_or_bool.term.factor.factor,
                                   s.expression.arith_expr_or_bool.term.factor.lineno):
            return eg.raise_exception(eg.INV_DT, eg.S_UN, s.expression.arith_expr_or_bool.term.factor.factor,
                                      s.expression.arith_expr_or_bool.term.factor.lineno)
        if is_number(s.expression.arith_expr_or_bool.term.factor.factor):
            condition_type = True
        elif is_boolean(s.expression.arith_expr_or_bool.term.factor.factor):
            condition_type = False
        else:
            eg.raise_exception(eg.INV_DT, eg.S_EN_CASO)
        check_statement_list(s.sino.statement_list)
        for sc in s.switch_list.switch_list:
            if is_number(sc.semi_condition.expression.arith_expr_or_bool.term.factor.factor) == condition_type:
                check_statement_list(sc.statements.statement_list)
            else:
                eg.raise_exception(eg.INV_COMP, eg.S_DT)
    else:
        eg.raise_exception(eg.INV_DT, eg.S_UN)


def check_for_loop(for_st):
    # ninguno de estos errores se puede probar, aun
    if is_number(for_st.to.factor, True):
        if not isinstance(for_st.to.factor, int):
            eg.raise_exception(eg.INV_DT, eg.S_TO)
    else:
        eg.raise_exception(eg.INV_DT, eg.S_TO)
    if not is_number(for_st.step, True):
        eg.raise_exception(eg.INV_DT, eg.S_STEP)
    if for_st.step <= 0:
        eg.raise_exception(eg.INV_DT, eg.S_STEP_N)

    if is_number(for_st.var_name):
        if get_var_value_in_symbol_table(for_st.var_name) <= 0:
            eg.raise_exception(eg.INV_DT, eg.S_TO)
    else:
        eg.raise_exception(eg.INV_DT, eg.S_TO)


def check_if(if_st):
    arith_con = False
    arith_semi_con = False
    eg.line += 1
    if if_st.condition_or_expression.arith_expr:
        arith_con = check_arith_or_bool_expr(if_st.condition_or_expression.arith_expr)
    if not if_st.condition_or_expression.semi_condition:
        pass
    else:
        if if_st.condition_or_expression.semi_condition.comparator:
            if if_st.condition_or_expression.semi_condition.expression.arith_expr_or_bool:
                arith_semi_con = check_arith_or_bool_expr(
                    if_st.condition_or_expression.semi_condition.expression.arith_expr_or_bool)
                if arith_con != arith_semi_con:
                    eg.raise_exception(eg.INV_DT, eg.S_MISMATCH_IF)
        if if_st.statements1:
            eg.line += 1
            check_statement_list(if_st.statements1.statement_list)
        if if_st.statements2:
            eg.line += 1
            check_statement_list(if_st.statements2.statement_list)


def check_var(s, line=None):
    if check_for_var_in_symbol_table(s.var_name):
        if line:
            if not check_line_validity(line, s.lineno):
                eg.raise_exception(eg.INV_DT, eg.S_UN, s.var_name, line)
        value = not is_boolean(get_var_value_in_symbol_table(s.var_name))
        if s.expression:
            print(3 * indentation + "expression found.")
            if s.expression.arith_expr_or_bool:
                current = check_arith_or_bool_expr(s.expression.arith_expr_or_bool)
                if value != current:
                    eg.raise_exception(eg.INV_DT, eg.S_MISMATCH_AS, s.var_name, eg.line)
        if get_var_value_in_symbol_table(s.var_name) is None:
            pass


def check_arith_or_bool_expr(s_term):
    # ERROR, NO DEBE LLEGAR UN STRING QUE NO SEA TRUE OR FALSE
    print(4 * indentation + "arithmetic or boolean expression found.")
    valid = True
    if bool_expr(s_term):
        return False
    else:
        if s_term.operator:
            if s_term.arith_expr:
                valid = check_arith_or_bool_expr(s_term.arith_expr)
            if s_term.term.operator:
                valid = check_arith_or_bool_expr(s_term.term)
            if s_term.operator == "//" or s_term.operator == "/":
                if s_term.factor.factor == 0:
                    eg.raise_exception(eg.INV_AP, eg.S_DIV)
        elif s_term.term.operator:
            valid = check_arith_or_bool_expr(s_term.term)
        if s_term.term.factor.factor:
            if isinstance(s_term.term.factor, negative):
                if not is_number(s_term.term.factor.factor.factor, True):
                    if is_boolean(s_term.term.factor.factor.factor):  # es una variable
                        return False
                    else:
                        check_for_var_in_symbol_table(s_term.term.factor.factor.factor)
                        check_var(s_term.term.factor.factor.factor, s_term.term.factor.factor.lineno)

            else:
                if not is_number(s_term.term.factor.factor, True):
                    if is_boolean(s_term.term.factor.factor):  # es una variable
                        return False
                    else:
                        check_for_var_in_symbol_table(s_term.term.factor.factor)
                else:
                    if check_for_var_in_symbol_table(s_term.term.factor.factor, True):
                        check_line_validity(s_term.term.factor.factor, s_term.term.factor.lineno)
        if not valid:
            eg.raise_exception(eg.INV_PARAM, eg.S_ARITH, None, eg.line)
        return True


def check_line_validity(var, current_line):
    set_line = parsing_symbol_table.get_lineno(var)
    if current_line <= set_line:
        eg.raise_exception(eg.INV_VAR, eg.S_UN, var, current_line)
    else:
        return True


def bool_expr(s_term):
    if not isinstance(s_term, bool):
        if not check_for_var_in_symbol_table(s_term, True):
            return False
        else:
            variable = get_var_value_in_symbol_table(s_term)
            return isinstance(variable, bool)
    else:
        return isinstance(s_term, bool)


def is_number(variable, condition=None):
    if not isinstance(variable, int) or isinstance(variable, float):
        if check_for_var_in_symbol_table(variable, condition):
            var = get_var_value_in_symbol_table(variable)
            if isinstance(var, bool):
                return False
            return isinstance(var, int) or isinstance(var, float)
        else:
            return False
    else:
        return isinstance(variable, int) or isinstance(variable, float)


def is_boolean(variable):
    if not isinstance(variable, bool):
        if check_for_var_in_symbol_table(variable, True):
            variable = get_var_value_in_symbol_table(variable)
            return isinstance(variable, bool)
        else:
            return False
    else:
        return isinstance(variable, bool)


def validate_number_operation(simbolo1, simbolo2):
    if is_boolean(simbolo1) or is_boolean(simbolo2):
        eg.raise_exception(eg.INV_DT, eg.S_BOOL)
    try:
        eval(simbolo1)
        eval(simbolo2)
    except:
        eg.raise_exception(eg.INV_DT, "")


def check_for_func_in_function_table(var, condition=None):
    # FALTA QUE EL BICHO RECONOZCA SI EL FOR SE RECORRE HASTA EL INFINITO
    for key in function_table.get_declared_function_keys():
        if key == var:
            return True
    return False


def get_function_body(function_name):
    pass


def check_for_var_in_symbol_table(var, condition=None):
    # FALTA QUE EL BICHO RECONOZCA SI EL FOR SE RECORRE HASTA EL INFINITO
    if parsing_symbol_table.is_in(var):
        return True
    else:
        if not isinstance(var, str):
            var = str(var)
        if not condition:
            eg.raise_exception(eg.INV_VAR, "un", var, eg.line)
        else:
            return False


def get_var_value_in_symbol_table(var):
    return parsing_symbol_table.get(var)


def check_if_validity(comparison):  # que comparison sea una lista
    if is_number(comparison[0], True):
        comp_type = int
    elif is_boolean(comparison[0], True):
        comp_type = bool
    else:
        comp_type = int
        eg.raise_exception(eg.UNEX, eg.S_DT)
    for i in comparison:
        if not isinstance(i, comp_type):
            eg.raise_exception(eg.INV_COMP, eg.S_DT)
    return True


class ExceptionGenerator(Exception):
    line = 1

    error = ''

    INV_DT = "inv_dt"
    INV_DT_AP = "inv_dt_arith_proc"
    INV_AP = "inv_arith"
    INV_COMP = "inv_comp"
    INV_VAR = "inv_var"
    INV_PARAM = "inv_param"
    INV_FUNC = "inv_func"

    UNEX = "unex"
    MISS = "miss"

    S_ARITH = "arith"
    S_EN_CASO = "en_caso"
    S_BOOL = "bool"
    S_STEP = "step"
    S_STEP_N = "step_neg"
    S_TO = "to"
    S_MISMATCH_IF = "if"
    S_MISMATCH_AS = "as"
    S_DIV = "div"
    S_UN = "un"
    S_DT = "dt"
    S_TWO_PRIN = "2_prin"
    S_PRIN = "prin"
    S_STAT = "stat"
    S_EXPR = "expr"
    S_FUNC_CALL = "call"
    S_FUNC_PARAM = "param"
    S_VIBRATO = "vib"
    S_ABANICO = "aban"
    S_VERTICAL = "vert"
    S_PERCUTOR = "perc"
    S_GOLPE = "golpe"
    S_METRO = "metro"


    def get_error(self):
        # print("ERRORRRRR: " + self.error)
        return self.error

    def set_error(self):
        self.error = ''

    def raise_exception(self, exc_num, exc_spec, var=None, line=None):
        match exc_num:
            case self.INV_FUNC:
                msg = "INVALID FUNCTION"
                if exc_spec == self.S_FUNC_CALL:
                    msg = msg + " CALL."
                if exc_spec == self.S_FUNC_PARAM:
                    msg = msg + " PARAM: NAME ALREADY IN USE."
                if exc_spec == self.S_VIBRATO:
                    msg = msg + " CALL VIBRAT0: PARAMETER MUST BE A NATURAL NUMBER."
                if exc_spec == self.S_METRO:
                    msg = msg + " CALL METRONOME: PARAMETER MUST BE A NATURAL NUMBER."
                if exc_spec == self.S_ABANICO:
                    msg = msg + " CALL ABANICO: PARAMETER MUST BE EITHER 'A' OR 'B'."
                if exc_spec == self.S_VERTICAL:
                    msg = msg + " CALL VERTICAL: PARAMETER MUST BE EITHER 'D' OR 'I'."
                if exc_spec == self.S_PERCUTOR:
                    msg = msg + " CALL PERCUTOR: PARAMETER MUST BE 'D', 'I', 'A', 'B, 'DI' OR 'AB'."
                if exc_spec == self.S_GOLPE:
                    msg = msg + " CALL GOLPE: UNEXPECTED PARAMETER."

            case self.INV_DT:
                msg = "INVALID DATATYPE"
                if exc_spec == self.S_BOOL:
                    msg = msg + ": BOOL."

                if exc_spec == self.S_STEP:
                    msg = msg + ": 'STEP' DURING FOR LOOP MUST BE A NUMBER."
                if exc_spec == self.S_STEP_N:
                    msg = msg + ": 'STEP' DURING FOR LOOP MUST BE A NATURAL NUMBER."
                if exc_spec == self.S_TO:
                    msg = msg + ": CONDITION DURING FOR LOOP MUST BE A NATURAL NUMBER."
                if exc_spec == self.S_MISMATCH_IF:
                    msg = msg + " : MISMATCH DURING COMPARISON."
                if exc_spec == self.S_MISMATCH_AS:
                    msg = msg + " : MISMATCH DURING ASSIGNATION"
                if exc_spec == self.S_EN_CASO:
                    msg = msg + " : DURING EN-CASO"
            case self.INV_DT_AP:
                msg = "INVALID DATATYPE DURING ARITHMETIC PROCEDURE."
            case self.INV_AP:
                msg = "INVALID ARITHMETIC PROCEDURE"
                if exc_spec == self.S_DIV:
                    msg = msg + ": CANNOT DIVIDE BY ZERO."
            case self.INV_COMP:
                msg = "INVALID COMPARISON"
                if exc_spec == self.S_DT:
                    msg = msg + "DUE TO MISMATCHED DATATYPES."
            case self.INV_VAR:
                msg = "INVALID VARIABLE"
                if exc_spec == self.S_UN:
                    msg = msg + ": UNASSIGNED VARIABLE CALLED."
            case self.INV_PARAM:
                msg = "INVALID PARAMETER"
                if exc_spec == self.S_ARITH:
                    msg = msg + " DURING ARITHMETIC PROCEDURE: MISMATCHED DATATYPES"
            case self.UNEX:
                msg = "UNEXPECTED"
                if exc_spec == self.S_DT:
                    msg = msg + "DATATYPE."
                if exc_spec == self.S_TWO_PRIN:
                    msg = msg + ": MORE THAN ONE PRINCIPAL DECLARED."

            case self.MISS:
                msg = "MISSING"
                if exc_spec == self.S_PRIN:
                    msg = msg + ": PRINCIPAL."
                if exc_spec == self.S_STAT:
                    msg = msg + ": STATEMENT(S)."
                if exc_spec == self.S_EXPR:
                    msg = msg + ": EXPRESSION"
            case _:
                return 0  # 0 is the default case if x is not found
        if var:
            msg = msg + ": " + var
        if line:
            msg = msg + " ON LINE " + str(self.line)
        if self.error == '':
            self.error = "ERROR: " + msg

        # print("Error 2: " + self.error)
        # print("ERROR: " + msg)
        #return error
        raise Exception("ERROR: " + msg)

# error types:
# 1: invalid data type
# 2: invalid data type during arithmetic procedure
# 3: invalid comparison due to mismatched data types
# que no haya principal
# que el principal este dos veces
# FALTA QUE EL BICHO RECONOZCA SI EL FOR SE RECORRE HASTA EL INFINITO
# se me olvido pero era muy importante
# los de las funciones, parametros positivos

eg = ExceptionGenerator()

# check_for_var_in_symbol_table(1)
# check_if_validity([1, 2])
