import math


def convertHeight(feet, inches):
    height = 12 * float(feet) + float(inches)
    #int(height)
    if int(height) < 0:
        return "out of bounds"

    return height


def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

def calcBMI (height, weight):
    Newweight = float(weight) * 0.45
    Newheight = float(height) * 0.025

    Newheight = pow(Newheight, 2)

    BMI = Newweight / Newheight
    BMI = truncate(BMI,1)

    return BMI

def BMI (feet, inches, weight):
    
    height = 12 * float(feet) + float(inches)
    
    newWeight = float(weight) * 0.45
    newHeight = float(height) * 0.025
    
    newHeight = pow(newHeight, 2)
    
    bmi = newWeight / newHeight
    bmi = truncate(bmi,1)
    if (18.5 > float(bmi)):
        return "Underweight"
    if (18.5 <= float(bmi) and float(bmi) <=24.9):
        return "Normal Weight"
    if (25 <= float(bmi) and float(bmi) <= 29.9):
        return "Overweight"
    if (30 <= float(bmi)):
        return "Obese"

def detBMIcatagory (BMI):

    if (18.5 > float(BMI)):
        return "Underweight"
    if (18.5 <= float(BMI) and float(BMI) <=24.9):
        return "Normal Weight"
    if (25 <= float(BMI) and float(BMI) <= 29.9):
        return "Overweight"
    if (30 <= float(BMI)):
        return "Obese"
