data = {'top-L': '   ', 'top-M': '   ', 'top-R': '   ', 'mid-L': '   ',
        'mid-M': '   ', 'mid-R': '   ', 'bot-L': '   ', 'bot-M': '   ', 'bot-R': '   '}


def print_board(data):
    print(data['top-L'] + '|' + data['top-M'] + '|' + data['top-R'])
    print('---+---+---')
    print(data['mid-L'] + '|' + data['mid-M'] + '|' + data['mid-R'])
    print('---+---+---')
    print(data['bot-L'] + '|' + data['bot-M'] + '|' + data['bot-R'])


turn = ' X '

for i in range(9):
    print_board(data)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    data[move] = turn  # overwrites value at input() key location

    # checks who went, X's or O's, and updates 'turn' variable for the next move
    if turn == ' X ':
        turn = ' O '
    else:
        turn = ' X '

print_board(data)
