import random

meal_options = []

while True:
    print('Enter a possible meal #' + str(
        len(meal_options) + 1) + ', or type nothing finish.')
    name = input()
    if name == '':
        break
    meal_options = meal_options + [name]
print(meal_options)
print('And the winner is... ' + random.choice(meal_options) + '!')
