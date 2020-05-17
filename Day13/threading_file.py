from random import randint
from threading import Thread
from time import time, sleep

class Download(Thread):

  def __init__(self, filename):
    super().__init__()
    self._filename = filename

  def run(self):
    print(f'Start downloading {self._filename} ...')
    time_to_download = randint(5, 10)
    sleep(time_to_download)

    print(f'Download completed! It took {time_to_download} seconds')

def main():
  start = time()
  t1 = Download('Python from entry to hospital.pdf', )
  t1.start()
  t2 = Download('Peking Hot.avi',)
  t2.start()
  t1.join()
  t2.join()
  end = time()
  print('Total cost {0:.3f}'.format(end - start))

if __name__ == '__main__':
    main()