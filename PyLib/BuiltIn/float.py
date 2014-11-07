"""
A python implementation of built in classes for looking at method signatures.

Modified on 2014-11-06
"""

class float():
	def __abs__(self, ???):
		"""
		abs(self)
		"""

	def __add__(self, ???):
		"""
		Return self+value.
		"""

	def __bool__(self, ???):
		"""
		self != 0
		"""

	def __class__(self, ???):
		"""
		float(x) -> floating point number
		
		Convert a string or number to a floating point number, if possible.
		"""

	def __delattr__(self, ???):
		"""
		Implement delattr(self, name).
		"""

	def __dir__(self, ???):
		"""
		__dir__() -> list
		default dir() implementation
		"""

	def __divmod__(self, ???):
		"""
		Return divmod(self, value).
		"""

	def __doc__(self, ???):
		"""
		str(object='') -> str
		str(bytes_or_buffer[, encoding[, errors]]) -> str
		
		Create a new string object from the given object. If encoding or
		errors is specified, then the object must expose a data buffer
		that will be decoded using the given encoding and error handler.
		Otherwise, returns the result of object.__str__() (if defined)
		or repr(object).
		encoding defaults to sys.getdefaultencoding().
		errors defaults to 'strict'.
		"""

	def __eq__(self, ???):
		"""
		Return self==value.
		"""

	def __float__(self, ???):
		"""
		float(self)
		"""

	def __floordiv__(self, ???):
		"""
		Return self//value.
		"""

	def __format__(self, ???):
		"""
		float.__format__(format_spec) -> string
		
		Formats the float according to format_spec.
		"""

	def __ge__(self, ???):
		"""
		Return self>=value.
		"""

	def __getattribute__(self, ???):
		"""
		Return getattr(self, name).
		"""

	def __getformat__(self, ???):
		"""
		float.__getformat__(typestr) -> string
		
		You probably don't want to use this function.  It exists mainly to be
		used in Python's test suite.
		
		typestr must be 'double' or 'float'.  This function returns whichever of
		'unknown', 'IEEE, big-endian' or 'IEEE, little-endian' best describes the
		format of floating point numbers used by the C type named by typestr.
		"""

	def __getnewargs__(self, ???):
		"""
		None
		"""

	def __gt__(self, ???):
		"""
		Return self>value.
		"""

	def __hash__(self, ???):
		"""
		Return hash(self).
		"""

	def __init__(self, ???):
		"""
		Initialize self.  See help(type(self)) for accurate signature.
		"""

	def __int__(self, ???):
		"""
		int(self)
		"""

	def __le__(self, ???):
		"""
		Return self<=value.
		"""

	def __lt__(self, ???):
		"""
		Return self<value.
		"""

	def __mod__(self, ???):
		"""
		Return self%value.
		"""

	def __mul__(self, ???):
		"""
		Return self*value.
		"""

	def __ne__(self, ???):
		"""
		Return self!=value.
		"""

	def __neg__(self, ???):
		"""
		-self
		"""

	def __new__(self, ???):
		"""
		Create and return a new object.  See help(type) for accurate signature.
		"""

	def __pos__(self, ???):
		"""
		+self
		"""

	def __pow__(self, ???):
		"""
		Return pow(self, value, mod).
		"""

	def __radd__(self, ???):
		"""
		Return value+self.
		"""

	def __rdivmod__(self, ???):
		"""
		Return divmod(value, self).
		"""

	def __reduce__(self, ???):
		"""
		helper for pickle
		"""

	def __reduce_ex__(self, ???):
		"""
		helper for pickle
		"""

	def __repr__(self, ???):
		"""
		Return repr(self).
		"""

	def __rfloordiv__(self, ???):
		"""
		Return value//self.
		"""

	def __rmod__(self, ???):
		"""
		Return value%self.
		"""

	def __rmul__(self, ???):
		"""
		Return value*self.
		"""

	def __round__(self, ???):
		"""
		Return the Integral closest to x, rounding half toward even.
		When an argument is passed, work like built-in round(x, ndigits).
		"""

	def __rpow__(self, ???):
		"""
		Return pow(value, self, mod).
		"""

	def __rsub__(self, ???):
		"""
		Return value-self.
		"""

	def __rtruediv__(self, ???):
		"""
		Return value/self.
		"""

	def __setattr__(self, ???):
		"""
		Implement setattr(self, name, value).
		"""

	def __setformat__(self, ???):
		"""
		float.__setformat__(typestr, fmt) -> None
		
		You probably don't want to use this function.  It exists mainly to be
		used in Python's test suite.
		
		typestr must be 'double' or 'float'.  fmt must be one of 'unknown',
		'IEEE, big-endian' or 'IEEE, little-endian', and in addition can only be
		one of the latter two if it appears to match the underlying C reality.
		
		Override the automatic determination of C-level floating point type.
		This affects how floats are converted to and from binary strings.
		"""

	def __sizeof__(self, ???):
		"""
		__sizeof__() -> int
		size of object in memory, in bytes
		"""

	def __str__(self, ???):
		"""
		Return str(self).
		"""

	def __sub__(self, ???):
		"""
		Return self-value.
		"""

	def __subclasshook__(self, ???):
		"""
		Abstract classes can override this to customize issubclass().
		
		This is invoked early on by abc.ABCMeta.__subclasscheck__().
		It should return True, False or NotImplemented.  If it returns
		NotImplemented, the normal algorithm is used.  Otherwise, it
		overrides the normal algorithm (and the outcome is cached).
		
		"""

	def __truediv__(self, ???):
		"""
		Return self/value.
		"""

	def __trunc__(self, ???):
		"""
		Return the Integral closest to x between 0 and x.
		"""

	def as_integer_ratio(self, ???):
		"""
		float.as_integer_ratio() -> (int, int)
		
		Return a pair of integers, whose ratio is exactly equal to the original
		float and with a positive denominator.
		Raise OverflowError on infinities and a ValueError on NaNs.
		
		>>> (10.0).as_integer_ratio()
		(10, 1)
		>>> (0.0).as_integer_ratio()
		(0, 1)
		>>> (-.25).as_integer_ratio()
		(-1, 4)
		"""

	def conjugate(self, ???):
		"""
		Return self, the complex conjugate of any float.
		"""

	def fromhex(self, ???):
		"""
		float.fromhex(string) -> float
		
		Create a floating-point number from a hexadecimal string.
		>>> float.fromhex('0x1.ffffp10')
		2047.984375
		>>> float.fromhex('-0x1p-1074')
		-5e-324
		"""

	def hex(self, ???):
		"""
		float.hex() -> string
		
		Return a hexadecimal representation of a floating-point number.
		>>> (-0.1).hex()
		'-0x1.999999999999ap-4'
		>>> 3.14159.hex()
		'0x1.921f9f01b866ep+1'
		"""

	def imag(self, ???):
		"""
		float(x) -> floating point number
		
		Convert a string or number to a floating point number, if possible.
		"""

	def is_integer(self, ???):
		"""
		Return True if the float is an integer.
		"""

	def real(self, ???):
		"""
		float(x) -> floating point number
		
		Convert a string or number to a floating point number, if possible.
		"""

