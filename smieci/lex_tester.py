from smieci.lexer import Lexer
import pytest

class test:
    def __init__(sef, input, left, middle, righ, leftovers):
        lexer = Lexer
        test1 = lexer.lex(lexer, input)
        assert test1[0] == left
        assert test1[1] == middle
        assert test1[2] == righ
        assert test1[3] == leftovers           


lexer = Lexer


test("fh**####fihauwhf+__*****", "\n", "fh**####fihauwhf+__*****", "\n", None)
test("  raz dwa ## \n ##  se ", "\n", "raz dwa ##", "\n", "## se")

print(lexer.lex(lexer, "fh**####fihauwhf+__*****"))
print(lexer.lex(lexer, "  raz dwa ## \n ##  se "))
print(lexer.lex(lexer, " ##  raz dwa ##  trzy  cztery "))
print(lexer.lex(lexer, " **  raz dwa ** trzy  cztery "))
print(lexer.lex(lexer, " ### raz dwa \n "))
print(lexer.lex(lexer, " ### raz dwa "))
print(lexer.lex(lexer, "    awjij ai jwj iaj iw ### ** **  juish uhes uu \n  auh iauhw ihuiwhi"))
print(lexer.lex(lexer, " __ jaoi jeioa j \n __ hello leftovers "))
print(lexer.lex(lexer, " jaoijeioa __ hell leftovers "))
print(lexer.lex(lexer, " ** __ jaoijeioa __ hell leftovers  a ** "))
print(lexer.lex(lexer, " ** __ halla B00nger __ ** "))
print(lexer.lex(lexer, " *** aij iah ehaehui \n\n\n\n\n\n.*####***  "))