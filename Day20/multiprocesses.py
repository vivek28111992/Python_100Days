"""
Multiple processes and process pools use multithreading. Because of the existence of GIL, they cannot take advantage of the multicore features of the CPU.
For computationally intensive tasks, you should consider using multiprocess time python3 example22.py
real 0m11.512s
user 0m39.319s
sys 0m0.169s
After using multi-processes, the actual execution time is 11.512 seconds, and the user time 39.319 seconds is about 4 times the actual execution time.
This proves that our program uses the multi-core characteristics of the CPU through multi-processes, and this computer is configured with a 4-core CPU.
"""

import concurrent.futures
import math

PRIMES = [
  1116281 ,
   1297337 ,
   104395303 ,
   472882027 ,
   533000389 ,
   817504243 ,
   982451653 ,
   112272535095293 ,
   112582705942171 ,
   112272535095293 ,
   115280095190773 ,
   115797848077099 ,
   1099726899285419
] * 5

def is_prime(n):
  """judgement prime number"""
  if n%2 == 0:
    return False

  sqrt_n = int(math.floor(math.sqrt(n)))
  for i in range(3, sqrt_n+1, 2):
    if n%i == 0:
      return False
  return True

def main():
  with concurrent.futures.ProcessPoolExecutor() as executor:
    for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
      print(f'{number} is prime : {prime}')

if __name__ == '__main__':
    main()
