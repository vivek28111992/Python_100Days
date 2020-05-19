def select_sort(items, comp = lambda x, y: x < y ):

  for i in range(len(items)-1):
    min_index = i
    for j in range(i+1, len(items)):
      if comp(items[j], items[min_index]):
        min_index = j
    items[i], items[min_index] = items[min_index], items[i]
    print(items)
  return items

if __name__ == '__main__':
    res = select_sort([8, 3, 5, 1, 0, 2, 9])
    print(res)