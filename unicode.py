'''
After reading about unicode in my textbook,
I was curious to see what a large range of
unicode looked like. This for loop can display
a wide array of unicode, and can be modified
by changing the range value.
'''
# unicode = []
# for i in range(50000):
#     unicode.append(chr(i+1))
#
# print(unicode)


# for i in range(50):
#     print((chr(9950 + i)).split('\n'))

unicode = []

for i in range(50):
    unicode.append(chr(9950 + i))

print(unicode) 