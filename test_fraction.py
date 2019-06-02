import unittest
from fraction import *

class TestFraction(unittest.TestCase):
	def test_init(self):
		f = Fraction(1, 2)
		self.assertEqual(f.numerator, 1)
		self.assertEqual(f.denominator, 2)

		f = Fraction(1, -2)
		self.assertEqual(f.numerator, -1)
		self.assertEqual(f.denominator, 2)

		# Exceptions
		self.assertRaises(ValueError, Fraction, 1, 0)

	def test_expand(self):
		f = Fraction(1, 2)
		f.expand(5)
		self.assertEqual(f, Fraction(5, 10, False, False))

		f = Fraction(-1, 2)
		f.expand(-1)
		self.assertEqual(f, Fraction(1, -2, False, False))

		# Exceptions
		f = Fraction(1, 2)
		self.assertRaises(ValueError, f.expand, 0)

	def test_reduce(self):
		f = Fraction(5, 10, False, False)
		f.reduce(5)
		self.assertEqual(f, Fraction(1, 2))

		# Exceptions
		f = Fraction(1, 2)
		self.assertRaises(ValueError, f.reduce, 2)

		f = Fraction(1, 2)
		self.assertRaises(ValueError, f.reduce, 2.0)

		f = Fraction(1, 2)
		self.assertRaises(ValueError, f.reduce, 0)

	def test_gcd(self):
		self.assertEqual(Fraction.gcd(27, 18), 9)
		self.assertEqual(Fraction.gcd(5, 10), 5)
		self.assertEqual(Fraction.gcd(10, 5), 5)
		self.assertEqual(Fraction.gcd(10, 0), 10)

	def test_max_reduce(self):
		f = Fraction(18, 27, False, False)
		f.max_reduce()
		self.assertEqual(f, Fraction(2, 3))

		f = Fraction(5, 10, False, False)
		f.max_reduce()
		self.assertEqual(f, Fraction(1, 2))

	def test_add_method(self):
		f1 = Fraction(5, 2)
		f2 = Fraction(3, 2)
		self.assertEqual(f1.add(f2), Fraction(4, 1))
		self.assertEqual(f1, Fraction(5, 2))
		self.assertEqual(f2, Fraction(3, 2))

		f1 = Fraction(1, 2)
		f2 = Fraction(1, 3)
		self.assertEqual(f1.add(f2), Fraction(5, 6))
		self.assertEqual(f1, Fraction(1, 2))
		self.assertEqual(f2, Fraction(1, 3))

	def test_add_left(self):
		f1 = Fraction(1, 2)
		f2 = Fraction(3, 2)
		self.assertEqual(f1 + f2, Fraction(2, 1))

		self.assertEqual(Fraction(1, 2) + 2, Fraction(5, 2))

	def test_add_right(self):
		f1 = Fraction(1, 2)
		f2 = Fraction(3, 2)
		self.assertEqual(f2 + f1, Fraction(2, 1))

		self.assertEqual(2 + Fraction(1, 2), Fraction(5, 2))

	def test_mul_scalar_method(self):
		f = Fraction(1, 3)
		s = 2
		self.assertEqual(f.multiply_scalar(s), Fraction(2, 3))
		self.assertEqual(f, Fraction(1, 3))

		f = Fraction(1, 3)
		s = 0
		self.assertEqual(f.multiply_scalar(s), Fraction(0, 3))
		self.assertEqual(f, Fraction(1, 3))

		f = Fraction(1, 3)
		s = -2
		self.assertEqual(f.multiply_scalar(s), Fraction(-2, 3))
		self.assertEqual(f, Fraction(1, 3))

		# Exceptions
		f = Fraction(1, 3)
		s = 2.0
		self.assertRaises(ValueError, f.multiply_scalar, s)

	def test_mul_fraction_method(self):
		f1 = Fraction(1, 2)
		f2 = Fraction(1, 3)
		self.assertEqual(f1.multiply_fraction(f2), Fraction(1, 6))
		self.assertEqual(f1, Fraction(1, 2))
		self.assertEqual(f2, Fraction(1, 3))

	def test_mul_left(self):
		f1 = Fraction(1, 2)
		f2 = Fraction(1, 3)
		self.assertEqual(f1 * f2, Fraction(1, 6))

		f = Fraction(1, 3)
		s = 2
		self.assertEqual(f * s, Fraction(2, 3))

	def test_mul_right(self):
		f1 = Fraction(1, 2)
		f2 = Fraction(1, 3)
		self.assertEqual(f2 * f1, Fraction(1, 6))

		f = Fraction(1, 3)
		s = 2
		self.assertEqual(s * f, Fraction(2, 3))

	def test_div_fraction_fraction_method(self):
		f1 = Fraction(1, 2)
		f2 = Fraction(1, 3)
		self.assertEqual(f1.divide_fraction_fraction(f2), Fraction(3, 2))
		self.assertEqual(f1, Fraction(1, 2))
		self.assertEqual(f2, Fraction(1, 3))

	def test_div_fraction_scalar_method(self):
		f = Fraction(1, 2)
		s = 3
		self.assertEqual(f.divide_fraction_scalar(s), Fraction(1, 6))
		self.assertEqual(f, Fraction(1, 2))

		# Exceptions
		f = Fraction(1, 2)
		s = 3.0
		self.assertRaises(ValueError, f.divide_fraction_scalar, s)

		f = Fraction(1, 2)
		s = 0
		self.assertRaises(ValueError, f.divide_fraction_scalar, s)

	def test_div_scalar_fraction_method(self):
		f = Fraction(1, 2)
		s = 3
		self.assertEqual(f.divide_scalar_fraction(s), Fraction(6, 1))
		self.assertEqual(f, Fraction(1, 2))

		# Exceptions
		f = Fraction(1, 2)
		s = 3.0
		self.assertRaises(ValueError, f.divide_scalar_fraction, s)

	def test_div_left(self):
		f1 = Fraction(1, 3)
		f2 = Fraction(1, 2)
		self.assertEqual(f1 / f2, Fraction(2, 3))

		f = Fraction(1, 3)
		s = 2
		self.assertEqual(f / s, Fraction(1, 6))

	def test_div_right(self):
		f1 = Fraction(1, 3)
		f2 = Fraction(1, 2)
		self.assertEqual(f2 / f1, Fraction(3, 2))

		f = Fraction(1, 3)
		s = 2
		self.assertEqual(s / f, Fraction(6, 1))

	def test_sub_left(self):
		f1 = Fraction(2, 3)
		f2 = Fraction(1, 3)
		self.assertEqual(f1 - f2, Fraction(1, 3))

		f1 = Fraction(1, 2)
		f2 = Fraction(1, 3)
		self.assertEqual(f1 - f2, Fraction(1, 6))

	def test_sub_right(self):
		f1 = Fraction(2, 3)
		f2 = Fraction(1, 3)
		self.assertEqual(f2 - f1, Fraction(-1, 3))

		f1 = Fraction(1, 2)
		f2 = Fraction(1, 3)
		self.assertEqual(f2 - f1, Fraction(-1, 6))
