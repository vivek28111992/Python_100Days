from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep

def download_task(filename):
  print(f'Start download process, process number [{getpid()}] \n')
  print(f'Start downloading {filename} ... ')
  time_to_download = randint(5, 10)
  sleep(time_to_download)
  print(f'{filename} download completed! It took {time_to_download} seconds')

def main():
  start = time()
  p1 = Process(target=download_task, args=('Python from entry to hospital.pdf', ))
  p1.start()
  p2 = Process(target=download_task, args=('Peking Hot.avi', ))
  p2.start()
  p1.join()
  p2.join()
  end = time()
  print('It took {0:.2f} seconds in total.'.format(end - start))

if __name__ == '__main__':
    main()
