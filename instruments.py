instruments_i_play = ['piano', 'guitar', 'bass']

print('Do you play any instruments? (yes/no)')
if input() == 'yes':
    print('What instrument do you play?')
    users_instrument = input()
    if users_instrument in instruments_i_play:
        print('I play', users_instrument, 'too!')
    else:
        print("I don't play", users_instrument +
              '. I play', instruments_i_play)
else:
    print("You're missing out, it's a lot of fun!")
