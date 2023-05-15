# author    https://github.com/iroshanvidanage
# date      05/15/2023

def odd_or_even(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'


input_number = float(input('Enter number: '))
print(odd_or_even(input_number))
