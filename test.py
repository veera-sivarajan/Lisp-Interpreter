class Test:
  def __init__(self, a, b):
    print("init")
    self.a = a
    self.b = b

  def __call__(self, a, b):
    print("__call__")
    print("a+b", a+b)

obj = Test(1, 2)
Test(3, 4)
