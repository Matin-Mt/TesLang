from lexer import Lexer

lex = Lexer(
"""
a::int=2;
a:: str = 'my 9string value';
b:: str = 8sa;"""
)

lex.run()
