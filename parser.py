class SymbolTable(dict):
    def __init__(self, parms=(), args=(), outer=None):
        self.update(zip(parms,args))
        self.outer = outer
    def find(self, var):
        return self if var in self else self.outer.find(var)

def op_and(a, b):
    return (a and b)

def op_or(a, b):
    return (a or b)

def op_iff(a, b):
    return (((not a) and b) or (a and (not b)))
        

def define_globals(symbol_table):
    import math, operator as op
    symbol_table.update(
     {'+':op.add, '-':op.sub, '*':op.mul, '/':op.div, 'not':op.not_,
      '>':op.gt, '<':op.lt, '>=':op.ge, '<=':op.le, '=':op.eq, '%': op.mod,
      'e':math.exp, 'logn':math.log, 'sin':math.sin, 'cos':math.cos,
      'tan':math.tan, 'real':float, 'string':str, 'bool':bool, 'int':int,
      'true':True, 'false':False, "^":math.pow, 'and':op_and, 'or':op_or,
      'iff':op_iff})
    return symbol_table

global_symbol_table = define_globals(SymbolTable())

def parse(s):
    return lex(tokenize(s))

def tokenize(s):
    return s.replace('(',' ( ').replace(')',' ) ').split()

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
        raise SyntaxError('unexpected )')
    else:
        return atom(token)


def atom(token):
    try: return int(token)
    except ValueError:
        try: return float(token)
        except ValueError:
            return str(token)
