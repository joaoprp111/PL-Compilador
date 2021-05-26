#
# T = {
#     'START', 'END',
#     'INT', 'NUM','ID','ATRIB',
#     'ADD','SUB','MUL','DIV','MOD','EQ','DIFF','GRT','GEQ','LWR','LEQ',
#     'AND','OR','NOT','READ','WRITE','IF','THEN','ELSE','FOR','DO','(',')','{','}',';','-'
# }
#
#  Linguagem -> START Exp END
#
#
# Exp --> ADD '(' Content ')'
#      |  SUB '(' Content ')'
#      |  Termo
#
# Content -> Factor Factor
#          | Exp Termo
#
#
# Termo --> MUL '(' Content ')'
#        |  DIV '(' Content ')'
#        |  Factor
#
# Factor --> NUM
#
#
#
#
import ply.yacc as yacc
import sys

from compilador_lex import tokens

#Produção da linguagem
def p_Linguagem(p):
    "Linguagem : START Exp END"
    p[0] = 'START\n' + p[2] + 'STOP\n'


#Produções Exp
def p_Exp_add(p):
    "Exp : ADD '(' Content ')'"
    p[0] = p[3] + 'ADD\n'

def p_Exp_sub(p):
    "Exp : SUB '(' Content ')'"
    p[0] = p[3] + 'SUB\n'

def p_Exp_Termo(p):
    "Exp : Termo"
    p[0] = p[1]

#Produções Content
def p_Content_Factors(p):
    "Content : Factor Factor"
    p[0] = 'PUSHI ' + p[1] + '\n' + 'PUSHI ' + p[2] + '\n'

def p_Content_ExpTerm(p):
    "Content : Exp Termo"
    p[0] = p[1] + p[2]

#Produções Termo
def p_Termo_mul(p):
    "Termo : MUL '(' Content ')'"
    p[0] = p[3] + 'MUL\n'

def p_Termo_div(p):
    "Termo : DIV '(' Content ')'"
    p[0] = p[3] + 'DIV\n'
    # if(p[4] != 0):
    #     p[0] = p[3] / p[4]
    # else:
    #     print('Erro: divisão por 0. A continuar com o dividendo: ',p[3])
    #     p[0] = p[3]

def p_Termo_factor(p):
    "Termo : Factor"
    p[0] = p[1]

#Produções Factor
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
for linha in sys.stdin:
    result = parser.parse(linha)
    print(result)
