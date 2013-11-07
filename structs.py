# structs.py
# This has all the structs that would be needed after parsing stage.
# Mainly the classes for Abstract Syntax Tree

class Program():
    "the root of the AST"
    def __init__(self):
        print 'program created'


class Classes():
    "collection of classes in a program"
    def __init__(self):
        print 'Classes created'

class Class():
    "a class definition in a program"
    def __init__(self):
        print 'Classes created'
class Features():
    "collection of features in a class"
    def __init__(self):
        print 'Features created for the class'

class Feature():
    "a feature in a class, variable of a class or a function"
    def __init__(self):
        print 'Feature of a class'

class Formalities():
    "formalities in a feature"
    def __init__(self):
        print 'Formalities of a class'

class ListFormal():
    "list of Formals in a feature"
    def __init__(self):
        print 'List of formals in a feature'

class Formal():
    "Formal in a feature"
    def __init__(self):
        print 'Formal in a feature'

class Expr():
    "Expression"
    def __init__(self):
        print 'Expr class'

class Type():
    "Type"
    def __init__(self):
        print 'Type class'

class AssignmentIds():
    "assignment_ids"
    def __init__(self):
        print 'assignment_ids'

class AssignmentList():
    "assignment_list"
    def __init__(self):
        print 'assignment list'

class Expressions():
    "Expressions"
    def __init__(self):
        print 'Expressions'

class ListExpressions():
    "list_expressions"
    def __init__(self):
        print 'list_expressions'

class ExprStatements():
    "expr_statements"
    def __init__(self):
        print 'expr_statements'

if __name__ == "__main__":
    cl = Classes()
