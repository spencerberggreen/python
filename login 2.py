while True:
    age = input('Enter your age: ')
    if age.isdecimal():
        break
    print('Your age must contain only numeric characters.')

while True:
    password = input('Enter your password (no special characters)')
    if password.isalnum():
        break
    print('Passwords may only contain letters and numbers.')

print('Thank you')
