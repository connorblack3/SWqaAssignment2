import math
from flask import Flask, request
from BMICalculator import BMI


app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():


    feet = request.values.get('feet', default="1", type = float)
    print(feet)
    inch = request.values.get('inch', default = "1", type = float)
    print(inch)
    weight = request.values.get('weight', default = "200", type = float)
    print(weight)

    return_value = BMI(feet, inch, weight)
    return return_value