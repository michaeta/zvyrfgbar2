# Symbol table based of example by Peter Norvig
class SymbolTable(dict):
    def __init__(self, parms=(), args=(), outer=None):
        self.update(zip(parms,args))
        self.outer = outer
    def find(self, var):
        return self if var in self else self.outer.find(var)

# not implemented yet
def evaluate(expr):
    # stubbed
    pass

# returns a and b
def op_and(a, b):
    return (a and b)

# standard or function
def op_or(a, b):
    return (a or b)

# if and only if
def op_iff(a, b):
    return (((not a) and b) or (a and (not b)))

# println
def op_println(a):
    print a
    return

# while loop
def op_while(a, b):
    while a:
        evaluate(b)
    return

#if/else statement
def op_if(a, b, c = None):
    if (a):
        evaluate(b)
    else:
        evaluate(c)
    return

# assignment statement
def op_assign(a, b):
    a = b
    return

# sets scope of variables
# not implemented yet
# create sub symbol tables for each statement/expr?
def op_let(a, b):
    pass

# defines the different 
def define_globals(symbol_table):
    import math, operator as op
    symbol_table.update(
     {'+':op.add, '-':op.sub, '*':op.mul, '/':op.div, 'not':op.not_,
      '>':op.gt, '<':op.lt, '>=':op.ge, '<=':op.le, '=':op.eq, '%': op.mod,
      'e':math.exp, 'logn':math.log, 'sin':math.sin, 'cos':math.cos,
      'tan':math.tan, 'real':float, 'string':str, 'bool':bool, 'int':int,
      'true':True, 'false':False, '^':math.pow, 'and':op_and, 'or':op_or,
      'iff':op_iff, 'while':op_while, 'if':op_if, 'let':op_let, 'assign':op_assign,
      'println':op_println})
    return symbol_table

global_symbol_table = define_globals(SymbolTable())

# parse the file!
def parse(s):
    return lex(tokenize(s))

# adds spaces to parenthesis so they can be split into tokens
def tokenize(s):
    #use the @ symbol so we dont split on spaces in strings
    return s.replace('(','@(@').replace(')','@)@').split('@')

# returns the tokens
def lex(tokens):
    if len(tokens) == 0:
        raise SyntaxError('Unexpected EOF.')
    token = tokens.pop(0)
    if '(' == token:
        inner = []
        while tokens[0] != ')':
            inner.append(lex(tokens))
        tokens.pop(0)
        return inner
    elif ')' == token:
        raise SyntaxError('Unexpected )')
    else:
        return atom(token)

#definition for a string, tries to cast it to a int, on failure
#tries to cast to float, finally it just returns the string
def atom(token):
    try: return int(token)
    except ValueError:
        try: return float(token)
        except ValueError:
            return str(token) 
