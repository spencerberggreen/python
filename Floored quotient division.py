import sys


def quotient():
    return dividend // divisor


def remainder():
    return dividend % divisor


while True:
    print('Type "exit" to close the program at any time')
    dividend = (input('Type the dividend: '))
    if dividend == 'exit':
        break
    divisor = (input('Type the divisor: '))
    if divisor == 'exit':
        break
    dividend = int(dividend)
    divisor = int(divisor)
    try:
        print('Floored Quotient: ', quotient())
        print('Remainder: ', remainder())
    except ZeroDivisionError:
        print('You cant divide by zero.')
sys.exit()
