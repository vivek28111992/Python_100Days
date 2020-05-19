def bubble_sort(items, comp= lambda x, y: x > y):
  for i in range(len(items) - 1):
    swapped = False
    for j in range(len(items)-1-i):
      if comp(items[j], items[j+1]):
        items[j], items[j+1] = items[j+1], items[j]
        swapped = True
    print(items)
    if not swapped:
      break
  return items

if __name__ == '__main__':
    bubble_sort([8, 3, 5, 1, 0, 2, 9])
