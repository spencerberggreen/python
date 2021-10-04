import random
for i in range(1):
    num = (random.randint(1, 20))

for guessQty in range(1, 6):
    print('''I'm thinking of a number between 1-20, take a guess.''')
    guess = int(input())

    if guess > num:
        print('Too high')
    elif guess < num:
        print('Too low')
    else:
        break

if guess == num:
    print('Nice work! You got it in ' + str(guessQty) + ' guesses!')
else:
    print('I was thinking of ' + str(num))
