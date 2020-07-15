from lisp import *

def repl(prompt = "lisp>>"):
  while True:
    val = eval(parse(input(prompt)))
    if val is not None:
      print(schemeStr(val))

def schemeStr(exp):
  if isinstance(exp, List):
    return '(' + ' '.join(map(schemeStr, exp)) + ')'
  else:
    return str(exp)

repl()
