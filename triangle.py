#utf-8. Python 3.6
from math import degrees,  acos

import unittest



def triangle_ckeck(a, b, c):
	try:
		float(a)
		float(b)
		float(c)
	except (TypeError, ValueError):
		print ("помилка вводу")
		return "помилка вводу"

	def cheakk(a, b, c):
		if (a <= 0) or (b <= 0)  or (c <= 0):
			print (" не трикутник ")
			return " не трикутник "
		elif (a + b) <= c or (a + c) <= b or (b + c) <= a:
			print (" не трикутник ")
			return " не трикутник "
		else:
			a = int(a)
			b = int(b)
			c = int(c)
			fi_3 = round(acos((c ** 2 - a ** 2 - b ** 2)/(-2 * a * b)),2)
			fi_3 = round(degrees(fi_3),1)
			fi_2 = round(acos((a ** 2 - b ** 2 - c ** 2)/(-2 * b * c)),2)
			fi_2 = round(degrees(fi_2),1)
			fi_1 = round((180 - fi_2 - fi_3),1)
			if (a == b and b == c and c == a):
				print ('рівносторонній гострокутній')
				return 'рівносторонній гострокутній'
			elif a != b and b != c and c != a: 
				if fi_1 < 90  and fi_2 < 90 and fi_3 < 90:
					print ('різносторонній госторкутній')
					return "різносторонній гострокутній"
				elif fi_1 == 90  or  fi_2 == 90 or fi_3 == 90:
					print ('різносторонній прямокутній')
					return "різносторонній прямокутній"
				else:
					print ('різносторонній тупокутній')
					return "різносторонній тупокутній"
			elif (a == b or b == c or a == c):
				if (fi_1 < 90  and fi_2 < 90 and fi_3 < 90):
					print ('рівнобедренний гострокутній')
					return "рівнобедренний гострокутній"
				elif fi_1 == 90 or fi_2 == 90 or fi_3 == 90:
					print ('рівнобедренний прямокутній')
					return "рівнобедренний прямокутній"
				elif fi_3 > 90 or fi_2 > 90 or fi_1 > 90:
					print ('рівнобедренний тупокутній')
					return "рівнобедренний тупокутній"
	return cheakk(a, b ,c)


class TestTriangle(unittest.TestCase):
    def setUp(self):
        pass

 #   def test_pos1(self):
 #       x = triangle_ckeck(1, 2, 3)
 #       self.assertEqual(x, 'різносторонній гострокутній')
 #       x = triangle_ckeck(3, 2, 1)
 #       self.assertEqual(x, 'різносторонній гострокутній')
 #       x = triangle_ckeck(2, 3, 1)
 #       self.assertEqual(x, 'різносторонній гострокутній')

    def test_pos2(self):
        x = triangle_ckeck(5, 5, 3)
        self.assertEqual(x, 'рівнобедренний гострокутній')
        x = triangle_ckeck(5, 3, 5)
        self.assertEqual(x, 'рівнобедренний гострокутній')
        x = triangle_ckeck(3, 5, 5)
        self.assertEqual(x, 'рівнобедренний гострокутній')

    def test_pos3(self):
        x = triangle_ckeck(5, 5, 9)
        self.assertEqual(x, 'рівнобедренний тупокутній')
        x = triangle_ckeck(5, 9, 5)
        self.assertEqual(x, 'рівнобедренний тупокутній')
        x = triangle_ckeck(9, 5, 5)
        self.assertEqual(x, 'рівнобедренний тупокутній')

    def test_pos4(self):
        x = triangle_ckeck(2, 2, 2)
        self.assertEqual(x, 'рівносторонній гострокутній')

    def test_pos5(self):
        x = triangle_ckeck(5, 8, 12)
        self.assertEqual(x, 'різносторонній тупокутній')
        x = triangle_ckeck(12, 8, 5)
        self.assertEqual(x, 'різносторонній тупокутній')
        x = triangle_ckeck(8, 5, 12)
        self.assertEqual(x, 'різносторонній тупокутній')

    def test_pos6(self):
        x = triangle_ckeck(3, 4, 5)
        self.assertEqual(x, 'різносторонній прямокутній')
        x = triangle_ckeck(4, 3, 5)
        self.assertEqual(x, 'різносторонній прямокутній')
        x = triangle_ckeck(5, 4, 3)
        self.assertEqual(x, 'різносторонній прямокутній')

    def test_pos7(self):
        pass
        # x = triangle_ckeck(3, 4, 5)
        # self.assertEqual(x, 'рівнобедренний прямокутній')

    def test_neg1(self):
        x = triangle_ckeck(10, 2, 2)
        self.assertEqual(x, ' не трикутник ')
        x = triangle_ckeck(2, 10, 2)
        self.assertEqual(x, ' не трикутник ')
        x = triangle_ckeck(2, 2, 10)
        self.assertEqual(x, ' не трикутник ')

    def test_neg2(self):
        x = triangle_ckeck(0, 2, 2)
        self.assertEqual(x, ' не трикутник ')
        x = triangle_ckeck(2, 0, 2)
        self.assertEqual(x, ' не трикутник ')
        x = triangle_ckeck(2, 2, 0)
        self.assertEqual(x, ' не трикутник ')
        x = triangle_ckeck(2, 0, 0)
        self.assertEqual(x, ' не трикутник ')
        x = triangle_ckeck(0, 0, 0)
        self.assertEqual(x, ' не трикутник ')

    def test_neg3(self):
        x = triangle_ckeck(-1, 2, 3)
        self.assertEqual(x, ' не трикутник ')
        x = triangle_ckeck(1, -2, 3)
        self.assertEqual(x, ' не трикутник ')
        x = triangle_ckeck(1, 2, -3)
        self.assertEqual(x, ' не трикутник ')
        x = triangle_ckeck(-1, -2, -3)
        self.assertEqual(x, ' не трикутник ')

    def test_neg4(self):
        x = triangle_ckeck('a', 2, 3)
        self.assertEqual(x, 'помилка вводу')
        x = triangle_ckeck('a', 'b', 3)
        self.assertEqual(x, 'помилка вводу')
        x = triangle_ckeck('a', 'b', 'c')
        self.assertEqual(x, 'помилка вводу')

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
