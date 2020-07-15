import math
import operator as op

Symbol = str
Number = (int, float)
Atom = (Symbol, Number)
List = list
Exp = (Atom, List)
Env = dict

def tokenize(line: str) -> list:
  return line.replace('(', ' ( ').replace(')', ' ) ').split()

def parse(program: str) -> Exp:
  return readTokens(tokenize(program))
  
def readTokens(tokens: list) -> Exp:
  if len(tokens) == 0:
    raise SyntaxError('unexpected EOF')

  token = tokens.pop(0) #popping first element to iterate list

  if token == '(':
    L = []
    while tokens[0] != ')':
      #print(hex(id(tokens)))
      #print("Inside while: " ,  tokens)
      L.append(readTokens(tokens))
    tokens.pop(0)
    return L
    
  elif token == ')':
    raise SyntaxError('unexpected )')

  else: 
    return atom(token)

def atom(token: str) -> Atom:
  try: return int(token)
  except ValueError:
    try: return float(token)
    except ValueError:
      return Symbol(token)
      
def standardEnv() -> Env:
  env = Env()
  env.update(vars(math)) #Convert trig functions to dict and add to env
  env.update({
        '+':op.add, '-':op.sub, '*':op.mul, '/':op.truediv, 
        '>':op.gt, '<':op.lt, '>=':op.ge, '<=':op.le, '=':op.eq, 
        'abs':     abs,
        'append':  op.add,  
        'apply':   lambda proc, args: proc(*args),
        'begin':   lambda *x: x[1],
        'car':     lambda x: x[0],
        'cdr':     lambda x: x[1:], 
        'cons':    lambda x,y: [x] + y, #x is an item and y is a list
        'eq?':     op.is_, 
        'expt':    pow,
        'equal?':  op.eq, 
        'length':  len, 
        'list':    lambda *x: List(x), 
        'list?':   lambda x: isinstance(x, List), 
        'map':     map,
        'max':     max,
        'min':     min,
        'not':     op.not_,
        'null?':   lambda x: x == [], 
        'number?': lambda x: isinstance(x, Number), 'print': print, 
        'procedure?': callable,
        'round':   round,
        'symbol?': lambda x: isinstance(x, Symbol),
  })
  return env

class Env(dict):
  def __init__(self, parms = (), args = (), outer = None):
    self.update(zip(parms, args))
    self.outer = outer

  def locate(self, var):
    return self if (var in self) else self.outer.locate(var)

class Procedure(object):
  def __init__(self, parms, body, env):
    self.parms, self.body, self.env = parms, body, env

  def __call__(self, *args):
    return eval(self.body, Env(self.parms, args, self.env))

globalEnv = standardEnv()

def eval(x: Exp, env = globalEnv) -> Exp:
  #print("Expression: " , x)
  if isinstance(x, Symbol): #Check if built in function 
    #print("Symbol" , x)
    if x == 'exit':
      exit()
    return env.locate(x)[x]

  elif not isinstance(x, List):
    return x
  
  op, *args = x
  
  if op == "quote":
    return args[0]

  elif op == 'if': #Check if 
    #print("If condition")
    (test, conseq, alt) = args 
    exp = (conseq if eval(test, env) else alt)
    return eval(exp, env)

  elif x[0] == 'define': 
    #print("define statement")
    (symbol, exp) = args 
    env[symbol] = eval(exp, env) #Add variable name: value to env

  elif op == "set":
    (symbol, exp) = args
    env.locate(symbol)[symbol] = eval(exp, env)

  elif op == "lambda":
    (parms, body) = args
    return Procedure(parms, body, env)

  else:
    #print("non built it procedure")
    proc = eval(x[0], env) #store function name in proc
    args = [eval(arg, env) for arg in x[1:]] #evaluate all arguments and store in args
    return proc(*args)  #unpack elements from list to positional arguments
                        #func(*[1, 2, 3]) == func(1, 2, 3)
