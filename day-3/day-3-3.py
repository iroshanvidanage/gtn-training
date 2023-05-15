# author    https://github.com/iroshanvidanage
# date      05/15/2023

# Leap Year
def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def leap_year2(year):
    return (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)


print(leap_year2(int(input('Enter year: '))))