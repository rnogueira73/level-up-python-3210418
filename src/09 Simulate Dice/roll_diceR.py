import random
from collections import Counter

def roll_dice(*dice, num_trails=1_000_000):
   counts = Counter()
   for _ in range(num_trails):
      counts[sum((random.randint(1, sides) for sides in dice))] += 1
   
   print("\nResults\tProbability")
   for results in range(len(dice), sum(dice) + 1):
      print(f"{results}\t{counts[results] * 100 / num_trails :0.2f}%")

def rolling(dice):
    sum = 0
    for i in dice:
      sum += random.randint(1, i)
    return sum

def roll_dice_R(*dice):
    dice_results = {}
    x = 1
    iterations = 1000000
    while x <= iterations:
      rolling_result = rolling(dice)
      if dice_results.get(rolling_result) is not None:
        dice_results.update({rolling_result:dice_results[rolling_result]+1})      
      else:
        dice_results.update({rolling_result:1})
      x += 1
    my_keys = list(dice_results.keys())
    my_keys.sort()
    dice_results_ordered = {i: dice_results[i] for i in my_keys}
    for key, value in dice_results_ordered.items():
       print(f"{key}   {round(value/iterations*100,2)}%")
       dice_results_ordered.update({key:round(value/iterations*100,2)})
       
    print("Fin!")
    




if __name__ == '__main__':
    roll_dice(6)
    roll_dice(4, 6, 6)
    roll_dice(4, 6, 6, 20)
