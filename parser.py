# parser.py : parser for cool

import ply.yacc as yacc

# Get the token map from the lexer. This is required
from lexer import tokens

def p_program(p):
    """program : classes"""

def p_classes(p):
    """classes : classes class SEMICOLON
            | class SEMICOLON"""

    print 'classes is :', p[1:]

def p_class(p):
    """class : CLASS type INHERITS type LBRACE features RBRACE
            | CLASS type LBRACE features RBRACE"""
    print 'class is :', p[1:]


def p_features(p):
    """features : features feature SEMICOLON
            | feature SEMICOLON
            | empty """
    print 'features is :',p[1:]

def p_feature(p):
    """feature : ID LPAREN formalities RPAREN COLON type LBRACE expr RBRACE
                | ID COLON type ASSIGN expr
                | ID COLON type"""

    print 'p_feature is :',p[1:]
    p[0] = p[1:]
def p_formalities(p):
    """formalities : formal
                    | formal list_formal
                    | empty
                    """
    print 'p_formalities are :', p[1:] 
    p[0] = p[1:]

def p_list_formal(p):
    """list_formal : COMMA formal list_formal
                    | COMMA formal 
                    | empty"""

def p_formal(p):
    """formal : ID COLON type"""
    print 'p_formal is :',p[1:]
    p[0] = p[1:]


def p_expr(p):
    """expr : ID ASSIGN expr
            | expr ATRATE type DOT ID LPAREN expressions  RPAREN 
            | expr DOT ID LPAREN expressions RPAREN 
            | expr DOT ID LPAREN RPAREN
            | ID LPAREN expressions RPAREN
            | IF expr THEN expr ELSE expr FI
            | WHILE expr LOOP expr POOL
            | LBRACE expr_statements RBRACE
            | LET ID COLON type ASSIGN expr assignment_list IN expr
            | LET ID COLON type assignment_list IN expr
            | CASE expr OF assignment_ids ESAC
            | NEW type
            | ISVOID expr
            | expr PLUS expr
            | expr MINUS expr
            | expr TIMES expr
            | expr DIVIDE expr
            | TILDA expr
            | expr LANGLE expr
            | expr LESSEQ expr
            | expr EQUAL expr
            | NOT expr
            | LPAREN expr RPAREN
            | ID
            | INTEGER
            | STRING
            | TRUE
            | FALSE """


    if len(p) == 2:
        print 'p_expr 2 is :',p[1:]
        p[0] = p[1:]
    elif len(p) == 3:
        print 'p_expr 3 is :',p[1:]
        p[0] = p[1:]
    elif len(p) == 4:
        print 'p_expr 4 is :',p[1:]
        p[0] = p[1:]
    elif len(p) == 5:
        print 'p_expr 5 is :',p[1:]
        p[0] = p[1:]
    print 'p_expr is and len is :',p[1:],len(p)

def p_type(p):
    """type : ID"""
    print 'type is ',p[1:]
    p[0] = p[1:]




def p_assignment_ids(p):
    """assignment_ids : assignment_ids ID COLON type IMPLY expr SEMICOLON
                        | ID COLON type IMPLY expr SEMICOLON"""


    print 'assignment_ids is ', p[1:], 'and len is :',len(p)
def p_assignment_list(p):
    """assignment_list : COMMA ID COLON type ASSIGN expr assignment_list
                        | COMMA ID COLON type assignment_list
                        | COMMA ID COLON type
                        | empty"""

    print 'assignment_list is :', p[1:]
def p_expressions(p):
    """expressions : expr list_expressions
                    | expr 
                    | empty"""


    print 'p_expressions are :', p[1:]
    p[0] = p[1:]
def p_list_expressions(p):
    """list_expressions : COMMA expr list_expressions
                        | COMMA expr """

def p_expr_statements(p):
    """expr_statements : expr SEMICOLON expr_statements
                        | expr SEMICOLON """

    print 'p_expr_statements is :', p[1:]

def p_empty(p):
    """empty : """
    pass



# Error rule for syntax errors
def p_error(p):
    print "Syntax error in input!"
    print 'syntax error: p is :',p
    exit()

#Build the parser
import sys

if __name__ == "__main__":

    f = open(sys.argv[1])
    parser = yacc.yacc()
    while True:
        try:
            s = "".join(f.readlines())
        except EOFError:
            break
        if not s: continue
        result = parser.parse(s)
        print result
