"""
The generator is a simplified version of the iterator
"""

def fib(n):
  """builder"""
  a, b = 0, 1
  for _ in range(n):
    a, b = b, a+b
    yield a

"""
The generator evolved into a coroutine.

The generator object can send()send data using methods, and the sent data will become yieldthe value obtained by the expression in the generator function . In this way, the generator can be used as a coroutine, which is simply a subroutine that can cooperate with each other.
"""
def calc_avg():
  """Streaming average"""
  total, counter = 0, 0
  avg_value = None
  while True:
    value = yield avg_value
    total, counter = total + value, counter+1
    avg_value = total/counter

if __name__ == '__main__':
    fib(5)
    gen = calc_avg()
    next(gen)
    print(gen.send(10))
    print(gen.send(20))
    print(gen.send(30))
