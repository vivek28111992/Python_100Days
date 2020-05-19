def generativeFormula() -> None:
  prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
  }

  # configured with stock price is greater than $100 a new dictionary
  prices2 = { key: value for key, value in prices.items() if value > 100 }
  print(prices2)

def nestedListOfPits() -> None:
  names = ['Vivek', 'Sankey', 'Vamsi', 'Yogesh']
  courses = ['English', 'Maths', 'Science']

  scores = [[None] * len(courses) for _ in range(len(names))]

  for row, name in enumerate(names):
    for col, course in enumerate(courses):
      scores[row][col] = float(input(f"Enter {name}'s {course} result: "))
      print(scores)

def heapq_module():
  """
  Find the largest or smallest N element
  heap structure (large root heap / small root heap)
  from the list
  :return:
  """
  import heapq

  list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
  list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
  ]
  print(heapq.nlargest(3, list1))
  print(heapq.nsmallest(3, list1))
  print(heapq.nlargest(2, list2, key=lambda x: x['price']))
  print(heapq.nsmallest(2, list2, key=lambda x: x['shares']))

def itertools_module() -> None:
  """
  Itertools module
  :return:
  """
  import itertools

  # ABCD produce a full arrangement of
  p = itertools.permutations('ABCD')

  # generates five selected three combination ABCDE
  c = itertools.combinations('ABCD', 3)

  # 123 produced ABC and cartesian product
  itertools.product('ABCD', '123')

  # ABC infinite loop sequence produced
  itertools.cycle(('a', 'b', 'c'))

def collections_module() -> None:
  from collections import Counter

  words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', ' not ', ' around ',
    ' the ', ' eyes', "don't", 'look', 'around ', ' the ', ' eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
  ]

  counter = Counter(words)
  print(counter.most_common(3))

if __name__ == '__main__':
  generativeFormula()
  # nestedListOfPits()
  heapq_module()
  itertools_module()
  itertools_module()
  collections_module()