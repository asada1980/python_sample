class MyClass:
  def minus(self, a, b):
    return a-b
  
  def plus(self, a, b):
    return a+b

myClass = MyClass()

print(myClass.minus(10, 3))

print(myClass.plus(10, 3))

import os
dir_path = os.path.dirname(os.path.abspath(__file__))
print(dir_path)

test = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(test)

test = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(test)

