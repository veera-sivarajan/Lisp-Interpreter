from lisp import *
import sys

def equalParen(line):
  return line.count('(') == line.count(')')

def load(filename = "/home/veera/Projects/LispIp/test/codefile"):
  f = open(filename, 'r')
  program = f.readlines()
  f.close()
  index = 0
  pLen = len(program)
  while (index < pLen):
    line = program[index].strip()
    while not (equalParen(line)):
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

load(sys.argv[1])
