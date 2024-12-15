import re


class Token:
    tokens = (
        'ID', 'ILLIGAL_ID', 'ASSIGNMENT', 'COMMENT', 'NON_ID_VALUE',
        'COLON', 'DOUBLE_COLON', 'SEMI_COLON', 'COMMA',
        'EQUAL', 'NOT_EQUAL', 'GREATER', 'GREATER_EQUAL', 'LOWER', 'LOWER_EQUAL',
        'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MODULUS',
        'PLUS_EQ', 'MINUS_EQ', 'TIMES_EQ', 'DIVIDE_EQ', 'MODULUS_EQ',
        'SINGLE_QUOTE', 'DOUBLE_QUOTE',
        'L_PAREN', 'R_PAREN', 'L_CURL', 'R_CURL', 'L_BRACK', 'R_BRACK',
        'DOUBLE_L_BRACK', 'DOUBLE_R_BRACK',
        'STRING', 'INT', 'BOOLEAN', 'VECTOR', 
        'FN', 'RETURN', 'VOID', 'AS', 
        'FOR', 'TO', 'BEGIN', 'END', 'IF', 'ELSE', 'ARROW',
        'SCAN_FN', 'LIST_FN', 'PRINT_FN', 'LENGTH_FN', 'EXIT_FN',
    )
    
    t_COLON = r':'
    t_DOUBLE_COLON = r'::'
    t_SEMI_COLON = r';'
    t_COMMA = r','
    
    t_ARROW = r'=>'
    
    t_ASSIGNMENT = r'='
    t_EQUAL = r'=='
    t_NOT_EQUAL = r'!='
    t_GREATER = r'>'
    t_GREATER_EQUAL = r'>='
    t_LOWER = r'<'
    t_LOWER_EQUAL = r'<='

    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_MODULUS = r'%'
    
    t_PLUS_EQ = r'\+='
    t_MINUS_EQ = r'-='
    t_TIMES_EQ = r'\*='
    t_DIVIDE_EQ = r'/='
    t_MODULUS_EQ = r'%='
    
    t_SINGLE_QUOTE = r'\''
    t_DOUBLE_QUOTE = r'\'\''
    
    t_L_PAREN = r'\('
    t_R_PAREN = r'\)'
    t_L_CURL = r'\{'
    t_R_CURL = r'\}'
    
    t_L_BRACK = r'\['
    t_R_BRACK = r'\]'
    t_DOUBLE_L_BRACK = r'\[\['
    t_DOUBLE_R_BRACK = r'\]\]'
    
    t_STRING = r'str'
    t_INT = r'int'
    t_BOOLEAN = r'boolean'
    t_VECTOR = r'vector'
    
    t_FN = r'fn'
    t_RETURN = r'return'
    t_VOID = r'void'
    t_AS = r'as'
        
    t_FOR = r'for'
    t_TO = r'to'
    t_BEGIN = r'begin'
    t_END = r'end'
    t_IF = r'if'
    t_ELSE = r'else'
    
    t_SCAN_FN = r'scan'
    t_LIST_FN = r'list'
    t_PRINT_FN = r'print'
    t_LENGTH_FN = r'length'
    t_EXIT_FN = r'exit'

    t_ignore = ' \t'
    
    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        
        kw = {
            'str': 'STRING',
            'int': 'INT',
            'vector': 'VECTOR',
            'boolean': 'BOOLEAN',
            'fn': 'FN',
            'return': 'RETURN',
            'void': 'VOID',
            'as': 'AS',
            'for': 'FOR',
            'to': 'TO',
            'begin': 'BEGIN',
            'end': 'END',
            'if': 'IF',
            'scan': 'SCAN_FN',
            'list': 'LIST_FN',
            'print': 'PRINT_FN',
            'lenght': 'LENGTH_FN',
            'exit': 'EXIT_FN',
        }
        t.type = kw.get(t.value, 'ID')
        return t

    def t_ILLIGAL_ID(self, t):
        r'[0-9][a-zA-Z_][a-zA-Z0-9_]*'
        return t
    
    def t_COMMENT(self, t):
        r'<%(.)*%>'
        return

    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
    
    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
    