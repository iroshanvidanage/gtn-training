# author    https://github.com/iroshanvidanage
# date      05/14/2023

# your life in weeks

import datetime


def life_cal(birth_day):
    today = datetime.date.today()
    b_day = datetime.date.fromisoformat(birth_day)
    date_diff = today - b_day
    days_left = 90 * 365 - date_diff.days
    years = days_left // 365
    months = (days_left - years * 365) // 30
    days = (days_left - years * 365 - months * 30)

    print(f'As of today {today}, you have {years} year(s), {months} month(s) and {days} day(s) left.')


birthday = str(input('Enter your birthday in the following format yyyy-mm-dd: '))
life_cal(birthday)
# print(datetime.date.fromisoformat(birthday))
# print(datetime.date.today())
# print(datetime.date.today()-datetime.date.fromisoformat(birthday))
