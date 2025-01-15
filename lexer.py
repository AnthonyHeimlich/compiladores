import ply.lex as lex

tokens = [
    'NUMBER',    
    'PLUS',      
    'MINUS',     
    'MULTIPLY',  
    'DIVIDE',    
    'LPAREN',    
    'RPAREN'     
]

t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_NUMBER(t):    
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t' 

def t_error(t):
    print(f"Caracter inválido: {t.value[0]}")
    t.lexer.skip(1)

def build_lexer():
    return lex.lex()
