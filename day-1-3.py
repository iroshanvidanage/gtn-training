# author    https://github.com/iroshanvidanage
# date      05/13/2023

def calculate_string(user_string):
    # without in built methods
    num = 0
    for _ in user_string:
        num += 1

    return num


u_string = str(input('Enter_user_name: '))
print(calculate_string(u_string))
print(len(u_string))
