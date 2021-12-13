while True:
    s = input('Enter something : ')
    if s == 'quit':
        print('exiting ...')
        breakpoint
    if len(s) < 3:
        print('The string is too small')
        continue
    print('Length of the string is ', len(s))
else:
    print('Done')


