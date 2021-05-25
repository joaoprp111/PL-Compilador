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
# Exp --> ADD Termo Exp
#      |  SUB Termo Exp
#      |  Termo
#
# Termo --> MUL Termo Factor
#        |  DIV Termo Factor
#        |  Factor
#
# Factor --> '(' Exp ')'
#         |   NUM
#         |   '-' NUM
#
#
#
#
import ply.yacc as yacc
import sys

from compilador_lex import tokens

# def p_Comando_write(p):
#     "Comando : '(' READ id ')'"
#     valor = input("Introduza um valor inteiro: ")
#     p.parser.registers.update({p[3]: int(valor)})
#
# def p_Comando_read(p):
#     "Comando : '(' PRINT Exp ')'"
#     print(p[3])
#
# def p_Comando_atrib(p):
#     "Comando : '(' SET id Exp ')'"
#     p.parser.registers.update({p[3]: p[4]})
#
# def p_Comando_despejar(p):
#     "Comando : DUMP"
#     print(p.parser.registers)

def p_Linguagem(p):
    "Linguagem : START Exp END"
    p[0] = 'START\n' + p[2] + 'STOP\n'

def p_Exp_add(p):
    "Exp : ADD '(' Exp Termo ')'"
    p[0] = 'PUSHI ' + p[3] + '\n' + 'PUSHI ' + p[4] + '\n' + 'ADD\n'

def p_Exp_sub(p):
    "Exp : SUB '(' Exp Termo ')'"
    p[0] = 'PUSHI ' + p[3] + '\n' + 'PUSHI ' + p[4] + '\n' + 'SUB\n'

def p_Exp_termo(p):
    "Exp : Termo"
    p[0] = p[1]

def p_Termo_mul(p):
    "Termo : MUL '(' Termo Factor ')'"
    p[0] = 'PUSHI ' + p[3] + '\n' + 'PUSHI ' + p[4] + '\n' + 'MUL\n'

def p_Termo_div(p):
    "Termo : DIV '(' Termo Factor ')'"
    p[0] = 'PUSHI ' + p[3] + '\n' + 'PUSHI ' + p[4] + '\n' + 'DIV\n'
    # if(p[4] != 0):
    #     p[0] = p[3] / p[4]
    # else:
    #     print('Erro: divisão por 0. A continuar com o dividendo: ',p[3])
    #     p[0] = p[3]

def p_Termo_factor(p):
    "Termo : Factor"
    p[0] = p[1]

def p_Factor_group(p):
    "Factor : '(' Exp ')'"
    p[0] = p[2]

def p_Factor_num(p):
    "Factor : NUM"
    p[0] = p[1]

# def p_Factor_id(p):
#     "Factor : id"
#     p[0] = p.parser.registers.get(p[1])

# def p_Factor_negativo(p):
#     "Factor : '-' NUM"
#     p[0] = int(p[1] + p[2])

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
