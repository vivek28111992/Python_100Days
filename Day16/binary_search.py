def binary_search(items, key):
  start, end = 0, len(items) - 1
  while start <= end:
    mid = (start + end) // 2
    print(mid)
    if items[mid] == key:
      return mid
    elif items[mid] > key:
      end = mid - 1
    else:
      start = mid + 1
  return -1

if __name__ == '__main__':
    res = binary_search([0, 1, 2, 5, 7, 8, 9], 5)
    print(res)