# author    https://github.com/iroshanvidanage
# date      05/13/2023

def switch_values(a, b):

    a, b = b, a
    return a, b


value_1 = input('Input value 1: ')
value_2 = input('Input value 2: ')
[value_1, value_2] = switch_values(value_1, value_2)

print('Value 1 ', value_1, '.\nValue 2 ', value_2, '.')
