
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightASSIGNleftLESSTHANLESSTHANEMORETHANMORETHANEleftNEGATIVEleftPLUSMINUSleftTIMESDIVIDEWHOLEDIVIDEMODULEleftPOWERleftTRUEFALSEABANICO ASSIGN BOOL CCODE COMMENT CUANDO DEF DIFFERENT DIVIDE ELSE ENCASO ENTONS EQUAL EQUALS EXEC EXPONENTE FALSE FINENCASO FOR FUNCTION GOLPE ID IF In LBRACE LESSTHAN LESSTHANE LPAREN METRONOMO MINUS MODULE MORETHAN MORETHANE NEG NEGATIVE NUMBER PERCUTOR PLUS POWER PRINCIPAL RBRACE RESERVED RPAREN SEMICOLON SET SINO STEP TIMES TO TRUE VAR VERTICAL VIBRATO WHILE WHOLEDIVIDEprogram : blockline : boolean_negblock : mainmain : lineline : expression\n        | var_declvar_decl : SET var_assigment_list SEMICOLONvar_assigment_list : VAR ASSIGN expression var_assigment_list : var_assigment_list VAR ASSIGN expression boolean_neg : SET VAR NEG SEMICOLONexpression : arith-expressionexpression : BOOLexpression : conditionexpression : if-expressionexpression : for-loopif-expression : RESERVED condition expression RBRACEif-expression : RESERVED condition expression RBRACE RESERVED expression RBRACEfor-loop : RESERVED VAR RESERVED factor RESERVED NUMBER expression RBRACEcondition : arith-expression EQUALS arith-expression\n                | arith-expression DIFFERENT arith-expression\n                | arith-expression LESSTHAN arith-expression\n                | arith-expression MORETHAN arith-expression\n                | arith-expression LESSTHANE arith-expression\n                | arith-expression MORETHANE arith-expressioncondition : NEGATIVE conditionarith-expression : arith-expression PLUS termarith-expression : arith-expression MINUS termarith-expression : termterm : term TIMES factorterm : term POWER factorterm : term DIVIDE factorterm : term MODULE factorterm : term WHOLEDIVIDE factorterm : factorfactor : NUMBERfactor : VARfactor : LPAREN expression RPAREN'
    
_lr_action_items = {'SET':([0,],[8,]),'BOOL':([0,9,15,18,19,20,36,38,42,45,46,47,48,49,50,51,52,53,54,55,56,57,60,63,67,70,],[11,-36,-28,-34,-35,11,-25,11,11,-26,-27,-19,-20,-21,-22,-23,-24,-29,-30,-31,-32,-33,-37,11,11,11,]),'NEGATIVE':([0,9,15,16,17,18,19,20,36,38,42,45,46,47,48,49,50,51,52,53,54,55,56,57,60,63,67,70,],[16,-36,-28,16,16,-34,-35,16,-25,16,16,-26,-27,-19,-20,-21,-22,-23,-24,-29,-30,-31,-32,-33,-37,16,16,16,]),'RESERVED':([0,9,15,18,19,20,36,38,39,42,45,46,47,48,49,50,51,52,53,54,55,56,57,60,63,64,65,67,70,],[17,-36,-28,-34,-35,17,-25,17,59,17,-26,-27,-19,-20,-21,-22,-23,-24,-29,-30,-31,-32,-33,-37,17,67,68,17,17,]),'NUMBER':([0,9,15,16,17,18,19,20,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,42,45,46,47,48,49,50,51,52,53,54,55,56,57,59,60,63,67,68,70,],[19,-36,-28,19,19,-34,-35,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-25,19,19,-26,-27,-19,-20,-21,-22,-23,-24,-29,-30,-31,-32,-33,19,-37,19,19,70,19,]),'VAR':([0,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,42,45,46,47,48,49,50,51,52,53,54,55,56,57,59,60,62,63,64,66,67,70,71,73,],[9,21,-36,-11,-12,-13,-14,-15,-28,9,39,-34,-35,9,44,9,9,9,9,9,9,9,9,9,9,9,9,9,-25,9,9,-26,-27,-19,-20,-21,-22,-23,-24,-29,-30,-31,-32,-33,9,-37,-8,9,-16,-9,9,9,-17,-18,]),'LPAREN':([0,9,15,16,17,18,19,20,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,42,45,46,47,48,49,50,51,52,53,54,55,56,57,59,60,63,67,70,],[20,-36,-28,20,20,-34,-35,20,20,20,20,20,20,20,20,20,20,20,20,20,20,-25,20,20,-26,-27,-19,-20,-21,-22,-23,-24,-29,-30,-31,-32,-33,20,-37,20,20,20,]),'$end':([1,2,3,4,5,6,7,9,10,11,12,13,14,15,18,19,36,43,45,46,47,48,49,50,51,52,53,54,55,56,57,60,61,64,71,73,],[0,-1,-3,-4,-2,-5,-6,-36,-11,-12,-13,-14,-15,-28,-34,-35,-25,-7,-26,-27,-19,-20,-21,-22,-23,-24,-29,-30,-31,-32,-33,-37,-10,-16,-17,-18,]),'TIMES':([9,15,18,19,39,45,46,53,54,55,56,57,60,],[-36,31,-34,-35,-36,31,31,-29,-30,-31,-32,-33,-37,]),'POWER':([9,15,18,19,39,45,46,53,54,55,56,57,60,],[-36,32,-34,-35,-36,32,32,-29,-30,-31,-32,-33,-37,]),'DIVIDE':([9,15,18,19,39,45,46,53,54,55,56,57,60,],[-36,33,-34,-35,-36,33,33,-29,-30,-31,-32,-33,-37,]),'MODULE':([9,15,18,19,39,45,46,53,54,55,56,57,60,],[-36,34,-34,-35,-36,34,34,-29,-30,-31,-32,-33,-37,]),'WHOLEDIVIDE':([9,15,18,19,39,45,46,53,54,55,56,57,60,],[-36,35,-34,-35,-36,35,35,-29,-30,-31,-32,-33,-37,]),'PLUS':([9,10,15,18,19,37,39,45,46,47,48,49,50,51,52,53,54,55,56,57,60,],[-36,23,-28,-34,-35,23,-36,-26,-27,23,23,23,23,23,23,-29,-30,-31,-32,-33,-37,]),'MINUS':([9,10,15,18,19,37,39,45,46,47,48,49,50,51,52,53,54,55,56,57,60,],[-36,24,-28,-34,-35,24,-36,-26,-27,24,24,24,24,24,24,-29,-30,-31,-32,-33,-37,]),'EQUALS':([9,10,15,18,19,37,39,45,46,53,54,55,56,57,60,],[-36,25,-28,-34,-35,25,-36,-26,-27,-29,-30,-31,-32,-33,-37,]),'DIFFERENT':([9,10,15,18,19,37,39,45,46,53,54,55,56,57,60,],[-36,26,-28,-34,-35,26,-36,-26,-27,-29,-30,-31,-32,-33,-37,]),'LESSTHAN':([9,10,15,18,19,37,39,45,46,53,54,55,56,57,60,],[-36,27,-28,-34,-35,27,-36,-26,-27,-29,-30,-31,-32,-33,-37,]),'MORETHAN':([9,10,15,18,19,37,39,45,46,53,54,55,56,57,60,],[-36,28,-28,-34,-35,28,-36,-26,-27,-29,-30,-31,-32,-33,-37,]),'LESSTHANE':([9,10,15,18,19,37,39,45,46,53,54,55,56,57,60,],[-36,29,-28,-34,-35,29,-36,-26,-27,-29,-30,-31,-32,-33,-37,]),'MORETHANE':([9,10,15,18,19,37,39,45,46,53,54,55,56,57,60,],[-36,30,-28,-34,-35,30,-36,-26,-27,-29,-30,-31,-32,-33,-37,]),'RPAREN':([9,10,11,12,13,14,15,18,19,36,40,45,46,47,48,49,50,51,52,53,54,55,56,57,60,64,71,73,],[-36,-11,-12,-13,-14,-15,-28,-34,-35,-25,60,-26,-27,-19,-20,-21,-22,-23,-24,-29,-30,-31,-32,-33,-37,-16,-17,-18,]),'RBRACE':([9,10,11,12,13,14,15,18,19,36,45,46,47,48,49,50,51,52,53,54,55,56,57,58,60,64,69,71,72,73,],[-36,-11,-12,-13,-14,-15,-28,-34,-35,-25,-26,-27,-19,-20,-21,-22,-23,-24,-29,-30,-31,-32,-33,64,-37,-16,71,-17,73,-18,]),'SEMICOLON':([9,10,11,12,13,14,15,18,19,22,36,41,45,46,47,48,49,50,51,52,53,54,55,56,57,60,62,64,66,71,73,],[-36,-11,-12,-13,-14,-15,-28,-34,-35,43,-25,61,-26,-27,-19,-20,-21,-22,-23,-24,-29,-30,-31,-32,-33,-37,-8,-16,-9,-17,-18,]),'NEG':([21,],[41,]),'ASSIGN':([21,44,],[42,63,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'block':([0,],[2,]),'main':([0,],[3,]),'line':([0,],[4,]),'boolean_neg':([0,],[5,]),'expression':([0,20,38,42,63,67,70,],[6,40,58,62,66,69,72,]),'var_decl':([0,],[7,]),'arith-expression':([0,16,17,20,25,26,27,28,29,30,38,42,63,67,70,],[10,37,37,10,47,48,49,50,51,52,10,10,10,10,10,]),'condition':([0,16,17,20,38,42,63,67,70,],[12,36,38,12,12,12,12,12,12,]),'if-expression':([0,20,38,42,63,67,70,],[13,13,13,13,13,13,13,]),'for-loop':([0,20,38,42,63,67,70,],[14,14,14,14,14,14,14,]),'term':([0,16,17,20,23,24,25,26,27,28,29,30,38,42,63,67,70,],[15,15,15,15,45,46,15,15,15,15,15,15,15,15,15,15,15,]),'factor':([0,16,17,20,23,24,25,26,27,28,29,30,31,32,33,34,35,38,42,59,63,67,70,],[18,18,18,18,18,18,18,18,18,18,18,18,53,54,55,56,57,18,18,65,18,18,18,]),'var_assigment_list':([8,],[22,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> block','program',1,'p_program','parserCop.py',42),
  ('line -> boolean_neg','line',1,'p_program_boolean_neg','parserCop.py',47),
  ('block -> main','block',1,'p_block','parserCop.py',55),
  ('main -> line','main',1,'p_main','parserCop.py',69),
  ('line -> expression','line',1,'p_line','parserCop.py',75),
  ('line -> var_decl','line',1,'p_line','parserCop.py',76),
  ('var_decl -> SET var_assigment_list SEMICOLON','var_decl',3,'p_var_decl','parserCop.py',91),
  ('var_assigment_list -> VAR ASSIGN expression','var_assigment_list',3,'p_var_assigment','parserCop.py',96),
  ('var_assigment_list -> var_assigment_list VAR ASSIGN expression','var_assigment_list',4,'p_var_assigment_list','parserCop.py',104),
  ('boolean_neg -> SET VAR NEG SEMICOLON','boolean_neg',4,'p_boolean_','parserCop.py',113),
  ('expression -> arith-expression','expression',1,'p_expression_arith','parserCop.py',120),
  ('expression -> BOOL','expression',1,'p_expression_boolean','parserCop.py',125),
  ('expression -> condition','expression',1,'p_expression_comp','parserCop.py',130),
  ('expression -> if-expression','expression',1,'p_expression_if','parserCop.py',135),
  ('expression -> for-loop','expression',1,'p_expression_for','parserCop.py',140),
  ('if-expression -> RESERVED condition expression RBRACE','if-expression',4,'p_if','parserCop.py',147),
  ('if-expression -> RESERVED condition expression RBRACE RESERVED expression RBRACE','if-expression',7,'p_if_else','parserCop.py',162),
  ('for-loop -> RESERVED VAR RESERVED factor RESERVED NUMBER expression RBRACE','for-loop',8,'p_for','parserCop.py',179),
  ('condition -> arith-expression EQUALS arith-expression','condition',3,'p_cond_arith','parserCop.py',190),
  ('condition -> arith-expression DIFFERENT arith-expression','condition',3,'p_cond_arith','parserCop.py',191),
  ('condition -> arith-expression LESSTHAN arith-expression','condition',3,'p_cond_arith','parserCop.py',192),
  ('condition -> arith-expression MORETHAN arith-expression','condition',3,'p_cond_arith','parserCop.py',193),
  ('condition -> arith-expression LESSTHANE arith-expression','condition',3,'p_cond_arith','parserCop.py',194),
  ('condition -> arith-expression MORETHANE arith-expression','condition',3,'p_cond_arith','parserCop.py',195),
  ('condition -> NEGATIVE condition','condition',2,'p_cond_negative','parserCop.py',211),
  ('arith-expression -> arith-expression PLUS term','arith-expression',3,'p_arith_plus','parserCop.py',217),
  ('arith-expression -> arith-expression MINUS term','arith-expression',3,'p_arith_minus','parserCop.py',222),
  ('arith-expression -> term','arith-expression',1,'p_arith_term','parserCop.py',227),
  ('term -> term TIMES factor','term',3,'p_term_times','parserCop.py',233),
  ('term -> term POWER factor','term',3,'p_term_exponente','parserCop.py',238),
  ('term -> term DIVIDE factor','term',3,'p_term_div','parserCop.py',243),
  ('term -> term MODULE factor','term',3,'p_term_mod','parserCop.py',248),
  ('term -> term WHOLEDIVIDE factor','term',3,'p_term_wholediv','parserCop.py',253),
  ('term -> factor','term',1,'p_term_factor','parserCop.py',258),
  ('factor -> NUMBER','factor',1,'p_factor_num','parserCop.py',265),
  ('factor -> VAR','factor',1,'p_factor_var','parserCop.py',270),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','parserCop.py',276),
]
