class test(object):
    def __init__(self, a, b):
      print("Inside init")
      self.a = a
      self.b = b

    def __call__(self, *args):
      print("Inside call")
      return func(args)

def func(args):
  print(args)

def load():
  return test(1, 2)

x = load()
x(1,2)
  

