''' Ask enter to enter two numbers (say, a and b).
 Generate two random numbers between those two numbers and
 find a combination of these two newly generated random numbers.'''

import math         # importing math module
import random       # importing random module

a= int(input("Enter the starting number:"))
b= int(input("Enter the ending number:"))

num1= random.randint(a,b)		# to generate a random number
num2 = random.randint(a,b)

# factorizing the number
num1fac= math.factorial(num1)       # n!
num2fac= math.factorial(num2)       # r!

# testing
print(num1)
print(num2)


if num1<num2:			# swaping the value if the num1 is smaller then num2
    num1,num2=num2,num1


subnum=num1-num2	# (n-r)


subnum2fac = math.factorial(subnum)	# factorizing the subnum -- (n-r)!


combination=int(num1fac/(num2fac*(subnum2fac)))	# combination formula


print(combination)