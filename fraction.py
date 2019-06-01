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
		Test if two fractions are equal.

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
