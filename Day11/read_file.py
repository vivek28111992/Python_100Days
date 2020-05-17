def main():
  try:
    with open('test.txt', 'r', encoding='utf-8') as f:
      print(f.read())
  except FileNotFoundError:
    print('Unable to open the specified file!')
  except LookupError:
    print('an unknown coding!')
  except UnicodeDecodeError:
    print('error while reading the file decoding!')

if __name__ == '__main__':
  main()

