from lexer import Lexer

lexer = Lexer
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