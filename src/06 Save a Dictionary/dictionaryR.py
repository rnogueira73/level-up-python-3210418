import json

def save_dict(dict, newFilename):
  with open(newFilename, 'w') as file:
    file.write(json.dumps(dict))

def load_dict(filename):
  with open(filename) as file:
    data = file.read()
  return json.loads(data)

if __name__ == '__main__':
    test_dict = test_dict = {'Gfg' : [6, 5, 9, 3, 10],
             'is' : [1, 3, 4], 
             'best' :[9, 16]} 
    save_dict(test_dict, 'test_dict.pickle')
    recovered = load_dict('test_dict.pickle')
    print(recovered)  # {1: 'a', 2: 'b', 3: 'c'}