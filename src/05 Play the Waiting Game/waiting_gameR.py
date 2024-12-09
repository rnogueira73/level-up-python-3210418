import time
import random

def waiting_game():
  randomTime = random.randint(1,10)
  too = "slow"

  print(f"Your tarjet times is {randomTime} seconds.")
  input("--Press Enter to Begin--")
  startTime = time.time()
  input()
  stopTime = time.time()

  elapsedTime  = round(stopTime - startTime, 3)
  difTime = round(randomTime - elapsedTime, 3)
  if difTime >= 0:
    too = "soon"
  return f" Elapsed Time: {elapsedTime} seconds ( {abs(difTime)} seconds to {too})"


if __name__ == '__main__':
  print(waiting_game())