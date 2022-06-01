from ply import lex
from ply import yacc

tokens = (
    'ALPHANUMERIC',
    'SPACE',
    'NEWLINE',
    'COMMA',
    'HEADING1'
)


t_NEWLINE = r'\n'
t_SPACE = r'\ '
t_COMMA = r'.'
t_ALPHANUMERIC = r'[a-zA-Z0-9]'
t_HEADING1 = r'\n\#'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)



def p_document(p):
    """
    document : sentence
    """
    p[0] = "sentence{" + p[1] + "}"


def p_word(p):
    """
        word : ALPHANUMERIC
            | ALPHANUMERIC word
    """
    try:
        p[0] = p[1] + p[2]
    except:
        p[0] = p[1]




def p_sentence(p):
    """
    sentence : word NEWLINE
    | word SPACE sentence


    """

    try:
        p[0] = "word{" + p[1] + "}" + p[3]
    except:
        p[0] = "word{" + p[1] + "}"


def p_heading(p):
    """
    heading : HEADING1 sentence
    """
    p[0] = p[1] + p[2]


# def p_error(p):
#     print("Syntax error in input!")



lexer = lex.lex()
data = "ala je kota\n"
# Give the lexer some input
lexer.input(data)
parser = yacc.yacc()

while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)




try:
    s = data
except EOFError:
    pass
if not s:
    pass
result = parser.parse(s)
print(result)