print("hello python") # in python this is the comment, you know it

# literal constants

#'this is a literal constant'
# 5 # this is also a literal
# 1.25 # this also

# numbers

# mainly of two types: int's and float's

# strings

print("this is a double quoted string")
print('this is a single quoted string')
print("there is no difference between single and double quoted string")

# triple quote string denoted by '''

''' this is a triple quoted string
it supports new lines and single and double quote strings
"this is a double quoted string inside a triple quote string"
'this is a single quoted string inside a triple quote string' ''' # this again is a comment

''' strigs are immutable '''


# we can construct strings using :

# format method

age = 20
name = 'Sunny'

print('{0} was {1} years old'.format(name, age))
print("why is {0} playing with that python?".format(name)) # the numbers 0 and 1 are optional

print("this is {} using format method without numbers in string".format(name))


# but a shorter way to use strings is f-string for format-strings

print(f'this is a format string where the variables are part of the string like \
    name is {name} and age is {age}. no need for format method')

print('{0:.3f}'.format(9.0/3))
print('{0:_^11}'.format('hello'))
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Pythons'))



print('print method always ends with a new line')
print('to print multiple strings', end=' ')
print('on a single line')

print('this is a normal string where escape sequence like \n will be handled')
print(r'this is a raw string where escape sequences like \n will not be handled and will be printed as is')
print(r'remember, raw strings are prefixed with a \'r\' character before the string literal')



