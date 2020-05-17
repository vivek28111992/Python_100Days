from multiprocessing import Process, Queue
from random import randint
from time import time

def task_handler(curr_list, result_queue):
  total = 0
  for number in curr_list:
    total += number
  result_queue.put(total)

def main():
  processes = []
  number_list = [x for x in range(1, 10000001)]
  result_queue = Queue()
  index = 0

  # Start 8 processes to slice the data and perform operations
  for _ in range(8):
    p = Process(target=task_handler, args=(number_list[index: index + 1250000], result_queue))
    index += 1250000
    processes.append(p)
    p.start()

  # Start recording the time it takes for all processes to complete execution
  start = time()

  for p in processes:
    p.join()

  # The combined execution result
  total = 0
  while not result_queue.empty():
    total += result_queue.get()
  print(total)
  end = time()
  print(f'Execution time: {end - start}', sep='')

if __name__ == '__main__':
    main()

