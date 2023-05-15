# author    https://github.com/iroshanvidanage
# date      05/15/2023

def pizza_order():
    pizza_size = str(input('Input s, m, l: ')).upper()
    pepp = str(input('Pepperoni y / n ? ')).upper()

    if pizza_size == 'S':
        bill = 15
    elif pizza_size == 'M':
        bill = 20
    else:
        bill = 25

    if pepp == 'Y' and pizza_size == 'S':
        bill += 2
    elif pepp == 'Y' and pizza_size != 'S':
        bill += 3
    else:
        pass

    print(f'Your pizza order is {bill}.')


pizza_order()
