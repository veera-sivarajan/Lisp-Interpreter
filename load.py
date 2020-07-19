from lisp import *

def lparen(line):
  return line.count('(')

def rparen(line):
  return line.count(')')

def load(filename = 'codefile'):
  f = open(filename, 'r')
  program = f.readlines()
  f.close()
  index = 0
  pLen = len(program)
  while (index < pLen):
    line = program[index].strip()
    while (lparen(line) != rparen(line)):
      #print("Inside while loop")
      index += 1
      line += program[index] 
      #print(line)
    feed(line)
    index += 1
      
def feed(line):
  val = eval(parse(line))
  if val is not None:
    print(schemeStr(val))

def schemeStr(exp):
  if isinstance(exp, List):
    return '(' + ' '.join(map(schemeStr, exp)) + ')'
  else:
    return str(exp)

load()
