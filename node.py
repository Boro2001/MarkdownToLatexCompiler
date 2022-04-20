from lexer import Lexer
class Node:
    childen = []
    left = None
    right = None
    middle = None

    def __init__(self, left, middle, right):
        self.left = left
        self.right = right
        self.middle = middle
        self.fill_children(middle)

    def fill_children(self, str):
        lexer = Lexer()
        leftovers = str
        while leftovers != None:
            result = lexer.lex(leftovers)
            leftovers = result[3]
            self.childen.append(Node(result[0], result[1], result[2]))

        pass