#utf-8. Python 3.6
while True:
	a = float(input('Enter first side: '))
	try:
		float(a)
		break
	except ValueError:
		print("Enter float number!")
		pass
while True:		
	b = float(input('Enter second side: '))
	try:
		float(b)
		break
	except ValueError:
		print("Enter float number!")
		pass
while True:
	c = float(input('Enter third side: '))
	try:
		float(c)
		break
	except ValueError:
		print("Enter float number!")
		pass	
if a == b == c:
	print("That Equal triangle")
elif a == b and b == c and a == c:
	print("that Isosceles triangle")
else:
	print("that Versatile triangle")
#