import math


def convertHeight(feet, inches):
    height = 12 * float(feet) + float(inches)
    #int(height)
    if int(height) < 0:
        return "out of bounds"

    return height


def truncate(f, n):
    return math.floor(f * 10 ** n) / 10 ** n

def calcBMI (height, weight):
    Newweight = float(weight) * 0.45
    Newheight = int(height) * 0.025

    Newheight = pow(Newheight, 2)

    BMI = Newweight // Newheight
    BMI = truncate(BMI,1)

    return BMI

def detBMIcatagory (BMI):

    if (18.5 > float(BMI)):
        return "Underweight"
    if (18.5 <= float(BMI) and float(BMI) <=24.9):
        return "Normal Weight"
    if (25 <= float(BMI) and float(BMI) <= 29.9):
        return "Overweight"
    if (30 <= float(BMI)):
        return "Obese"