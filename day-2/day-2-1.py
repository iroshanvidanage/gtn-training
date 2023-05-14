# author    https://github.com/iroshanvidanage
# date      05/14/2023

def digit_num(num):
    value = 0
    for _ in num:
        value += int(_)

    return value


# print(digit_num(str(input('Enter two digit number: '))))

#########################################################

two_digit_number = input('Enter two digit number: ')
# print(type(two_digit_number))
# int(two_digit_number)

try:
    int(two_digit_number)
    print(int(two_digit_number[0]) + int(two_digit_number[1]))
except ValueError as e:
    print('Enter only integer\n', e)
