import re  # regular expressions (regexes)
chapter = 1
'SPECIAL OPERATPORS'  # excludes / * - +
# exponent
2 ** 3  # 8

# remainder
10 % 3  # 1

# int division (rounds down)
10 // 3  # 3

'DATA TYPES'
# integer
7

# float
7.3

# string
'hi'

'STRING CONCATENATION'
# , will add a space
# + will not

'PRINT FUNCTION'

print()  # prints a blank line
print('hello')  # prints hello to the terminal

'INPUT FUNCTION'

# input() will wait for user to type something and press enter

'LEN FUNCTION'

len('hello')  # evaluates the length of string, 5
# len() will also return the number of items in an object
# e.g. number of items in a list

'STR, INT, AND FLOAT FUNCTIONS'
str(12)  # '12'
int('12')  # 12
float('12.0')  # 12.0
float(12)  # 12.0


chapter = 2

'BOOLEAN VALUES'
True
False

'COMPARISON OPERATORS'
all = True or False
# == Equal to

# != Not equal to

# <  Less than

# >  Greater than

# <= Less than or equal to

# >= Greater than or equal to

'BOOLEAN OPERATORS'
# and, or, not

one = 1
two = 2
three = 3
one and one == 1  # True, both variables == 1
one or two == 1  # True, any variable == 1
not False  # True

'FLOW CONTROL STATEMENTS'

# if statements will only execute when True
name = 'dave'
if name == 'dave':
    print('hello, dave')
else:
    print('hello, stranger')

# for loops only execute a finite amount
for index in range(3):
    print('this will print 3 times')

"""


jumping to chapter 6


"""


'ESCAPE CHARACTERS'

# adding a backslash \ to a string allows you to implement omitted string characters

'don\'t'  # don't

'\t'  # Tab

'\n'  # newline

'RAW STRINGS'

# place an r before the string quote to send backslashes to print
# very useful for Windows file paths (C:\users\Spencer\Documents)

print(r'\n')  # prints \n instead of a new line

'MULTI-LINE STRINGS'

# use triple quotes ('''text''') to make strings with multiple lines

'''this format
is also useful for
multi-line comments'''


'INDEXING AND SLICING STRINGS'

string = '012343456'

print(string[2:5])  # 234
print(string[:4])  # 0123

# [ : ]
# left side is the starting point, left blank means start with first index
# right side is the end point, but will not be included

'IN AND NOT OPERATORS WITH STRINGS'
# case sensitive

'he' and 'llo' in 'hello'  # True
'HELLO' not in 'hello'  # False

'STRING INSERTION'

name = 'dave'
age = 25

print('hi', name, 'I am', str(age), 'years old')
print('hi %s I am %s years old' % (name, age))
print(f'hi {name} I am {age} years old')

# hi dave I am 25 years old

'USEFUL STRING METHODS'

name = name.upper()  # dave -> DAVE
name = name.lower()  # DAVE -> dave

# 'dave'
name.isupper()  # False, must be all uppercase
name.islower()  # True, must be all lowercase
name.isalpha()  # True, must be only letters, not blank
name.isalnum()  # True, must be only letters AND/OR numbers, not blank
name.isdecimal()  # False, must be only numeric characters, not blank
name.isspace()  # False, must be only spaces, tabs, or new lines, not blank
name.istitle()  # False, first letter of each word must be capitalized
name.startswith('da')  # True, must start with the passed string
name.endswith('ve')  # True, must end with the passed string

'join() and split() methods'

# join() combines a list of strings into a single string
'-'.join(['one', 'two', 'three'])  # 'one-two-three'

# split() will separate the string into a list by via argument characters
'the red fox'.split(' ')  # ['the', 'red', 'fox']
'the-B-red-B-fox'.split('-B-')  # ['the', 'red', 'fox']

'splitting strings with the partition() method'

'Hello'.partition('l')  # ('He', 'l', 'lo')
'Hello'.partition('xyz')  # ('Hello', '', '')
# returns a tuple of 3 substrings. (before, separator, after)
# returns first occurence

before, sep, after = 'hello world'.partition(' ')
before  # 'hello'
after  # 'world'
sep  # ' '

'justifying text with rjust(), ljust() and center()'

'hello'.rjust(10)  # '     hello'
'hello'.ljust(10)  # 'hello     '
'hello'.center(10)  # '  hello   '

'hello'.center(10, '.')  # '..hello...'

'removing whitespace with strip(),rstrip(), and lstrip()'
# strip removes the argument from the beginning and ends of the string
text = '   hello world   '
text.strip()  # 'hello world'
text.lstrip()  # 'hello world   '
text.rstrip()  # '   hello world'
text.strip('l')  # 'hello world'
text.strip('h')  # 'ello world'

text = 'spamspamhello worldspamspam'
text.strip('psam')  # 'hello world'

# Passing 'psam' creates occurences of 'p', 's', 'a', 'm' and will
# remove them from the ends of the string.

'Unicode code point ord() and chr()'

# ord() shows the unicode number of the argument(character)
ord('A')  # 65
chr(65)  # 'A'
# chr() shows the unicode symbol of the argument(number)


"""

Chapter 7

Pattern matching with regular expressions

"""

'finding patterns of text with regular expressions'


# \d stands for digit character (0-9)

'scanning text for phone numbers'

# \d\d\d-\d\d\d-\d\d\d\d
# is the same as
# \d{3}-\d{3}-\d{4}
