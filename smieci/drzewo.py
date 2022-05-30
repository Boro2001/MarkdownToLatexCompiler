from smieci.lexer import Lexer
from smieci.node import Node

class Drzewo:
    def __init__(self):
        root = None
        lexer = Lexer()
        

    def build_tree(self, uncompiled_text):
        #TODO make function to build a tree
        root = Node(None, uncompiled_text, None)
        
        
        #root_data = lexer.lex(uncompiled_text)
        #root = Node(root_data[0], root_data[1], root_data[2])
        #root.fill_children(root_data[3])
        
        pass





lexer = Lexer()
#print(lexer.lex("** uhafiefuh ahw uiehiuhw ** i# # \n ## "))
tree = Drzewo()
tree.build_tree("** uhafiefuh ahw uiehiuhw ** i# # \n ## ")





