
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightASSIGNleftLESSTHANLESSTHANEMORETHANMORETHANEleftNEGATIVEleftPLUSMINUSleftTIMESDIVIDEWHOLEDIVIDEMODULEleftPOWERleftTRUEFALSEABANICO ASSIGN BOOL CCODE COMMENT CUANDO DEF DIFFERENT DIVIDE ELSE ENCASO ENTONS EQUAL EQUALS EXEC EXPONENTE FALSE FINENCASO FOR FUNCTION GOLPE ID IF In LBRACE LESSTHAN LESSTHANE LPAREN METRONOMO MINUS MODULE MORETHAN MORETHANE NEGATIVE NUMBER PERCUTOR PLUS POWER RBRACE RESERVED RPAREN SEMICOLON SET SINO STEP TIMES TO TRUE VAR VERTICAL VIBRATO WHILE WHOLEDIVIDEexpression : RESERVED VAR ASSIGN expressionexpression : arith-expressionexpression : conditionexpression : if-expressionif-expression : RESERVED condition LBRACE expression RBRACEif-expression : RESERVED condition LBRACE expression RBRACE RESERVED LBRACE expression RBRACEcondition : arith-expression EQUALS arith-expression\n                | arith-expression DIFFERENT arith-expression\n                | arith-expression LESSTHAN arith-expression\n                | arith-expression MORETHAN arith-expression\n                | arith-expression LESSTHANE arith-expression\n                | arith-expression MORETHANE arith-expressioncondition : NEGATIVE conditionarith-expression : arith-expression PLUS termarith-expression : arith-expression MINUS termarith-expression : termterm : term TIMES factorterm : term POWER factorterm : term DIVIDE factorterm : term MODULE factorterm : term WHOLEDIVIDE factorterm : factorfactor : NUMBERfactor : VARfactor : LPAREN expression RPAREN'
    
_lr_action_items = {'RESERVED':([0,11,30,31,48,50,],[2,2,2,2,49,2,]),'NEGATIVE':([0,2,8,11,30,31,50,],[8,8,8,8,8,8,8,]),'NUMBER':([0,2,8,11,15,16,17,18,19,20,21,22,23,24,25,26,27,30,31,50,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'VAR':([0,2,8,11,15,16,17,18,19,20,21,22,23,24,25,26,27,30,31,50,],[3,12,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'LPAREN':([0,2,8,11,15,16,17,18,19,20,21,22,23,24,25,26,27,30,31,50,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'$end':([1,3,4,5,6,7,9,10,28,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,48,52,],[0,-24,-2,-3,-4,-16,-22,-23,-13,-14,-15,-7,-8,-9,-10,-11,-12,-17,-18,-19,-20,-21,-25,-1,-5,-6,]),'TIMES':([3,7,9,10,12,32,33,40,41,42,43,44,45,],[-24,23,-22,-23,-24,23,23,-17,-18,-19,-20,-21,-25,]),'POWER':([3,7,9,10,12,32,33,40,41,42,43,44,45,],[-24,24,-22,-23,-24,24,24,-17,-18,-19,-20,-21,-25,]),'DIVIDE':([3,7,9,10,12,32,33,40,41,42,43,44,45,],[-24,25,-22,-23,-24,25,25,-17,-18,-19,-20,-21,-25,]),'MODULE':([3,7,9,10,12,32,33,40,41,42,43,44,45,],[-24,26,-22,-23,-24,26,26,-17,-18,-19,-20,-21,-25,]),'WHOLEDIVIDE':([3,7,9,10,12,32,33,40,41,42,43,44,45,],[-24,27,-22,-23,-24,27,27,-17,-18,-19,-20,-21,-25,]),'PLUS':([3,4,7,9,10,12,14,32,33,34,35,36,37,38,39,40,41,42,43,44,45,],[-24,15,-16,-22,-23,-24,15,-14,-15,15,15,15,15,15,15,-17,-18,-19,-20,-21,-25,]),'MINUS':([3,4,7,9,10,12,14,32,33,34,35,36,37,38,39,40,41,42,43,44,45,],[-24,16,-16,-22,-23,-24,16,-14,-15,16,16,16,16,16,16,-17,-18,-19,-20,-21,-25,]),'EQUALS':([3,4,7,9,10,12,14,32,33,40,41,42,43,44,45,],[-24,17,-16,-22,-23,-24,17,-14,-15,-17,-18,-19,-20,-21,-25,]),'DIFFERENT':([3,4,7,9,10,12,14,32,33,40,41,42,43,44,45,],[-24,18,-16,-22,-23,-24,18,-14,-15,-17,-18,-19,-20,-21,-25,]),'LESSTHAN':([3,4,7,9,10,12,14,32,33,40,41,42,43,44,45,],[-24,19,-16,-22,-23,-24,19,-14,-15,-17,-18,-19,-20,-21,-25,]),'MORETHAN':([3,4,7,9,10,12,14,32,33,40,41,42,43,44,45,],[-24,20,-16,-22,-23,-24,20,-14,-15,-17,-18,-19,-20,-21,-25,]),'LESSTHANE':([3,4,7,9,10,12,14,32,33,40,41,42,43,44,45,],[-24,21,-16,-22,-23,-24,21,-14,-15,-17,-18,-19,-20,-21,-25,]),'MORETHANE':([3,4,7,9,10,12,14,32,33,40,41,42,43,44,45,],[-24,22,-16,-22,-23,-24,22,-14,-15,-17,-18,-19,-20,-21,-25,]),'RPAREN':([3,4,5,6,7,9,10,28,29,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,48,52,],[-24,-2,-3,-4,-16,-22,-23,-13,45,-14,-15,-7,-8,-9,-10,-11,-12,-17,-18,-19,-20,-21,-25,-1,-5,-6,]),'LBRACE':([3,7,9,10,13,28,32,33,34,35,36,37,38,39,40,41,42,43,44,45,49,],[-24,-16,-22,-23,31,-13,-14,-15,-7,-8,-9,-10,-11,-12,-17,-18,-19,-20,-21,-25,50,]),'RBRACE':([3,4,5,6,7,9,10,28,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,],[-24,-2,-3,-4,-16,-22,-23,-13,-14,-15,-7,-8,-9,-10,-11,-12,-17,-18,-19,-20,-21,-25,-1,48,-5,52,-6,]),'ASSIGN':([12,],[30,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,11,30,31,50,],[1,29,46,47,51,]),'arith-expression':([0,2,8,11,17,18,19,20,21,22,30,31,50,],[4,14,14,4,34,35,36,37,38,39,4,4,4,]),'condition':([0,2,8,11,30,31,50,],[5,13,28,5,5,5,5,]),'if-expression':([0,11,30,31,50,],[6,6,6,6,6,]),'term':([0,2,8,11,15,16,17,18,19,20,21,22,30,31,50,],[7,7,7,7,32,33,7,7,7,7,7,7,7,7,7,]),'factor':([0,2,8,11,15,16,17,18,19,20,21,22,23,24,25,26,27,30,31,50,],[9,9,9,9,9,9,9,9,9,9,9,9,40,41,42,43,44,9,9,9,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> RESERVED VAR ASSIGN expression','expression',4,'p_expression_var','parser.py',36),
  ('expression -> arith-expression','expression',1,'p_expression_arith','parser.py',42),
  ('expression -> condition','expression',1,'p_expression_comp','parser.py',45),
  ('expression -> if-expression','expression',1,'p_expression_if','parser.py',48),
  ('if-expression -> RESERVED condition LBRACE expression RBRACE','if-expression',5,'p_if','parser.py',59),
  ('if-expression -> RESERVED condition LBRACE expression RBRACE RESERVED LBRACE expression RBRACE','if-expression',9,'p_if_else','parser.py',72),
  ('condition -> arith-expression EQUALS arith-expression','condition',3,'p_cond_arith','parser.py',85),
  ('condition -> arith-expression DIFFERENT arith-expression','condition',3,'p_cond_arith','parser.py',86),
  ('condition -> arith-expression LESSTHAN arith-expression','condition',3,'p_cond_arith','parser.py',87),
  ('condition -> arith-expression MORETHAN arith-expression','condition',3,'p_cond_arith','parser.py',88),
  ('condition -> arith-expression LESSTHANE arith-expression','condition',3,'p_cond_arith','parser.py',89),
  ('condition -> arith-expression MORETHANE arith-expression','condition',3,'p_cond_arith','parser.py',90),
  ('condition -> NEGATIVE condition','condition',2,'p_cond_negative','parser.py',104),
  ('arith-expression -> arith-expression PLUS term','arith-expression',3,'p_arith_plus','parser.py',110),
  ('arith-expression -> arith-expression MINUS term','arith-expression',3,'p_arith_minus','parser.py',113),
  ('arith-expression -> term','arith-expression',1,'p_arith_term','parser.py',116),
  ('term -> term TIMES factor','term',3,'p_term_times','parser.py',124),
  ('term -> term POWER factor','term',3,'p_term_exponente','parser.py',127),
  ('term -> term DIVIDE factor','term',3,'p_term_div','parser.py',130),
  ('term -> term MODULE factor','term',3,'p_term_mod','parser.py',133),
  ('term -> term WHOLEDIVIDE factor','term',3,'p_term_wholediv','parser.py',136),
  ('term -> factor','term',1,'p_term_factor','parser.py',139),
  ('factor -> NUMBER','factor',1,'p_factor_num','parser.py',144),
  ('factor -> VAR','factor',1,'p_factor_var','parser.py',147),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','parser.py',151),
]
