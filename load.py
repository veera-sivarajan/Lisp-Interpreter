from lisp import *

def lparen(line):
  return line.count('(')

def rparen(line):
  return line.count(')')

def load(filename = 'codefile'):
  f = open(filename, 'r')
  program = f.readlines()
  f.close()
  program = [line.strip() for line in program]
  lenProgram = len(program)
  index = 0
  #print("Length: ", lenProgram)
  while (index < lenProgram):
    #print("Incoming index: ", index)
    while not (lparen(program[index]) == rparen(program[index])):
      #print("Modding index at: ", index)
      #print("Moding line: ", program[index])
      #print(lparen(program[index]), " ", rparen(program[index]))
      addIndex = index + 1
      #print("Adding ele at: ",addIndex)
      program[index] += " " + program[addIndex]
      #print("Modifyed input: ",program[index])
      program.pop(addIndex)
      #print("Modifyed program: ",program)
    index += 1
    lenProgram = len(program)
    #print(lenProgram)
    for line in program:
      print(line)
      
load()
