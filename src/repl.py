from lisp import *
import traceback

def repl(prompt = "lisp>>"):
  while True:
    userInput = input(prompt)
    if userInput == "exit":
      exit()
    try:
      val = eval(parse(userInput))
      if val is not None:
        print(schemeStr(val))
    except KeyboardInterrupt:
      print("\n")
      exit()
    except: #Print error and continue REPL
      traceback.print_exc()
      repl()

def schemeStr(exp):
  if isinstance(exp, List):
    return '(' + ' '.join(map(schemeStr, exp)) + ')'
  else:
    return str(exp)

repl()
