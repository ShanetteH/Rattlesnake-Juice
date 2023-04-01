tries = 0

guess = 0

while guess != 6:
  guess = int(input("Guess the number:  "))
  tries = tries + 1

print("You got it! Tries taken: " + str(tries))
