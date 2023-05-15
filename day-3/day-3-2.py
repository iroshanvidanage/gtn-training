# author    https://github.com/iroshanvidanage
# date      05/15/2023

# BMI 2.0

def bmi_cal(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)


def bmi_type(bmi_val):
    if bmi_val <= 18.5:
        return 'Under Weight'
    elif bmi_val <= 25:
        return 'Normal'
    elif bmi_val <= 30:
        return 'Over Weight'
    elif bmi_val <= 35:
        return 'Obese'
    else:
        return 'Clinically Obese'


weight = float(input('Enter weight in kgs: '))
height = float(input('Enter height in meters: '))
bmi_value = bmi_cal(weight, height)
bmi_ty = bmi_type(bmi_value)
print(f'Your bmi value is {bmi_value} and your clinical status is {bmi_ty}.')
