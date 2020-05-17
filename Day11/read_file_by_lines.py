import time

def main():
  # Read the file content at once
  with open('test.txt', 'r', encoding='utf-8') as f:
    print(f.read())

  # Read through for-in loop line-by-line
  with open('test.txt', 'r', ) as f:
    for line in f:
      print(line, end='')
      time.sleep(0.5)
  print()

  # REad the file & read it into list by line
  with open('test.txt') as f:
    lines = f.readlines()
  print(lines)

if __name__ == '__main__':
  main()
