"""
the maximum value of the sum of the elements of the sublist
"""

def main(items):
  overall = partial = items[0]
  for i in range(1, len(items)):
    partial = max(items[i], partial+items[i])
    overall = max(partial, overall)
  print(overall)

if __name__ == '__main__':
    main([0, -2, 3, 5, -1, 2])

