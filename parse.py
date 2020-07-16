from var import *

def tokenize(line: str) -> list:
  return line.replace('(', ' ( ').replace(')', ' ) ').split()

def parse(program: str) -> Exp:
  return readTokens(tokenize(program))
  
def readTokens(tokens: list) -> Exp:
  if len(tokens) == 0:
    raise SyntaxError('unexpected EOF')

  token = tokens.pop(0) #popping first element to iterate list

  if token == '(':
    L = []
    while tokens[0] != ')':
      #print(hex(id(tokens)))
      #print("Inside while: " ,  tokens)
      L.append(readTokens(tokens))
    tokens.pop(0)
    return L
    
  elif token == ')':
    raise SyntaxError('unexpected )')

  else: 
    return atom(token)

def atom(token: str) -> Atom:
  try: return int(token)
  except ValueError:
    try: return float(token)
    except ValueError:
      return Symbol(token)
