class Fraction:
	def __init__(self, numerator, denominator, fix_sign=True, reduce_fraction=True):
		"""
		Summary:
		Initialize a fraction.

		Parameters:
		numerator (int): The numerator of the fraction.
		denomiinator (int): The denominator of the fraction.

		Returns:
		A fraction instance.
		"""

		if denominator == 0:
			raise ValueError("Denominator can not be 0.")

		self.numerator = numerator
		self.denominator = denominator

		if fix_sign:
			self.fix_sign()

		if reduce_fraction:
			self.max_reduce()

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
			return self.add(other)
		elif type(other) is int:
			return self.add(Fraction(other, 1))
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
			return self.multiply_fraction(other)
		elif type(other) is int:
			return self.multiply_scalar(other)
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
			return self.divide_fraction_fraction(other)
		elif type(other) is int:
			return self.divide_fraction_scalar(other)
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
			return other.divide_fraction_fraction(self)
		elif type(other) is int:
			return self.divide_scalar_fraction(other)
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

	def add(self, other):
		"""
		Summary:
		Add two fractions.

		Parameters:
		self (Fraction): This fraction.
		other (Fraction): The other fraction.

		Returns:
		The sum of the fractions.
		"""

		if self.denominator == other.denominator:
			return Fraction(self.numerator + other.numerator, self.denominator)

		self_copy = self.copy()
		other_copy = other.copy()

		self_copy.expand(other.denominator)
		other_copy.expand(self.denominator)

		f = Fraction.add(self_copy, other_copy)

		return f

	def multiply_scalar(self, s):
		"""
		Summary:
		Multiply a fraction with a scalar.

		Parameters:
		self (Fraction): This fraction.
		s (int): The scalar.

		Returns:
		The fraction multiplied with the scalar.
		"""

		if type(s) is float:
			raise ValueError("Multiply with a fraction rather than a float.")

		return Fraction(self.numerator * s, self.denominator)

	def multiply_fraction(self, other):
		"""
		Summary:
		Multiply the fraction with another fraction.

		Parameters:
		this (Fraction): This fraction.
		other (Fraction): The other fraction.

		Returns:
		The product of the two fractions.
		"""

		return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

	def divide_fraction_fraction(self, other):
		"""
		Summary:
		Divide fraction with another fraction.

		Parameters:
		self (Fraction): This fraction.
		other (Fraction): The other fraction.

		Returns:
		The result of dividing the two fractions.
		"""

		return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

	def divide_fraction_scalar(self, s):
		"""
		Summary:
		Divide a fraction with a scalar.

		Parameters:
		self (Fraction): This fraction.
		s (int): The scalar.

		Returns:
		The fraction divided with the scalar.
		"""

		if s == 0:
			raise ValueError("Cannot divide with 0.")

		if type(s) is float:
			raise ValueError("Divide with a fraction rather than a float.")

		return Fraction(self.numerator, self.denominator * s)

	def divide_scalar_fraction(self, s):
		"""
		Summary:
		Divide a scalar with a fraction.

		Parameters:
		self (Fraction): This fraction.
		s (int): The scalar.

		Returns:
		The scalar divided with the fraction.
		"""

		if type(s) is float:
			raise ValueError("Divide with a fraction rather than a float.")

		return Fraction(self.denominator * s, self.numerator)

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

		self.numerator = self.numerator * s
		self.denominator = self.denominator * s

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
			raise ValueError("Do not reduce with a float, use a fraction or int instead.")

		if self.numerator % s != 0 or self.denominator % s != 0:
			raise ValueError("Can only reduce by numbers that divide numerator and denominator.")

		self.numerator = int(self.numerator / s)
		self.denominator = int(self.denominator / s)

	def max_reduce(self):
		"""
		Summary:
		Reduce a fraction as much as possible.

		Returns:
		The fraction reduced as much as possible.
		"""

		gcd = Fraction.gcd(self.numerator, self.denominator)

		while gcd != 1:
			self.reduce(gcd)
			gcd = Fraction.gcd(self.numerator, self.denominator)

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
		"""

		if self.denominator < 0:
			self.numerator = -self.numerator
			self.denominator = -self.denominator
