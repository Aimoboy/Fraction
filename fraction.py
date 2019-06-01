class Fraction:
	def __init__(self, numerator, denominator):
		"""
		Summary:
		Initialize a fraction.

		Returns:
		A fraction instance.
		"""

		self.numerator = numerator
		self.denominator = denominator
		self.fix_sign()

	def __eq__(self, other):
		"""
		Summary:
		Check if two fractions are equal.

		Returns:
		True if they are equal else false.
		"""

		if self.numerator == other.numerator and self.denominator == other.denominator:
			return True
		return False

	def __str__(self):
		"""
		Summary:
		Override the to string method.

		Returns:
		A string representation of the fraction.
		"""

		if self.numerator == 0:
			return "0"
		elif self.denominator == 1:
			return str(self.numerator)
		else:
			return "{0}/{1}".format(self.numerator, self.denominator)

	def __neg__(self):
		"""
		Summary:
		Negate the fraction.

		Returns:
		The fraction negated.
		"""

		return Fraction(self.numerator * (-1), self.denominator)

	def __add__(self, other):
		"""
		Summary:
		Addition overload for fraction.

		Returns:
		The sum of self and other.
		"""

		if type(other) is Fraction:
			return Fraction.add(self, other)
		elif type(other) is int:
			return Fraction.add(self, Fraction(other, 1))
		else:
			return NotImplemented()

	def __radd__(self, other):
		"""
		Summary:
		Addition overload for fraction.

		Returns:
		The sum of self and other.
		"""

		return self + other

	def __mul__(self, other):
		"""
		Summary:
		Multiplication overload for fraction.

		Returns:
		The product of self and other.
		"""

		if type(other) is Fraction:
			return Fraction.multiply_fraction(self, other)
		elif type(other) is int:
			return Fraction.multiply_scalar(self, other)
		else:
			return NotImplemented()

	def __rmul__(self, other):
		"""
		Summary:
		Multiplication overload for fraction.

		Returns:
		The product of self and other.
		"""

		return self * other

	def __truediv__(self, other):
		"""
		Summary:
		Division overload for fraction.

		Returns:
		The result of dividing self and other.
		"""

		if type(other) is Fraction:
			return Fraction.divide_fraction_fraction(self, other)
		elif type(other) is int:
			return Fraction.divide_fraction_scalar(self, other)
		else:
			return NotImplemented()

	def __rtruediv__(self, other):
		"""
		Summary:
		Division overload for fraction.

		Returns:
		The result of dividing self and other.
		"""

		if type(other) is Fraction:
			return Fraction.divide_fraction_fraction(other, self)
		elif type(other) is int:
			return Fraction.divide_scalar_fraction(other, self)
		else:
			return NotImplemented()

	def __sub__(self, other):
		"""
		Summary:
		Subtraction overload for fraction.

		Returns:
		The result of subtracting self and other.
		"""

		if (type(other) is Fraction) or (type(other) is int):
			return self + (-other)
		else:
			return NotImplemented()

	def __rsub__(self, other):
		"""
		Summary:
		Subtraction overload for fraction.

		Returns:
		The result of subtracting self and other.
		"""

		if (type(other) is Fraction) or (type(other) is int):
			return (-self) + other
		else:
			return NotImplemented()

	@staticmethod
	def add(f1, f2):
		"""
		Summary:
		Add two fractions.

		Parameters:
		f1 (Fraction): The first fraction.
		f2 (Fraction): The second fraction.

		Returns:
		The sum of the fractions.
		"""

		if f1.denominator == f2.denominator:
			return Fraction(f1.numerator + f2.numerator, f1.denominator)

		f = Fraction.add(f1.expand(f2.denominator), f2.expand(f1.denominator))
		f = f.max_reduce()

		return f

	@staticmethod
	def multiply_scalar(f, s):
		"""
		Summary:
		Multiply a fraction with a scalar.

		Parameters:
		f (Fraction): The fraction.
		s (int): The scalar.

		Returns:
		The fraction multiplied with the scalar.
		"""

		if type(s) is float:
			raise ValueError("Multiply with a fraction rather than a float.")

		return Fraction(self.numerator * s, self.denominator)

	@staticmethod
	def multiply_fraction(f1, f2):
		"""
		Summary:
		Multiply the fraction with another fraction.

		Parameters:
		f1 (Fraction): The first fraction.
		f2 (Fraction): The second fraction.

		Returns:
		The product of the two fractions.
		"""

		f = Fraction(f1.numerator * f2.numerator, f1.denominator * f2.denominator)
		f = f.max_reduce()

		return f

	@staticmethod
	def divide_fraction_fraction(f1, f2):
		"""
		Summary:
		Divide fraction with another fraction.

		Parameters:
		f1 (Fraction): The first fraction.
		f2 (Fraction): The second fraction.

		Returns:
		The result of dividing the two fractions.
		"""

		f = Fraction(f1.numerator * f2.denominator, f1.denominator * f2.numerator)
		f = f.max_reduce()

		return f

	@staticmethod
	def divide_fraction_scalar(f, s):
		"""
		Summary:
		Divide a fraction with a scalar.

		Parameters:
		f (Fraction): The fraction.
		s (int): The scalar.

		Returns:
		The fraction divided with the scalar.
		"""

		if s == 0:
			raise ValueError("Cannot divide with 0.")

		if type(s) is float:
			raise ValueError("Divide with a fraction rather than a float.")

		f = Fraction(f.numerator, f.denominator * s)
		f = f.max_reduce()

		return f

	@staticmethod
	def divide_scalar_fraction(f, s):
		"""
		Summary:
		Divide a scalar with a fraction.

		Parameters:
		f (Fraction): The fraction.
		s (int): The scalar.

		Returns:
		The scalar divided with the fraction.
		"""

		if type(s) is float:
			raise ValueError("Divide with a fraction rather than a float.")

		f = Fraction(f.denominator * s, f.numerator)
		f = f.max_reduce()

		return f

	def expand(self, s):
		"""
		Summary:
		Expand a fraction with a scalar.

		Parameters:
		s (int): The scalar to expand with.

		Returns:
		The fraction expanded by s.
		"""

		if s == 0:
			raise ValueError("Cannot expand fraction by 0.")

		return Fraction(self.numerator * s, self.denominator * s)

	def reduce(self, s):
		"""
		Summary:
		Reduce the fraction with a scalar.

		Parameters:
		s (int): The scalar to reduce with.

		Returns:
		The fraction reduced by s.
		"""

		if s == 0:
			raise ValueError("Cannot reduce fraction by 0.")

		if type(s) is float:
			raise ValueError("Do not reduce with a float, use a fraction instead.")

		return Fraction(int(self.numerator / s), int(self.denominator / s))

	def max_reduce(self):
		"""
		Summary:
		Reduce a fraction as much as possible.

		Returns:
		The fraction reduced as much as possible.
		"""

		f = self.copy()
		gcd = Fraction.gcd(f.numerator, f.denominator)

		while gcd != 1:
			f.reduce(gcd)
			gcd = Fraction.gcd(f.numerator, f.denominator)

		return f

	@staticmethod
	def gcd(a, b):
		"""
		Summary:
		Finds the greatest common divisor (GCD) of two numbers.

		Parameters:
		a (int): The first number.
		b (int): The second number.

		Returns:
		The greatest common divisor of a and b.
		"""

		if a < 0 or b < 0:
			a = abs(a)
			b = abs(b)

		if a < b:
			return Fraction.gcd(b, a)

		if b == 0:
			return a

		return Fraction.gcd(b, a % b)

	def copy(self):
		"""
		Summary:
		Make a copy of the fraction.

		Returns:
		A copy of the fraction.
		"""

		return Fraction(self.numerator, self.denominator)

	def fix_sign(self):
		"""
		Summary:
		Make the denominator positive if it is negative.

		Returns:
		A fraction with a positive denominator.
		"""

		f = self.copy()

		if self.denominator < 0:
			f.expand(-1)

		return f
