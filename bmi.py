import math
from flask import Flask, request
from BMICalculator import BMI


app = Flask(__name__)

@app.route('/bmi', methods=['GET'])
def hello_world():


    args = request.args
    print (args)
    feet = args.get('feet', default="1", type = float)
    print(feet)
    inch = args.get('inch', default = "1", type = float)
    print(inch)
    weight = args.get('weight', default = "200", type = float)
    print(weight)

    return_value = BMI(feet, inch, weight)
    print(return_value)
    return return_value