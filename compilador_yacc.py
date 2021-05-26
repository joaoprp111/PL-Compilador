#
# T = {
#     'START', 'END',
#     'INT', 'NUM','ID','ATRIB',
#     'ADD','SUB','MUL','DIV','MOD','EQ','DIFF','GRT','GEQ','LWR','LEQ',
#     'AND','OR','NOT','READ','WRITE','IF','THEN','ELSE','FOR','DO','(',')','{','}',';','-'
# }
#
#  Linguagem -> START Instrs END
#
#  Instrs -> Exp
#          | WRITE '(' Exp ')'
#
# Exp --> ADD '(' Content ')'
#      |  SUB '(' Content ')'
#      |  Termo
#
# Content -> Exp Termo
#          | Factor Factor
#
#
# Termo --> MUL '(' Content ')'
#        |  DIV '(' Content ')'
#        |  MOD '(' Content ')'
#        |  Factor
#
# Factor --> '(' Exp ')'
#          |  NUM
#
#
#
#
import ply.yacc as yacc
import sys

from compilador_lex import tokens

#Produção da linguagem
def p_Linguagem(p):
    "Linguagem : START Instrs END"
    p[0] = 'START\n' + p[2] + '\n\nSTOP'


#Produções das instruções
def p_Instrs_Exp(p):
    "Instrs : Exp"
    p[0] = p[1]

def p_Instrs_write(p):
    "Instrs : WRITE Exp"
    p[0] = p[2] + '\nWRITEI'


#Produções Exp
def p_Exp_add(p):
    "Exp : ADD '(' Content ')'"
    p[0] = p[3] + '\nADD'

def p_Exp_sub(p):
    "Exp : SUB '(' Content ')'"
    p[0] = p[3] + '\nSUB'

def p_Exp_Termo(p):
    "Exp : Termo"
    p[0] = p[1]

#Produções Content
def p_Content_ExpTerm(p):
    "Content : Exp Termo"
    p[0] = p[1] + p[2]

def p_Content_Factors(p):
    "Content : Factor Factor"
    p[0] = '\nPUSHI ' + p[1] + '\nPUSHI ' + p[2]

#Produções Termo
def p_Termo_mul(p):
    "Termo : MUL '(' Content ')'"
    p[0] = p[3] + '\nMUL'

def p_Termo_div(p):
    "Termo : DIV '(' Content ')'"
    p[0] = p[3] + '\nDIV'
    # if(p[4] != 0):
    #     p[0] = p[3] / p[4]
    # else:
    #     print('Erro: divisão por 0. A continuar com o dividendo: ',p[3])
    #     p[0] = p[3]

def p_Termo_mod(p):
    "Termo : MOD '(' Content ')'"
    p[0] = p[3] + '\nMOD'

def p_Termo_factor(p):
    "Termo : Factor"
    p[0] = p[1]

#Produções Factor
def p_Factor_group(p):
    "Factor : '(' Exp ')'"
    p[0] = p[2]

def p_Factor_num(p):
    "Factor : NUM"
    p[0] = p[1]

# Error rule for syntax errors
def p_error(p):
    print('Syntax error in input: ', p)

# Build the parser
parser = yacc.yacc()

# Creating the model
# parser.registers = {}

# Read line from input and parse it
result = ""
for linha in sys.stdin:
    result += linha

result = parser.parse(result)
print(result)
