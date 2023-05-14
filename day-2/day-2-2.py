# author    https://github.com/iroshanvidanage
# date      05/14/2023

# BMI Calculator
def bmi_cal():
    weight = float(input('Enter weight in kgs: '))
    height = float(input('Enter height in meters: '))
    bmi = weight // (height ** 2)
    print(int(bmi))


bmi_cal()
