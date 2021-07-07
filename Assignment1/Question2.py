# Write a Python code to calculate Combination (15,3)
import math

n=15 	# n = total number of objects
r=3		# r = number of choosing objects
nr=n-r	

n_fac= math.factorial(n)
r_fac= math.factorial(r)
nr_fac= math.factorial(nr)

Combination= int(n_fac/(r_fac*(nr_fac))) 	# Combination=n!/r!(n-r)!

print(Combination)

