import re
from collections import Counter

def count_words(filename):
    f = open(filename, "r")
    list = []
    count = 0
    for line in f.readlines():
        line =re.findall(r"([a-z0-9-']+)", line.lower().strip())
        list += line
        count += (len(line))

    print(f"Total Word: {count :,.0f}\n")
    print("Top 20 Word:\n")
    counts = Counter(list)
    top = 0
    for key, value in sorted(counts.items(), key=lambda item: item[1], reverse=True):
      print(f"{top+1}\t{key.upper()}\t{value:,.0f}")
      top += 1
      if top >= 20:
        break

if __name__ == '__main__':
    count_words('shakespeare.txt')