def list_of_primes(number):
  listPrimes = []
  cont = 0
  for i in range(2, number + 1):
      for j in range(2, int(i/2) + 1):
        if (i) % j == 0:
          cont += 1
      if cont == 0:
          listPrimes.append(i)
      cont = 0
  return listPrimes

def get_prime_factors(n):
  listPrimes = []
  primeNumbers = list_of_primes(n)
  result = n
  i = 0
  while result != 1:
    prime = primeNumbers[i]
    if result % prime == 0:
      result = result / prime
      listPrimes.append(prime)
    else:
      i += 1
  return listPrimes

if __name__ == '__main__':
    print(get_prime_factors(630))  # [2, 3, 3, 5, 7]
    print(get_prime_factors(13))  # [13]

    #print(list_of_primes(630))
