import json

def main():
  mydict = {
    'name': 'Vivek',
    'age': 38,
    'cars': [
      { 'brand': 'BYD', 'max_speed': 180 },
      { 'brand': 'Audi', 'max_speed': 280 },
      { 'brand': 'Benz', 'max_speed': 320 }
    ]
  }

  try:
    with open('data.json', 'w', encoding='utf-8') as f:
      json.dump(mydict, f)
  except IOError as e:
    print(e)
  print('Saving of data completed!')

if __name__ == '__main__':
    main()
