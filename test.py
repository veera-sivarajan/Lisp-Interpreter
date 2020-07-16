from lisp import *

def schemeStr(exp):
  if isinstance(exp, List):
    return '(' + ' '.join(map(schemeStr, exp)) + ')'
  else:
    return str(exp)

with open('codefile') as file:
  for line in file:
    print("Line: ", line, "Line length: " , len(line))
    if(len(line) > 0):
      try:
        val = eval(parse(line.strip()))
        if val is not None:
          print(schemeStr(val))
      except KeyboardInterrupt:
        print("\n")
        exit()
