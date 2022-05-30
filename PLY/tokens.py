from matplotlib.ft2font import HORIZONTAL
from ply import lex
from ply import yacc

tokens = (
    'NEWLINE',
    'INDENT',
    'TABLE',
    'TEXT',
    'TABLESPLITTER',
    'STRINGCHAR',
    'TABCHAR',
    'HEADING1',
    'HEADING2',
    'HEADING3',
    'HEADING4',
    'HEADING5',
    'HEADING6',
    'HORIZONTALLINE',
    'BOLD',
    'ITALIC',
    'STRIKE',
    'QUOTE',
    'UNORDEREDLIST',
    'ORDEREDLIST',
    'CODE',
)

t_HEADING1 = r"\#"
t_HEADING2 = r"\#\#"
t_HEADING3 = r"\#\#\#"
t_HEADING4 = r"\#\#\#\#"
t_HEADING5 = r"\#\#\#\#\#"
t_HEADING6 = r"\#\#\#\#\#\#"
t_HORIZONTALLINE = r"(---|\*\*\*|___)"
t_BOLD = r"(\*\*|__)"
t_ITALIC = r"(\*|_)"
#t_BLOCKQUOTES = r">"
#t_LIST = r"\+"
#t_BLOCKNODE = r"```"
t_TEXT = r"[a-zA-z]+"
t_TABLESPLITTER = r"\|"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_STRINGCHAR(t):
    r'\d+'
    t.value = int(t.value)    
    return t


lexer = lex.lex()
parser = yacc.yacc()
