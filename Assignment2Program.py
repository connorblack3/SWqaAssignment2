import BMICalculator


print("Please enter height in two parts, feet and inches. You will be prompted these seperaty.")
heightFeet = input("Feet: ")
heightInches = input("Inches: ")
weight = input("Please enter your weight in pounds: ")

height = BMICalculator.convertHeight(heightFeet,heightInches)

BMI = BMICalculator.calcBMI(height, weight)

BMIcat = BMICalculator.detBMIcatagory(BMI)

print(BMIcat)
