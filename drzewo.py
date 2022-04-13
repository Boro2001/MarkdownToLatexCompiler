import lexer

class Drzewo:
    def __init__(self):
        root = None

    def build_tree(self, uncompiled_text):
        #TODO make function to build a tree
        root = Node(None, uncompiled_text, None)
        
        
        #lexer = Lexer()
        #root_data = lexer.lex(uncompiled_text)
        #root = Node(root_data[0], root_data[1], root_data[2])
        #root.fill_children(root_data[3])
        
        
        
        pass

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


class Lexer:
    single_starting_tokens = ['#', '##', '###', '####','#####', '######', '---', '***', '>','+','-','*','']
    double_tokens = ['**', '__', '*', '_']

    def lex(self, str):
        #TODO: debug this function
        type_o_matching = None
        left_token = None
        last_token = -1
        result = ''
        expression = str.split()
        print(expression)

        for i,token in enumerate(expression):
            result = result + " " + token
            
            if type_o_matching is None:
                type_o_matching = 0
                if token in self.single_starting_tokens:
                    type_o_matching = 1
                if token in self.double_tokens:
                    left_token = token
                    type_o_matching = 2
                continue

            if type_o_matching == 0:
                if token == '\n':
                    print(result)
                    last_token = i
                    break                    
                    
            if type_o_matching == 1:
                if token == '\n':
                    print(result)
                    last_token = i
                    break
                    
            if type_o_matching == 2:
                if token == left_token:
                    print(result)
                    last_token = i
                    break
        leftovers = expression[last_token+1:]
        print(type_o_matching)
        result = result.split()
        return (result[0], ' '.join(result[1:-1]), result[-1]," ".join(leftovers))

lexer = Lexer()
#print(lexer.lex("** uhafiefuh ahw uiehiuhw ** i# # \n ## "))
tree = Drzewo()
tree.build_tree("** uhafiefuh ahw uiehiuhw ** i# # \n ## ")





