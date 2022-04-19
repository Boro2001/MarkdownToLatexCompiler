
class Lexer:
    single_starting_tokens = ['#', '##', '###', '####', '#####', '######', '---', '***', '>', '+', '-', '*']
    double_tokens = ['**', '__', '*', '_']

    def lex(self, input_expression):
        # TODO: debug this function
        type_o_matching = None
        left_token = None
        last_token = -1
        result = ''
        expression = input_expression.split(" ")
        while ("" in expression):
            expression.remove("")
        #print(expression)
        for i, token in enumerate(expression):
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
                    last_token = i
                    # print(i)
                    break

            if type_o_matching == 1:
                if token == '\n':
                    last_token = i
                    # print(i)
                    break

            if type_o_matching == 2:
                if token == left_token:
                    last_token = i
                    break

        result = result.split()
        left_token, right_token, middle_string = None, None, None
        # lewy token
        if type_o_matching == 0:
            left_token = '\n'
        else:
            left_token = result[0]
        # prawy token
        if type_o_matching == 0 or type_o_matching == 1:
            right_token = '\n'
        else:
            right_token = left_token
        # middle
        if type_o_matching == 0:
            middle_string = ' '.join(result[:last_token])
        if type_o_matching == 1:
            middle_string = ' '.join(result[1:])
        if type_o_matching == 2:
            middle_string = ' '.join(result[1:-1])
        # leftovers

        leftover_string = None
        leftover_string = expression[last_token+1:]
        leftover_string = " ".join(leftover_string)

        if last_token == len(expression)-1:
            leftover_string = None
        if last_token == -1:
            leftover_string = None
        return left_token, middle_string, right_token, leftover_string


lexer = Lexer
print(lexer.lex(lexer, "  raz dwa trzy \n"))
print(lexer.lex(lexer, "  raz dwa ## \n ##  se "))
print(lexer.lex(lexer, " ##  raz dwa ##  trzy  cztery "))
print(lexer.lex(lexer, " **  raz dwa ** trzy  cztery "))
print(lexer.lex(lexer, " ### raz dwa \n "))
print(lexer.lex(lexer, " ### raz dwa "))
