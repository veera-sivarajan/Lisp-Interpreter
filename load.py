from lisp import *
from repl import *

def load(filename):
  print("Loading file")
  f = open(filename, 'r')
  program = f.readlines()
  f.close()
  rps = running_paren_sums(program)
  full_line = ''
  for (paren_sum, program_line) in zip(rps, program):
    program_line = program_line.strip()
    full_line   += "%s " % program_line
    if (paren_sum == 0) and (full_line.strip() != ''):
      try:
        val = eval(parse(full_line))
        if val is not None: print(schemeStr(val))
      except:
        handle_error()
        print("ERROR")
        break
      full_line = ''
  repl()

def running_paren_sums(program):
  count_open_parens = lambda line: line.count('(') - line.count(')')
  paren_counts      = map(count_open_parens, program)
  rps   = []
  total = 0
  for paren_count in paren_counts:
    total += paren_count
    rps.append(total)
  return rps

load()
