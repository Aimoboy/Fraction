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

	@staticmethod
	def add(f1, f2):
		pass

	@staticmethod
	def multiply_scalar(f, s):
		pass

	@staticmethod
	def multiply_fraction(f1, f2):
		pass

	@staticmethod
	def divide_fraction_fraction(f1, f2):
		pass

	@staticmethod
	def divide_fraction_scalar(f, s):
		pass

	@staticmethod
	def divide_scalar_fraction(f, s):
		pass

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
