# -----------------------------------------------
# lexer.py
# tokenizer for the cool language.
import ply.lex as lex

# reserved for cool
reserved = ( 'class',
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

tokens = reserved + ( 'INTEGER',
                    'ID',
                    'PLUS',
                    'MINUS',
                    'TIMES',
                    'DIVIDE',
                    'EQUAL',
                    'LPAREN',
                    'RPAREN',
                    'LBRACE',
                    'RBRACE',
                    'SEMICOLON',
                    'ASSIGN',
                    'COLON',
                    'LANGLE',
                    'RANGLE',
                    'COMMA',
                    'DOT',
                    'STRING',
                    'TILDA',
                    'ATRATE',
                    )

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUAL = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_COLON = r':'
t_ASSIGN = r'<-'
t_LANGLE = r'<'
t_RANGLE = r'>'
t_COMMA = r','
t_DOT = '\.'
t_TILDA = '~'
t_ATRATE = '@'

def t_STRING(t):
    r'"[^"]*"'
    t.type = 'STRING'
    t.value = t.value[1:-1]
    return t
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reserved:
        t.type = t.value
    else:
        t.type = 'ID'
    return t
def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t



# Define a rule to track line numbers
def t_newline(t):
    r'\n+'
    #print 'new line found'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t\r'
#t_ignore_carriage = '\r'
t_ignore_COMMENT_SINGLE_LINE = r'--.*(?:--|[^\n])'
t_ignore_COMMENT_MULTILINE = r'\(\*(?:.|\n)*\*\)'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    print "Ascii code '%s'" % ord(t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

#Test it out
import sys
f = open(sys.argv[1])
data = "".join(f.readlines())
if __name__ == "__main__":

    lexer.input(data)
    # Tokenize
    while True:
	    tok = lexer.token()
	    if not tok: break #No more input
	    print tok#tok.type, tok.value, tok.line, tok.lexpos


