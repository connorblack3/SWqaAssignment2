import BMICalculator
from flask import Flask

app = Flask(__name__)

@app.route("/")
def assignment2():
    print("Please enter height in two parts, feet and inches. You will be prompted these seperaty.")
    heightFeet = input("Feet: ")
    heightInches = input("Inches: ")
    weight = input("Please enter your weight in pounds: ")

    height = BMICalculator.convertHeight(heightFeet,heightInches)

    BMI = BMICalculator.calcBMI(height, weight)

    BMIcat = BMICalculator.detBMIcatagory(BMI)

    #print(BMIcat)

    return BMIcat
