
import random
import sys


def getAnswer(num):
    if num == 1:
        return 'Yes'
    elif num == 2:
        return 'No'
    elif num == 3:
        return 'Maybe'


while True:
    if input('Ask me a yes or no question, or type "exit": ') == 'exit':
        break
    fortune = getAnswer(random.randint(1, 3))
    print(fortune)

sys.exit()
