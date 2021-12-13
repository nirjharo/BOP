number = 23
running = True


while running:

    guess = int(input('enter an integer : '))

    if guess == number:
        # this is a new block which starts with intendati0n
        print('congrats, you guessed it.')
        running = False
    elif guess < number:
        print('No, it is a little higher')
    else:
        print('No, it is a little lower')

else:
    print('While loop is over')


print('Done')

