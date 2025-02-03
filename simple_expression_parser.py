import io
import string
from tokenizer import Tokenizer


class SimpleExpressionParser:
    def __init__(self, text):
        self.tokenizer = Tokenizer(io.StringIO(text))
        c = self.tokenizer.reader.read(1)
        self.tokenizer.position = 1
        self.tokenizer.current_char = c

    def parse_expression(self):
        # This method should handle addition and subtraction
        self.parse_term()

    def parse_term(self):
        # This method should handle multiplication and division
        if self.tokenizer.current_char is not None and self.tokenizer.current_char.isspace():
            self.tokenizer.advance(True)

        left = self.parse_factor()
        result = left
        if(left is None):

            ##return
        #self.tokenizer.advance(True)
        multiply = None 

        while(not (left is None) and (not (self.tokenizer.current_char is None))): #and (not self.tokenizer.current_char.isspace())):
            if self.tokenizer.current_char is not None and self.tokenizer.current_char.isspace():
                self.tokenizer.advance(True)

            if(self.tokenizer.current_char == '*' or self.tokenizer.current_char == '/'):
                multiply = True if self.tokenizer.current_char == '*' else  False
                self.tokenizer.advance(True)
                parsed_factor = self.parse_factor()
                left = left * parsed_factor if multiply else left / parsed_factor

        return left

#        if(self.tokenizer.current_char == '*' or self.tokenizer.current_char == '/'):
#            multiply = True if self.tokenizer.current_char == '*' else False
#            self.tokenizer.advance(True)
#        #right = self.parse_term()
#        if(not (self.tokenizer.current_char is None)):
#            right = self.parse_factor()
#            if self.tokenizer.current_char is not None and self.tokenizer.current_char.isspace():
#                self.tokenizer.advance(True)
#
#            if multiply is None and self.tokenizer.current_char:
#                return self.parse_term() 
#            if multiply:
#                return left * right
#            else:
#                return left /  right
#
    def parse_factor(self):
        # This method should handle parentheses and numbers
        
        if(self.tokenizer.current_char and self.tokenizer.current_char == '('):
            ## return self.parse_number()
            self.tokenizer.advance(True)
             ##return self.parse_factor()
            return self.parse_term()
        
        if(self.tokenizer.current_char.isdigit() ):
            re = self.parse_number()
            if(self.tokenizer.current_char is not None and self.tokenizer.current_char == ')'):
                self.tokenizer.advance(False)
            return re

        

    def parse_number(self):
        # This method should parse and return a number
        term = 0
        while (self.tokenizer.current_char and self.tokenizer.current_char.isdigit()):
            intValue = ord(self.tokenizer.current_char) - ord('0')
            term = term * 10
            term += intValue
            self.tokenizer.advance(False)

        return term

expression = '2*3*4'
parser = SimpleExpressionParser(expression)
assert parser.parse_term() == 24

expression = '2 * 6 / 3'  # Nested parentheses
parser = SimpleExpressionParser(expression)
assert parser.parse_term() == 4.0 
expression = '(12934)'
parser = SimpleExpressionParser(expression)
assert parser.parse_term() == 12934
expression = '2 *  3 * 4'
parser = SimpleExpressionParser(expression)
assert parser.parse_term() == 24

##expression = "23232 * (3 + 4) - 5"
#expression = '1234'
#parser = SimpleExpressionParser(expression)
#expression = '(12934)'
#parser = SimpleExpressionParser(expression)


#expression = '(2 *  (129 * 34))'
#parser = SimpleExpressionParser(expression)
#assert parser.parse_term() == 8772
#
#expression = '( (2 *  (129 * 34)) * 2)'
#parser = SimpleExpressionParser(expression)
#assert parser.parse_term() == 17544
#
#expression = '(2 * (3 * 4)) * 5'
#parser = SimpleExpressionParser(expression)
#assert parser.parse_term() == 120
#
#expression = '2 * 3 * 4'  # Chain multiplication
#parser = SimpleExpressionParser(expression)
#assert parser.parse_term() == 24
#
#expression = '2 * (3 * 4)'  # Nested parentheses
#parser = SimpleExpressionParser(expression)
#assert parser.parse_term() == 24
#
#
#expression = '(10 / 2) * 3'  # Nested parentheses
#parser = SimpleExpressionParser(expression)
#print(parser.parse_term())
#print("X")
#expression = '10 * 2 / 5 * 3' # Nested parentheses
#parser = SimpleExpressionParser(expression)
#print(parser.parse_term())  # Should be 4 xpression = '2 * 6 / 3)'  # Nested parentheses
#
#expression = '2 * 6 / 3'  # Nested parentheses
#parser = SimpleExpressionParser(expression)
#print(parser.parse_term())  # Should be 4 xpression = '2 * 6 / 3)'  # Nested parentheses
