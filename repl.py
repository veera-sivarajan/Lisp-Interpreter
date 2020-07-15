from lisp import *

def repl(prompt = "lisp>>"):
  while True:
    try:
      val = eval(parse(input(prompt)))
      if val is not None:
        print(schemeStr(val))
    except KeyboardInterrupt:
      print("\n")
      exit()
      

def schemeStr(exp):
  if isinstance(exp, List):
    return '(' + ' '.join(map(schemeStr, exp)) + ')'
  else:
    return str(exp)

repl()
