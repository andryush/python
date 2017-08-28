print('''
HELLO, WELCOME TO MY PLACE
YOU ARE IN THE DARK ROOM WITh TWO DOORS
WHICH DOOR WOULD YOU LIKE TO ENTER
??? 1 OR 2 ???
''')

door = input('> ')

if door == '1':
    print('You entered to 1 door and you see bear eating cake, what will you do?')
    print('1 - Take cake from bear')
    print('2 - Scream to the bear')
    decision = input('> ')
    if decision == '1':
        print('Nice, bear eats your left hand, you are dead')
    elif decision == '2':
        print('Bear give you a CHAPALAX, you are dead')
    else:
        print('It\'s the smartest answer not to answer 1 or 2 :)))')

elif door == '2':
    print('You are in 2 door. There is a strange voice asking you: What is the name of Vito Coreone\'s youngest son?')
    print('1: Michael')
    print('2: Mikele')
    print('3: Sonny')
    son = input('> ')
    if son == '1' or son == '2':
        print('Excellent')
        print('The voice is manto and gonne')
    else:
        print('Who are you? You don\'t know Michael Corleone?')
        print('The strange voice give you a chapalax')

else:
    print('When you will be free, come back and play idiot, i said 1 or 2!!!')
