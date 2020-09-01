import random

def main():

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  rnd = random.randint(0,len(quotes)-1)

  print(quotes[rnd], end = '')
  print(quotes[rnd+1])

if __name__== "__main__":
  main()
