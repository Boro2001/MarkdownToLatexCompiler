from ply import yacc
from ply import lex


# TOKENS
tokens = (
    'NEWLINE', #\n
    'BACKTICK', #` <- ten jest do kodu
    'GT', #>
    'HASH', #
    'PIPE', #|
    'SLASH', # \\
    'ALPHANUMERIC', # a-zA-Z0-9
    'PUNCTUATION', # ale nie moze byc # | > ` \ '
    'WS', # whitespace
    'BULLET', # * 
    'LITERALCHAR' # ' <- ten jest do nawiasów

)
t_NEWLINE = r'\n'
t_BACKTICK = r'`'
t_GT = r'>'
t_HASH = r'\#'
t_PIPE = r'\|'
t_SLASH = r'\\'
t_ALPHANUMERIC = r'[a-zA-Z0-9]'
t_PUNCTUATION = r'[!"$%&(),-./:;<=?@^_{}]'
t_WS = r'\ '
t_BULLET = r'\*'
t_LITERALCHAR = r'\''
# /TOKENS

# GRAMMAR
def p_document(p):
    """document : block
                | block document"""
    if len(p) == 2:
        p[0] = "\\begin{document}" + p[1] + "\\end{document}"
    elif len(p) == 3:
        p[0] = "\\begin{document}" + p[1] + p[2][17:-15] + "\\end{document}"
    else:
        print("Document wrong argument lenght")

def p_block(p):
    """
    block : heading
    | quote
    | bulletitem
    """
    p[0] = p[1]

def p_heading(p):
    """
    heading : HASH sentence NEWLINE
    """
    p[0] = "\\begin{heading}" + p[2] + "\\end{heading}"

def p_bulletitem(p):
    """
    bulletitem : BULLET sentence NEWLINE
    """
    p[0] = "\\begin{bulletitem} " + p[2] + "\\end{bulletitem}"

def p_quote(p):
    """
    quote : GT sentence NEWLINE
    """
    p[0] = "\\begin{quote}" + p[2] + "\\end{quote}"
    
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
    | word WS sentence
    """
    try:
        p[0] = "word{" + p[1] + "}" + p[3]
    except:
        p[0] = "word{" + p[1] + "}"

#/GRAMMAR
data = """#Heading\n\n#Heading2\n\n>Jebanie dziada\n\n*Jebanie baby\n\n"""

#lexowanie
lexer = lex.lex()
lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)



#parsowanie
parser = yacc.yacc()
try:
    s = data
except EOFError:
    pass
if not s:
    pass
result = parser.parse(s)
print(result)
