from random import randint

def file2array(filename):
  with open(filename,"r") as file:
    for line in file:
      if not line.strip() or line.startswith('-----') or '=' in line:
        continue
      try:
        number, word = line.strip().split('\t')
        wordDict.update({number: word})
      except ValueError:
        continue

def generate_passphrase(rollnumber):
  sides = 6
  passphrase = []
  file2array('diceware.wordlist.asc') 
  for roll in range(rollnumber):
    diceResult = ''.join(str(randint(1, sides)) for _ in range(5))

    if diceResult in wordDict: passphrase.append(wordDict[diceResult])

  return ' '.join(passphrase)


if __name__ == '__main__':
  wordDict = {}
  print(generate_passphrase(5))
  print(generate_passphrase(3))

  
