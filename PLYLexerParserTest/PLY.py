# example parser for training
# tokenize sth like: 1 + 2 = 9 / 3

from ply import lex
from ply import yacc


tokens = (
    "NUMBER", "PLUS", "EQUAL", "DIVIDE", "MINUS", "MULTIPLY"
)

t_PLUS = r"[\+&]"
t_MINUS = r"\-"
t_DIVIDE = r"\/"
t_MULTIPLY = r"\*"
t_EQUAL = r"\="


def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

data = "1+26787868=967/&32"

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)


def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]


def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]


def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]


def p_error(p):
    print("Syntax error in input!")


parser = yacc.yacc()

while True:
    try:
        s = input(">>>")  # e. g. 19 + 2 - 10
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
