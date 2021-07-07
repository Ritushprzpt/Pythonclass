 #Write a Python code that takes the degree as input from the user and convert it into radian.
import math #for the value of math.pi

deg = int(input("Enter the value in degree to convert into radian:"))

rad= float(deg*(math.pi/180))

print(rad)

