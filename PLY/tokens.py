from matplotlib.ft2font import HORIZONTAL
from ply import lex
from ply import yacc

tokens = (
    'LITERAL',
    'HEADINGLINE',
    'QUOTELINE',
    'LISTLINE',
    'PARAGRAPHLINE',
    'TABLEDELIMINATORCELL',
    'OPEN_FENCE',
    'NEWLINE',
    'CELLTEXT',
    'BACKTICK',
    'GT',
    'HASH',
    'PIPE',
    'CELLCHAR',
    'ESCAPEDCHAR',
    'ALPHANUMERIC',
    'PUNCTUATION',
    'ESCAPEDPIPE',
    'WS',
    'LISTNUMBER',
    'BULLET',
    'INITIALPARACHAR',
    'LITERALCHAR',
    'LINECHAR',
    'CLOSE_FENCE',
    'TEXTLINE',
    'INITIALTEXTCHAR',
    'LINENUMBER',
    'IMPORT',
    'FROM',
    'TO',
    'STRING',
    'WORD',
    'FENCED_NEWLINE',
    'FENCED_IGNORE_WS',
    'DIGIT',
    'WORDCHAR',
    'TEXTCHAR',
    'IGNORE_WS',
)

t_LITERAL = r'BACKTICK?LITERALCHAR+?BACKTICK'
t_HEADINGLINE = r'HASH+?LINECHAR+'
t_QUOTELINE = r'GT?(LINECHAR+|LITERAL)+'
t_LISTLINE = r'WS*(BULLET|LISTNUMBER)WS+LINECHAR*'
t_PARAGRAPHLINE = r'INITIALPARACHAR(LINECHAR+|LITERAL)*'
t_TABLEDELIMINATORCELL = r'PIPE?:?-+:?'
t_OPEN_FENCE = r'```->mode(FENCED)'#
t_IGNORE_WS = r'WS->skip'#
t_NEWLINE = r'\r?\n'
t_CELLTEXT = r'PIPE IGNORE_WS(CELLCHAR+|LITERAL)*'
t_BACKTICK = r'`'
t_GT = r'>'
t_HASH = r'\#'
t_PIPE = r'\|'
t_CELLCHAR = r'(ESCAPEDCHAR|ESCAPEDPIPE|WS|ALPHANUMERIC|PUNCTUATION)'
t_ESCAPEDCHAR = r'\\'
t_ALPHANUMERIC = r'[a-zA-Z0-9]'
t_PUNCTUATION = r'[!"#$%&\'()*+,\-./:;<=>?@[\]^_{}]'
t_ESCAPEDPIPE = r'\|'
t_WS = r'\ '
t_LISTNUMBER = r'[1-9][.)]'
t_BULLET = r'[-+*]'
t_INITIALPARACHAR = r'~[#>|\n\r]'
t_LITERALCHAR = r'~[`]'
t_LINECHAR = r'~[\n\r`]'
t_CLOSE_FENCE = r'```(FENCED_NEWLINE|EOF)->mode(DEFAULT_MODE)'
t_TEXTLINE = r'INITIALTEXTCHAR TEXTCHAR*FENCED_NEWLINE'
t_INITIALTEXTCHAR = r'{_input.LA(-1) == 10|_input.LA(-1) == 13}?~[\n\r]'
t_LINENUMBER = r'DIGIT+'
t_IMPORT = r'import'
t_FROM = r'from'
t_TO = r'to|\-'
t_STRING = r'\'LINECHAR*?\''
t_WORD = r'WORDCHAR+'
t_FENCED_NEWLINE = r'\r?\n'
t_FENCED_IGNORE_WS = r'WS->skip' #
t_DIGIT = r'[0-9]'
t_WORDCHAR = r'~[\n\r\t |`]'
t_TEXTCHAR = r'~[\n\r]'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

data = '''
import
+ Create a list by starting a line with `+`, `-`, or `*`
+ Sub-lists are made by indenting 2 spaces:
  - Marker character change forces new list start:
    * Ac tristique libero volutpat at
      + Facilisis in pretium nisl aliquet
      - Nulla v

## Horizontal Rules

___

---

***

'''
# Give the lexer some input
lexer.input(data)
 
 # Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)