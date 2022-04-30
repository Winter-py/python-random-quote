import random

def primary():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = 17
  rnd = random.randint(0, last)
  arnd = random.randint(0, last)

  print(quotes[rnd] + quotes[arnd])
  

if __name__== "__main__":
  primary()
