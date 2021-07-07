# Write a Python code to calculate LCM of (25,55)

x=25
y=55

# To choose the greater number among them 
if x>y:
	greater=x		#  g = greater number
else:
	greater=y

while True:
	if ((greater%x==0) and (greater%y==0)):
		lcm = greater
		break
	greater+=1

print(lcm)

