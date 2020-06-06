"""
Interview question: The difference and connection between processes and threads?
Processes-the basic unit of memory allocated by the operating system-a process can contain one or more thread
threads-the basic unit of CPU allocated by the operating system
concurrent programming (concurrent programming)
1. Improve execution performance-allow parts of the program that have no causality to be executed concurrently
2. Improve user experience-let time-consuming operations not cause the program to die
"""


""" 
Multi-threaded programs are usually relatively simple to deal with without competing resources. 
When multiple threads compete for critical resources, the lack of necessary protective measures will lead to data confusion 
. Critical resources are resources competed by multiple threads. 
"""


import time
import threading

from concurrent.futures import ThreadPoolExecutor

class Account(object):
  """Bank Account"""

  def __init__(self):
    self.balance = 0
    self.lock = threading.Lock()

  def deposit(self, money):
    # Protect critical resources
    with self.lock:
      new_balance = self.balance + money
      time.sleep(0.0001)
      self.balance = new_balance

class AddMoneyThread(threading.Thread):
  """Custom thread class"""

  def __init__(self, account, money):
    self.account = account
    self.money = money
    # In the initialization method of the custom thread, the initialization method super() of the parent class must be called init()

  def run(self) -> None:
    # The opertation to be performed after the thread starts
    self.account.deposit(self.money)

def main():
  """Main function"""
  account = Account()

  # Create thread pool
  pool = ThreadPoolExecutor(max_workers=10)
  futures = []

  for _ in range(100):
    # The first way to create threads
    # threading.Thread(target=account.deposit, args=(1,)).start()
    # The second way to create threads
    # AddMoneyThread(account, 1).start()
    # The third way to create threads Way
    # Call the thread in the thread pool to perform a specific task
    future = pool.submit(account.deposit, 1)
    futures.append(future)

  # close the thread pool
  pool.shutdown()

  for future in futures:
    future.result()
  print(account.balance)

if __name__ == '__main__':
    main()
