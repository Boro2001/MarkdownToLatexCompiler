from lexer import lex
from scanner import Scanner


class Compiler:
    filepath = "example.md"
    outfile = "out.tex"
    scanner = Scanner()

    def __init__(self, filepath, outfile):
        self.filepath = filepath
        self.outfile = outfile
        scanner = Scanner(filepath)

    def compile(self):
        uncompiled_text = self.scanner.scan()
        # czary mary




