from time import sleep
from threading import Thread, Lock


class Account(object):

  def __init__(self):
    self._balance = 0
    self._lock = Lock()

  def deposit(self, money):
    # acquire the lock before executing subsequent code
    self._lock.acquire()
    try:
      # Calculate the balance after deposit
      new_balance = self._balance + money
      # It takes 0.01 seconds to stimulate the deposit acceptance business
      sleep(0.01)
      # Modify the account balance
      self._balance = new_balance
    finally:
      # execute the release in finally to ensure the normal operation of the lock the abnormal release of
      self._lock.release()

  @property
  def balance(self):
    return self._balance

class AddMoneyThread(Thread):
  def __init__(self, account, money):
    super().__init__()
    self._account = account
    self._money = money

  def run(self) -> None:
    self._account.deposit(self._money)

def main() -> None:
  account = Account()
  threads = []
  # Create 100 deposit threads to save money in the same account
  for _ in range(100):
    t = AddMoneyThread(account, 1)
    threads.append(t)
    t.start()

  # Wait for all the deposits threads to be executed
  for t in threads:
    t.join()
  print(f'Account balance: {account.balance}')

if __name__ == '__main__':
    main()

