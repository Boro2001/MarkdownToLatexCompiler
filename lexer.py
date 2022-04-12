# based on:
# https://accu.org/journals/overload/26/145/balaam_2510/

import re


def lex(chars_iter):
    chars = PeekableStream(chars_iter)
    while chars.next is not None:
        c = chars.move_next()
        if c in " \n":
            # Ignore white space
            pass
        elif c in "#*_~":
            # Currently supports: heading, bold text, italic, crossed out text
            yield "symbol", _scan(c, chars, '[#*_~]')
        elif re.match("[_a-zA-Z0-9]", c):
            # Normal text (with spaces)
            yield "text", _scan(c, chars, "[_a-zA-Z0-9 ]")
        else:
            raise Exception(
                "Unexpected character: '" + c + "'.")


class PeekableStream:
    def __init__(self, iterator):
        self.iterator = iter(iterator)
        self._fill()

    def _fill(self):
        try:
            self.next = next(self.iterator)
        except StopIteration:
            self.next = None

    def move_next(self):
        ret = self.next
        self._fill()
        return ret


def _scan(first_char, chars, allowed):
    ret = first_char
    p = chars.next
    while p is not None and re.match(allowed, p):
        ret += chars.move_next()
        p = chars.next
    return ret


tokens = lex(""" 
** lala **
## sdad ola
3kl
~l~
""")

