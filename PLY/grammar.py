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
    'LITERALCHAR',  # ' <- ten jest do nawiasów
    'FLOOR', # _
    'LEFTBRACKET',  # [
    'RIGHTBRACKET',  # ]
    'LEFTMBRACKET',  # {
    'RIGHTMBRACKET'  # }
    )

t_NEWLINE = r'\n'
t_BACKTICK = r'`'
t_GT = r'>'
t_HASH = r'\#'
t_PIPE = r'\|'
t_SLASH = r'\\'
t_ALPHANUMERIC = r'[a-zA-Z0-9]'
t_PUNCTUATION = r'[!"$%&,./:;\-<=?@^{}]'
t_WS = r'\ '
t_BULLET = r'\*'
t_LITERALCHAR = r'\''
t_FLOOR = r'_'
t_LEFTBRACKET = r'\['
t_RIGHTBRACKET = r'\]'
t_LEFTMBRACKET = r'\('
t_RIGHTMBRACKET = r'\)'

# /TOKENS


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# GRAMMAR
def p_document(p):
    """document : block
                | document block
    """
    if len(p) == 2:
        p[0] = """\\documentclass{article}\\usepackage{array, makecell}\\usepackage[utf8]{inputenc}\\usepackage{hyperref}\\begin{document}\\newenvironment{amazingtabular}{\\begin{tabular}{*{30}{|l}}}{\\end{tabular}}\n""" + p[1] + "\\end{document}"
    elif len(p) == 3:
        p[0] =  p[1][:-14] + p[2] + "\\end{document}"
    else:
        print("Document wrong argument length")

def p_block(p):
    """
    block : heading
    | subheading
    | subsubheading
    | quote
    | bulletitem
    | code
    | paragraph
    | urllink
    | heading NEWLINE
    | quote NEWLINE
    | bulletitem NEWLINE
    | code NEWLINE
    | paragraph NEWLINE
    | urllink NEWLINE
    | enumeratedlist NEWLINE
    | list NEWLINE
    | table
    | pipeline NEWLINE
    | table NEWLINE
    """
    p[0] = p[1]

def p_heading(p):
    """
    heading : HASH sentence NEWLINE
    """
    p[0] = "\\section*{" + p[2] + "}\n"

def p_subheading(p):
    """
    subheading : HASH HASH sentence NEWLINE
    """
    p[0] = "\\subsection*{" + p[3] + "}\n"

def p_subsubheading(p):
    """
    subsubheading : HASH HASH HASH sentence NEWLINE
    """
    p[0] = "\\subsubsection*{" + p[4] + "}\n"

def p_bulletitem(p):
    """
    bulletitem : BULLET sentence NEWLINE
    """
    p[0] = "\\begin{bulletitem} " + p[2] + "\\end{bulletitem}\n"

def p_bolditem(p):
    """
    bolditem : BULLET sentence BULLET
    | FLOOR sentence FLOOR
    """
    p[0] = "\\textbf{" + p[2] + "}"

def p_italicitem(p):
    """
    italicitem : BULLET BULLET sentence BULLET BULLET
    | FLOOR FLOOR sentence FLOOR FLOOR
    """
    p[0] = "\\textit{" + p[3] + "}"

def p_listelement(p):
    """
    listelement : PUNCTUATION WS sentence NEWLINE
    """
    p[0] = "\\item " + p[3] + "\n"

def p_enumeratedlistelement(p):
    """
    enumeratedlistelement :  ALPHANUMERIC PUNCTUATION WS sentence NEWLINE
    """
    p[0] = "\\item " +  p[4] + "\n"

def p_list(p):
    """
    list : listelement
    | list listelement
    """
    try:
        p[0] = "\\begin{itemize}\n" + p[1][16:-14] + p[2] + "\\end{itemize}\n"
    except:
        p[0] = "\\begin{itemize}\n" + p[1] + "\\end{itemize}\n"
        
def p_enumeratedlist(p):
    """
    enumeratedlist : enumeratedlistelement
                    | enumeratedlist enumeratedlistelement
    """
    try:
        p[0] = "\\begin{enumerate}\n" + p[1][18:-16] + p[2] + "\\end{enumerate}\n"
    except:
        p[0] = "\\begin{enumerate}\n" + p[1] + "\\end{enumerate}\n"

def p_urllink(p):
    """
    urllink : LEFTBRACKET sentence RIGHTBRACKET LEFTMBRACKET sentence RIGHTMBRACKET NEWLINE
    """
    p[0] = "\\href{" + p[5] + "}{" + p[2] + "}\n"

def p_quote(p):
    """
    quote : GT sentence NEWLINE
    """
    p[0] = "\\begin{quote}" + p[2] + "\\end{quote}\n"
    
def p_word(p):
    """
        word : ALPHANUMERIC
            | word ALPHANUMERIC
            | PUNCTUATION
            | word PUNCTUATION
            | ALPHANUMERIC WS
            | word WS

    """
    try:
        p[0] = p[1] + p[2]
    except:
        p[0] = p[1]

def p_sentence(p):
    """
    sentence : word
    | sentence WS word
    | sentence WS

    """
    try:
        p[0] = p[1] + " " + p[3]
    except:
        p[0] = p[1]

def p_paragraph(p):
    """
    paragraph : sentence
    | paragraph NEWLINE sentence
    | bolditem
    | paragraph NEWLINE bolditem
    | italicitem
    | paragraph NEWLINE italicitem
    | paragraph WS sentence
    | paragraph WS bolditem
    | paragraph WS italicitem
    | paragraph WS WS sentence
    | paragraph WS WS bolditem
    | paragraph WS WS italicitem
    | paragraph WS WS NEWLINE sentence
    | paragraph WS WS NEWLINE bolditem
    | paragraph WS WS NEWLINE italicitem
    | paragraph WS WS NEWLINE
    """


    if len(p) == 4:
        p[0] = p[1] + " " + p[3]
    elif len(p) == 2:
        p[0] = p[1] #+ "\\newline "
    elif len(p) == 5:
        p[0] = p[1] + "\\newline " + p[4]
    else: # len = 6
        p[0] = p[1] + "\\newline " + p[5]
    # p[0] = "\\paragraph{" + p[1] + "}\n"
"""
       paragraph : sentence NEWLINE
       | sentence

       | paragraph NEWLINE sentence
       | bolditem NEWLINE
       | paragraph NEWLINE bolditem
       | italicitem NEWLINE
       | paragraph NEWLINE italicitem
       | paragraph WS sentence
       | bolditem WS
       | paragraph WS bolditem
       | italicitem WS
       | paragraph WS italicitem
"""

"""
    | sentence NEWLINE paragraph
    | bolditem NEWLINE
    | bolditem NEWLINE paragraph
    | italicitem NEWLINE
    | italicitem NEWLINE paragraph
    | sentence WS paragraph
    | bolditem WS paragraph
    | italicitem WS paragraph
"""


def p_code(p):
    """
    code : BACKTICK BACKTICK BACKTICK NEWLINE paragraph BACKTICK BACKTICK BACKTICK
    """
    p[0] = "\\begin{code}\n" + p[5] + "\\end{code}\n"

def p_tablerow(p):
    """
    tablerow : PIPE sentence PIPE NEWLINE
    | PIPE sentence tablerow
    """ 
    if(len(p)==5):
        p[0] = " " + p[2] + "\\\\ \\hline\n"
    else:
        p[0] = " " + p[2] + " &" + p[3]

    
def p_table(p):
    """
    table : table tablerow
    | tablerow
    """
    try:
        x = p[2]
        p[0] = p[1][:-30] + p[2] + "\\end{amazingtabular}\n\\newline "
        delimeter = True
        for letter in p[2][:-11]:
            if letter not in " -&":
                delimeter = False
        if delimeter:
            p[0] = p[1]
    except:

        elems = p[1].split("&")
        elems[-1] = elems[-1][:-10]
        for i in range(len(elems)):
            elems[i] = "\\thead{" + elems[i] + "}"
        out = str.join("&", elems)
        p[0] = "\\begin{amazingtabular}\\hline" + out + "\\\\ \hline\\end{amazingtabular}\n\\newline " # uncommed this later

# def p_minusline(p):
#     """
#     minusline : MINUS
#     """
#     p[0] = ""
#
def p_pipeline(p):
    """
    pipeline : PIPE PIPE
    | pipeline PIPE
    """
    p[0] = "\\hline\n"

# def tabledelimeter(p):
#     """
#     tabledelimeter : PIPE tabledelimetercell
#     tabledelimeter : tabledelimeter tabledelimetercell
#     """
#     p[0] = "\\hline\n"
#
# def tabledelimetercell(p):
#     """
#     tabledelimetercell : MINUS PIPE
#     tabledelimetercell : MINUS tabledelimetercell
#     """
#     p[0] = ""

# /GRAMMAR


data = """normal text *bold text* some text __second bold or italic text__  
|pierwszy|drugi|trzeci|
|---|---|---|
|323|fdf33 fd|fdf3 3 3|
|dsd lskds l|d sldkhjhjhj hjs dls|d hj hj hkslkl|
zdanie ostatnie
#heading

1. pierwszy element
2. drugi element
3. trzeci element

"""


"""ala ma kota
|pierwszy|drugi|trzeci|
|---|---|---|
|323|fdf33 fd|fdf3 3 3|
|dsd lskds l|d sldkhjhjhj hjs dls|d hj hj hkslkl|
kot ma ale
"""
"""[link do internetu](http://www.overleaf.com)
ala ma kota
kot ma ale

#heading
##subheading
###subsubheading
ostatnia linia

1. pierwszy element
2. drugi element
3. trzeci element

- pierwszy element
- drugi element
- trzeci element
"""


def p_error(p):

    # get formatted representation of stack
    stack_state_str = ' '.join([symbol.type for symbol in parser.symstack][1:])

    print('Syntax error in input! Parser State:{} {} . {}'
          .format(parser.state,
                  stack_state_str,
                  p))# lexowanie
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

print("ENDDD")

def get_parser():
    parser2 = yacc.yacc()
    return parser2


