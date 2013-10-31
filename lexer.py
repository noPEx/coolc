# -----------------------------------------------
# lexer.py
# tokenizer for the cool language.
import ply.lex as lex

# keywords for cool
keywords = ( 'class',
        'else',
        'false',
        'fi',
        'if',
        'in',
        'inherits',
        'isvoid',
        'let',
        'loop',
        'pool',
        'then',
        'while',
        'case',
        'esac',
        'new',
        'of',
        'not',
        'true', 
        )

tokens = keywords + ( 'INTEGER',
                    'PLUS',
                    'MINUS',
                    'TIMES',
                    'DIVIDE',
                    'LPAREN',
                    'RPAREN',
                    )

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()


#Test it out
data = '''hello
        I was here and
        now I am gone.'''

if __name__ == "__main__":

    lexer.input(data)
    # Tokenize
    while True:
	    tok = lexer.token()
	    if not tok: break #No more input
	    print tok.type, tok.value, tok.line, tok.lexpos

