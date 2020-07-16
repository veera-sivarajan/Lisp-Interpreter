from lisp import *

def load(filename = 'codefile'):
  f = open(filename, 'r')
  program = f.readlines()
  f.close()
  print(program[0].strip())

load()
