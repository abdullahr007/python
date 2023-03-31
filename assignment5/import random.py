import random
random. seed()
minval = 1
maxval = 50
r = random . randint(minval, maxval)
counter = 0
found = False
while not found:
    guess = int(input(" Enter your guess : "))
    counter += 1
    if r == guess:
        print("Took", counter, "attempts", " You got it!")
        break
    elif guess < r:
        print(" Your guess is too small !", "attempt=", counter)
    else:
        print(" Your guess is too high !", "attempt=", counter)
print("Bye")
