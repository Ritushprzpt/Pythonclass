# Write a Python code to calculate Permutation (5,3).

import math		# importing math means module provide acces to mathematical functions defined by C

n=5 	# n = total no of objects
r=n-3	# r = selection of objects

n_factorial= math.factorial(n)
r_factorial= math.factorial(r)

permutation = int(n_factorial/r_factorial) 	# permutation = n!/(n-r)!

print(permutation)