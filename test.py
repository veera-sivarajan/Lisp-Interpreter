from lisp import *

def schemeStr(exp):
  if isinstance(exp, List):
    return '(' + ' '.join(map(schemeStr, exp)) + ')'
  else:
    return str(exp)

with open('lispcode') as file:
  for line in file:
    print(type(line))
    if(len(line) > 0):
      try:
        val = eval(parse(line))
        if val is not None:
          print(schemeStr(val))
      except KeyboardInterrupt:
        print("\n")
        exit()
      

