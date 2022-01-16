def print_list(itemdict, leftwidth, rightwidth):
    print('Shopping List'.center(leftwidth + rightwidth, '-'))
    for k, v in itemdict.items():
        print(k.ljust(leftwidth, '.')+str(v).rjust(rightwidth))


shopping_list = {'apples': 4, 'cookies': 8, 'napkins': 20, 'cups': 6}

print_list(shopping_list, 12, 5)
print_list(shopping_list, 20, 6)
