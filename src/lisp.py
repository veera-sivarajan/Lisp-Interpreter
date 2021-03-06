import math
import operator as op
from var import *
from parse import *

def standardEnv() -> Env:
  env = Env() #create new dict
  env.update(vars(math)) #Convert trig functions to dict format and add to env
  env.update({
        '+':lambda *x: sum(x), '-':op.sub, '*':op.mul, '/':op.truediv, 
        '>':op.gt, '<':op.lt, '>=':op.ge, '<=':op.le, '=':op.eq, 
        'mul':     lambda *x: math.prod(x),
        'abs':     abs,
        'append':  op.add,  
        'apply':   lambda proc, args: proc(*args),
        'atom?':   lambda x: not isinstance(x, List),
        'begin':   lambda *x: x[-1],
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
        'number?': lambda x: isinstance(x, Number), '#print': print, 
        'procedure?': callable,
        'round':   round,
        'symbol?': lambda x: isinstance(x, Symbol),
        't'    : True,
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
    self.parms = parms
    self.body = body
    self.env = env

  def __call__(self, *args):
    return eval(self.body, Env(self.parms, args, self.env))

globalEnv = standardEnv()

def eval(x: Exp, env = globalEnv) -> Exp:
  #print("Expression: " , x)
  if isinstance(x, Symbol): #Check if built in function 
    #print("Symbol" , x)
    ##print(env.locate(x))
    return env.locate(x)[x]

  elif isinstance(x, Number):
    #print("Number: ", x)
    return x

  elif not isinstance(x, List):
    #print("List: ", x)
    return x
  
  op, *args = x
  
  if op == "quote":
    return args[0]

  elif op == 'if': #Check if 
    #print("If condition")
    (test, conseq, alt) = args 
    exp = (conseq if eval(test, env) else alt)
    return eval(exp, env)

  elif op == 'define': 
    #print("define statement")
    (symbol, exp) = args 
    env[symbol] = eval(exp, env) #Add variable name: value to env

  elif op == "set":
    (symbol, exp) = args
    env.locate(symbol)[symbol] = eval(exp, env)

  elif op == "lambda":
    (parms, body) = args
    #print("Calling Procedure")
    return Procedure(parms, body, env)
    #return eval(body, Env(parms, 

  elif op == "cond": #Lisp's version of if case
    for (x,y) in args:
      if eval(x, env):
        return eval(y, env)
    return [] #WHY?
    
  else:
    #print("non built it procedure")
    proc = eval(op, env) #get function definition from env
    vals = [eval(arg, env) for arg in args] #evaluate all arguments and store in args
    ##print(vals)
    return proc(*vals)  #unpack elements from list to positional arguments
                        #func(*[1, 2, 3]) == func(1, 2, 3)

