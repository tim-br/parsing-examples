import io
import string
from tokenizer import Tokenizer


class SimpleExpressionParser:
    def __init__(self, text):
        self.tokenizer = Tokenizer(io.StringIO(text))

    def parse_expression(self):
        # This method should handle addition and subtraction
        self.parse_term()

    def parse_term(self):
        # This method should handle multiplication and division
        if(not self.tokenizer.current_char):
            self.tokenizer.advance(True)

        left = self.parse_factor()
        self.tokenizer.advance(True)
        if(self.tokenizer.current_char == '*'):
            self.tokenizer.advance(True)
        if(not self.tokenizer.current_char):
            return left
        else:
            right = self.parse_factor()
            return left * right

    def parse_factor(self):
        # This method should handle parentheses and numbers
        
        if(self.tokenizer.current_char and self.tokenizer.current_char == '('):
            ## return self.parse_number()
            self.tokenizer.advance(True)
             ##return self.parse_factor()
            return self.parse_term()
        
        if(self.tokenizer.current_char.isdigit() ):
            re = self.parse_number()
            while(self.tokenizer.current_char and self.tokenizer.current_char == ')'):
                self.tokenizer.advance(True)
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


##expression = "23232 * (3 + 4) - 5"
#expression = '1234'
#parser = SimpleExpressionParser(expression)
#print(parser.parse_number())
#expression = '(12934)'
#parser = SimpleExpressionParser(expression)
#print(parser.parse_factor())

expression = '(12934)'
parser = SimpleExpressionParser(expression)
expression = '(129 * 34)'
parser = SimpleExpressionParser(expression)
expression = '(2 *  (129 * 34))'
parser = SimpleExpressionParser(expression)
print(parser.parse_term())

expression = '( (2 *  (129 * 34)) * 2)'
parser = SimpleExpressionParser(expression)
print(parser.parse_term())
