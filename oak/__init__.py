from oak.utils import Position, Token
from oak.error import IllegalCharError

FLOAT, INTEGER, AS = 'FLOAT', 'INTEGER', 'AS'


def run(code, fn):
    lexer = Lexer(code, fn)
    tokens, _error = lexer.make_tokens()
    if _error: return None, _error
    return tokens, None


class Lexer:
    def __init__(self, code, fn):
        self.code = code
        self.fn = fn
        self.pos = Position(-1, 1, 0, fn)
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.code[self.pos.idx] if self.pos.idx < len(self.code) else None

    def make_tokens(self):
        tokens = []
        while self.current_char is not None:
            token, _error = self.get_next_token()
            if _error is None:
                if token is not None:
                    tokens.append(token)
            else:
                return [], _error
        return tokens, None

    def get_next_token(self):
        if self.current_char in ' \t':
            self.advance()
            return None, None
        elif self.current_char in ['+', '-', '*', '/', '(', ')']:
            token = Token(AS, str(self.current_char))
            self.advance()
            return token, None
        elif self.current_char.isdigit():
            return self.make_number()
        else:
            return None, IllegalCharError(self.current_char, self.pos)

    def make_number(self):
        digits = ''
        dot_count = 0
        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
            if self.current_char == '.':
                if dot_count >= 1: return None, IllegalCharError(self.current_char, self.pos)
                dot_count += 1
            digits += self.current_char
            self.advance()
        if dot_count == 0:
            return Token(INTEGER, int(digits)), None
        else:
            return Token(FLOAT, float(digits)), None
