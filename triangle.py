#utf-8. Python 3.6
from math import acos, degrees


while True:
	try:
		a = float(input('Enter first side: '))
		float(a)
		break
	except ValueError:
		print("Enter float number!")
		pass
while True:		
	try:
		b = float(input('Enter second side: '))
		float(b)
		break
	except ValueError:
		print("Enter float number!")
		pass
while True:
	try:
		c = float(input('Enter third side: '))
		float(c)
		break
	except ValueError:
		print("Enter float number!")
		pass

a = int(a)
b = int(b)
c = int(c)

fi_3 = acos((c ** 2 - a ** 2 - b ** 2)/(-2 * a * b))
fi_3 = degrees(fi_3)
fi_2 = acos((a ** 2 - b ** 2 - c ** 2)/(-2 * b * c))
fi_2 = degrees(fi_2)
fi_1 = 180 - fi_3 - fi_2
while True:
	if a < 0 or b < 0 or c < 0:
		print("uncorrect")
		break
	elif a > b:
		if (a + b) < c or (a - b) > c or (a + b) == c:
			print("ucorrect")
			break
	elif b > a:
		if (b + a) < c or (b - a) > c or (b + a) == c :
			print("ucorrect")
			break
	elif a == b:
		if (a + b) < c or (b + a) < c or (a - b) > c or (b - a) > c or (a + b) == c:
			print("uncorrect")
			break
	elif a > c:
		if (a + c) < b or (a - c) > b or (a + c) == b:
			print("ucorrect")
			break
	elif c > a:
		if (c + a) < b or (c - a) > b or (c + a) == b:
			print("uncorrect")
			break
	elif a == c:
		if (a + c) < c or (c + c) < c or (a - c) > b or (c - a) > b or (c + a) == b:
			print("uncorrect")
			break
	elif b > c:
		if (b + c) < a or (b - c) > a or (b + c) == a :
			print("uncorrect")
			break
	elif c > b:	
		if (c + b) < a or (c - b) > a or (c + b) == a:
			print("uncorrect")
			break
	elif b == c:
		if (b + c) < a or (c + b) < a or (c - b) > a or (b - c) > a or (b + c ) == a:
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
	elif fi_1 == fi_2 == fi_3:
		print("that Acute triangle")  
		break
	elif fi_1 > 90 or fi_2 > 90 or fi_3 > 90:
		print("that Obstuse triangle")
		break
	elif fi_1 == 90 or fi_2 == 90 or fi_3 == 90:
		print("that Rectangular triangle")
		break
	else:
		print("that Versatile triangle")
		break
		pass
