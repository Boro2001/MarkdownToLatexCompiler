from ply import lex
from ply import yacc


def p_document(p):
    "block+ EOF"


def p_block(p):
     """heading |
        paragraph |
        list |
        blockquote |
        fencedcodeblock |
        table |
        NEWLINE"""


def p_heading(p):
    "NEWLINE* HEADINGLINE NEWLINE"


def p_paragraph(p):
    "NEWLINE* paragraphline+"


def p_paragraphline(p):
    """PARAGRAPHLINE
    (
        NEWLINE |
        EOF
    )"""


def p_list(p):
    "NEWLINE* listline+"


def p_listline(p):
    """LISTLINE
    (
        NEWLINE |
        EOF
    )"""


def p_blockquote(p):
    "NEWLINE* quoteline+"


def p_quoteline(p):
    """QUOTELINE
    (
        NEWLINE |
        EOF
    )"""


def p_fencedcodeblock(p):
    """OPEN_FENCT infostring? FENCRD_IGNORE_WS? importspec? FENCED_NEWLINE
    textline*
    CLOSE_FENCE"""


def p_textline(p):
    "TEXTLINE"


def p_infostring(p):
    "WORD"


def p_importspec(p):
    "IMPORT FENCED_INGORE_WS? path FENCED_IGNORE_WS? (start FENCED_IGNORE_WS? end?)?"


def p_path(p):
    "WORD | STRING"


def p_start(p):
    "FROM? FENCED_IGNORE_WS? location"


def p_end(p):
    "TO FENCED_IGNORE_WS? location"


def p_location(p):
    "LINENUMBER | STRING"


def p_table(p):
    "NEWLINE* tableheading tabledelimiterrow tablerow+"


def p_tableheading(p):
    "tablerow"


def p_tablerow(p):
    """cell+ PIPE?
    (
        NEWLINNE |
        EOF
    )"""


def p_cell(p):
    "CELLTEXT"


def p_tabledelimiterrow(p):
    "TABLEDELIMINATORCELL+ PIPE? NEWLINE"