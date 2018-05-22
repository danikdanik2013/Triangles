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

while True:
	if a < 0 or b < 0 or c < 0:
		print("uncorrect")
		break
	if a > b:
		if (a + b) < c or (a - b) > c:
			print("ucorrect")
	
	if b > a:
		if (b + a) < c or (b - a) > c:
			print("ucorrect")
			break
	if a == b:
		if (a + b) < c or (b + a) < c or (a - b) > c or (b - a) > c:
			print("uncorrect")
			break
	if a == b == c:
		print("That Equal triangle")
		break
		pass
	elif a == b and b == c and a == c:
		print("that Isosceles triangle")
		break
		pass
	else:
		print("that Versatile triangle")
		break
		pass
#