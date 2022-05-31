from ply import lex
from ply import yacc


def p_document(p):
    "document : block+ EOF"
    p[0] = p[1]


def p_block(p):
    """block : heading |
        paragraph |
        list |
        blockquote |
        fencedcodeblock |
        table |
        NEWLINE"""
    p[0] = p[1]

def p_heading(p):
    "hediang : NEWLINE* HEADINGLINE NEWLINE"
    p[0] = "{\huge" + p[1] + "}"

def p_paragraph(p):
    "paragraph : NEWLINE* paragraphline+"


def p_paragraphline(p):
    """paragraph : PARAGRAPHLINE
    (
        NEWLINE |
        EOF
    )"""


def p_list(p):
    "list : NEWLINE* listline+"


def p_listline(p):
    """listline : LISTLINE
    (
        NEWLINE |
        EOF
    )"""


def p_blockquote(p):
    "blockquote : NEWLINE* quoteline+"


def p_quoteline(p):
    """quoteline : QUOTELINE
    (
        NEWLINE |
        EOF
    )"""


def p_fencedcodeblock(p):
    """fencedcodeblock : OPEN_FENCT infostring? FENCRD_IGNORE_WS? importspec? FENCED_NEWLINE
    textline*
    CLOSE_FENCE"""


def p_textline(p):
    "textline : TEXTLINE"


def p_infostring(p):
    "infostring : WORD"


def p_importspec(p):
    "importspec : IMPORT FENCED_INGORE_WS? path FENCED_IGNORE_WS? (start FENCED_IGNORE_WS? end?)?"


def p_path(p):
    "path : WORD | STRING"


def p_start(p):
    "start : FROM? FENCED_IGNORE_WS? location"


def p_end(p):
    "end : TO FENCED_IGNORE_WS? location"


def p_location(p):
    "location : LINENUMBER | STRING"


def p_table(p):
    "table : NEWLINE* tableheading tabledelimiterrow tablerow+"


def p_tableheading(p):
    "tableheading : tablerow"


def p_tablerow(p):
    """tablerow : cell+ PIPE?
    (
        NEWLINNE |
        EOF
    )"""


def p_cell(p):
    "cell : CELLTEXT"


def p_tabledelimiterrow(p):
    "tabledelimiterrow : TABLEDELIMINATORCELL+ PIPE? NEWLINE"