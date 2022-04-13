import math
from flask import Flask
from markupsafe import escape


def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper


app = Flask(bmi)

@app.route("/bmi/<fliat:feet>,<float:inches>,<float:weight>")
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
