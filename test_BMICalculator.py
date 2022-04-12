import unittest
import BMICalculator

class TestBMI(unittest.TestCase):

    def test_convertHeight(self):

       # self.assertEqual(BMICalculator.convertHeight(0,-1), "out of bounds")
        #self.assertEqual(BMICalculator.convertHeight(-2,12), "out of bounds")
        self.assertEqual(BMICalculator.convertHeight(1,0), 12)
        self.assertEqual(BMICalculator.convertHeight(2,11), 35)
        self.assertEqual(BMICalculator.convertHeight(0,4.79), 4.79)

    def test_calcBMI(self):
     #   self.assertEqual(BMICalculator.calcBMI(72, -190), "out of bounds")
      #  self.assertEqual(BMICalculator.calcBMI(72, 0), "out of bounds")
        self.assertEqual(BMICalculator.calcBMI(72, 190), 26.0)
        self.assertEqual(BMICalculator.calcBMI(64.5, 146.5), 25.3)


    def test_detBMIcatagory(self):

        self.assertEqual(BMICalculator.detBMIcatagory(18.4), "Underweight")
        self.assertEqual(BMICalculator.detBMIcatagory(18.5), "Normal Weight")
        self.assertEqual(BMICalculator.detBMIcatagory(24.9), "Normal Weight")
        self.assertEqual(BMICalculator.detBMIcatagory(25), "Overweight")
        self.assertEqual(BMICalculator.detBMIcatagory(29.9), "Overweight")
        self.assertEqual(BMICalculator.detBMIcatagory(30), "Obese")
        self.assertEqual(BMICalculator.detBMIcatagory(18.3), "Underweight")
        self.assertEqual(BMICalculator.detBMIcatagory(18.6), "Normal Weight")
