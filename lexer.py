# -----------------------------------------------
# lexer.py
# tokenizer for the cool language.
import ply.lex as lex

# reserved for cool
reserved = { 'class':'CLASS',
        'else':'ELSE',
        'false':'FALSE',
        'fi':'FI',
        'if':'IF',
        'in':'IN',
        'inherits':'INHERITS',
        'isvoid':'ISVOID',
        'let':'LET',
        'loop':'LOOP',
        'pool':'POOL',
        'then':'THEN',
        'while':'WHILE',
        'case':'CASE',
        'esac':'ESAC',
        'new':'NEW',
        'of':'OF',
        'not':'NOT',
        'true':'TRUE', 
        }

tokens = list(reserved.values()) + [ 'INTEGER',
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
                    'LESSEQ',
                    'GREATEQ',
                    'IMPLY',
                    ]

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
t_LESSEQ = '<='
t_GREATEQ = '>='
t_IMPLY = '=>'

# Define a rule to track line numbers

def t_multilinecomment(t):
    r'\(\*(.|\n)*?\*\)'
    #print 'current line is :', t.lexer.lineno
    #print 'line count is :', t.value.count('\n')
    t.lexer.lineno += t.value.count('\n')
    print 'multiline comment is :', t.value,'ends here---------------'
def t_newline(t):
    r'\n+'
    #print 'new line found'
    #print 'len of nl is ', len(t.value)
    t.lexer.lineno += len(t.value)
def t_STRING(t):
    r'"[^"]*"'
    t.type = 'STRING'
    t.value = t.value[1:-1]
    return t
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.value = t.value.lower()
    t.type = reserved.get(t.value,'ID')
    return t
def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t




# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t\r'
t_ignore_COMMENT_SINGLE_LINE = r'--.*(?:--|[^\n])'
#t_ignore_COMMENT_MULTILINE = r'\(\*(?:.|\n)*\*\)'
#t_ignore_COMMENT_MULTILINE = r'\(\*[^(?:\*\))**\*\)'
#t_ignore_COMMENT_MULTILINE = r'\(\*[^(\*\))]+\*\)'

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
print 'hello'
if __name__ == "__main__":

    lexer.input(data)
    # Tokenize
    while True:
	    tok = lexer.token()
	    if not tok: break #No more input
	    print tok#tok.type, tok.value, tok.line, tok.lexpos


