from calc import *

def repl(prompt = "lispCalc>>"):
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
