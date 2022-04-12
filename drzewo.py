import lexer

class Drzewo:
    def __init__(self):
        root = None

    def build_tree(self, uncompiled_text):
        #TODO make function to build a tree
        pass

class Node:
    childen = None
    left = None
    right = None
    middle = None

    def __init__(self, left, middle, right, children):
        self.left = left
        self.right = right
        self.middle = middle
        children = []

    def fill_children(self):
        #TODO make function to fill children
        pass


class Lexer:
    single_starting_tokens = ['#', '##', '###', '####','#####', '######', '---', '***', '>','+','-','*','']
    double_tokens = ['**', '__', '*', '_']

    def lex(self, str):
        #TODO: debud this function
        type_o_matching = None
        left_token = None
        nest_deep = 0
        result = ''
        expression = str.split()
        print(expression)

        for token in expression:
            result = result + " " + token
            if type_o_matching is None:
                if token in self.single_starting_tokens:
                    type_o_matching = 1
                if token in self.double_tokens:
                    left_token = token
                    type_o_matching = 2
                type_o_matching = 0
            if type_o_matching == 0:
                if token == '\n':
                    print(result)
            if type_o_matching == 1:
                if token == '\n':
                    print(result)
            if type_o_matching == 2:
                if token == left_token:
                    print(result)

        print(type_o_matching)

lexer = Lexer()
lexer.lex("# uhafiefuh ahw uiehiuhw i# #\n ## ")





