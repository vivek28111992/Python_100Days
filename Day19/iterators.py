"""
Iterators are objects that implement the iterator protocol.

There are no keywords in protocol or interface like Python that define the protocol.
The magic method is used to represent the protocol in Python.
__iter__The __next__magic method is the iterator protocol.
"""

class Fib(object):
  """Iterator"""

  def __init__(self, num):
    self.num = num
    self.a, self.b = 0, 1
    self.idx = 0

  def __iter__(self):
    return self

  def __next__(self):
    if self.idx < self.num:
      self.a, self.b = self.b, self.a + self.b
      self.idx += 1
    raise StopIteration()
