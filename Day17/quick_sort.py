"""
Quick sort-select the pivot to divide the elements, the left is smaller than the pivot and the right is larger than pivot
"""

def quick_sort(items, comp = lambda x, y: x <= y):
  _quick_sort(items, 0, len(items) - 1, comp)
  return items

def _quick_sort(items, start, end , comp):
  if start < end:
    pos = _partition()
    _quick_sort(items, start, pos-1, comp)
    _quick_sort(items, pos+1, end, comp)

def _partition(items, start, end, comp):
  pivot = items[end]
  i = start - 1
  for j in range(start, end):
    if comp(items[j], pivot):
      i += 1
      items[i], items[j] = items[j], items[i]
  items[i+1], items[end] = items[end], items[i+1]
  return i+1
