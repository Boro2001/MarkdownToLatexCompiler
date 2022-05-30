from matplotlib.ft2font import HORIZONTAL


tokens = (
    NEWLINE,
    INDENT,
    TABLE,
    TEXT, 
    TABLESPLITTER,
    STRINGCHAR,
    TABCHAR,
    HEADING1,
    HEADING2,
    HEADING3,
    HEADING4,
    HEADING5,
    HEADING6,
    HORIZONTALLINE,
    BOLD,
    ITALIC,
    STRIKE,
    QUOTE,
    UNORDEREDLIST,
    ORDEREDLIST,
    CODE
)

t_HEADING1 = r"\#",
t_HEADING2 = r"\##",
t_HEADING3 = r"\###",
t_HEADING4 = r"\####",
t_HEADING5 = r"\#####"
t_HEADING6 = r"\######"

t_horizontalline = r"(---|\*\*\*|___)"

t_bold = r"(\*\*|__)"
t_italic = r"(\*|_)"

t_blockquotes = r">"
t_list = r"\+"
t_blocknode = r"```"



