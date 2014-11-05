class int():
	def __abs__(???):
		"""
		abs(self)
		"""

	def __add__(???):
		"""
		Return self+value.
		"""

	def __and__(???):
		"""
		Return self&value.
		"""

	def __bool__(???):
		"""
		self != 0
		"""

	def __ceil__(???):
		"""
		Ceiling of an Integral returns itself.
		"""

	def __class__(???):
		"""
		int(x=0) -> integer
		int(x, base=10) -> integer
		
		Convert a number or string to an integer, or return 0 if no arguments
		are given.  If x is a number, return x.__int__().  For floating point
		numbers, this truncates towards zero.
		
		If x is not a number or if base is given, then x must be a string,
		bytes, or bytearray instance representing an integer literal in the
		given base.  The literal can be preceded by '+' or '-' and be surrounded
		by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
		Base 0 means to interpret the base from the string as an integer literal.
		>>> int('0b100', base=0)
		4
		"""

	def __delattr__(???):
		"""
		Implement delattr(self, name).
		"""

	def __dir__(???):
		"""
		__dir__() -> list
		default dir() implementation
		"""

	def __divmod__(???):
		"""
		Return divmod(self, value).
		"""

	def __doc__(???):
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

	def __eq__(???):
		"""
		Return self==value.
		"""

	def __float__(???):
		"""
		float(self)
		"""

	def __floor__(???):
		"""
		Flooring an Integral returns itself.
		"""

	def __floordiv__(???):
		"""
		Return self//value.
		"""

	def __format__(???):
		"""
		None
		"""

	def __ge__(???):
		"""
		Return self>=value.
		"""

	def __getattribute__(???):
		"""
		Return getattr(self, name).
		"""

	def __getnewargs__(???):
		"""
		None
		"""

	def __gt__(???):
		"""
		Return self>value.
		"""

	def __hash__(???):
		"""
		Return hash(self).
		"""

	def __index__(???):
		"""
		Return self converted to an integer, if self is suitable for use as an index into a list.
		"""

	def __init__(???):
		"""
		Initialize self.  See help(type(self)) for accurate signature.
		"""

	def __int__(???):
		"""
		int(self)
		"""

	def __invert__(???):
		"""
		~self
		"""

	def __le__(???):
		"""
		Return self<=value.
		"""

	def __lshift__(???):
		"""
		Return self<<value.
		"""

	def __lt__(???):
		"""
		Return self<value.
		"""

	def __mod__(???):
		"""
		Return self%value.
		"""

	def __mul__(???):
		"""
		Return self*value.
		"""

	def __ne__(???):
		"""
		Return self!=value.
		"""

	def __neg__(???):
		"""
		-self
		"""

	def __new__(???):
		"""
		Create and return a new object.  See help(type) for accurate signature.
		"""

	def __or__(???):
		"""
		Return self|value.
		"""

	def __pos__(???):
		"""
		+self
		"""

	def __pow__(???):
		"""
		Return pow(self, value, mod).
		"""

	def __radd__(???):
		"""
		Return value+self.
		"""

	def __rand__(???):
		"""
		Return value&self.
		"""

	def __rdivmod__(???):
		"""
		Return divmod(value, self).
		"""

	def __reduce__(???):
		"""
		helper for pickle
		"""

	def __reduce_ex__(???):
		"""
		helper for pickle
		"""

	def __repr__(???):
		"""
		Return repr(self).
		"""

	def __rfloordiv__(???):
		"""
		Return value//self.
		"""

	def __rlshift__(???):
		"""
		Return value<<self.
		"""

	def __rmod__(???):
		"""
		Return value%self.
		"""

	def __rmul__(???):
		"""
		Return value*self.
		"""

	def __ror__(???):
		"""
		Return value|self.
		"""

	def __round__(???):
		"""
		Rounding an Integral returns itself.
		Rounding with an ndigits argument also returns an integer.
		"""

	def __rpow__(???):
		"""
		Return pow(value, self, mod).
		"""

	def __rrshift__(???):
		"""
		Return value>>self.
		"""

	def __rshift__(???):
		"""
		Return self>>value.
		"""

	def __rsub__(???):
		"""
		Return value-self.
		"""

	def __rtruediv__(???):
		"""
		Return value/self.
		"""

	def __rxor__(???):
		"""
		Return value^self.
		"""

	def __setattr__(???):
		"""
		Implement setattr(self, name, value).
		"""

	def __sizeof__(???):
		"""
		Returns size in memory, in bytes
		"""

	def __str__(???):
		"""
		Return str(self).
		"""

	def __sub__(???):
		"""
		Return self-value.
		"""

	def __subclasshook__(???):
		"""
		Abstract classes can override this to customize issubclass().
		
		This is invoked early on by abc.ABCMeta.__subclasscheck__().
		It should return True, False or NotImplemented.  If it returns
		NotImplemented, the normal algorithm is used.  Otherwise, it
		overrides the normal algorithm (and the outcome is cached).
		
		"""

	def __truediv__(???):
		"""
		Return self/value.
		"""

	def __trunc__(???):
		"""
		Truncating an Integral returns itself.
		"""

	def __xor__(???):
		"""
		Return self^value.
		"""

	def bit_length(???):
		"""
		int.bit_length() -> int
		
		Number of bits necessary to represent self in binary.
		>>> bin(37)
		'0b100101'
		>>> (37).bit_length()
		6
		"""

	def conjugate(???):
		"""
		Returns self, the complex conjugate of any int.
		"""

	def denominator(???):
		"""
		int(x=0) -> integer
		int(x, base=10) -> integer
		
		Convert a number or string to an integer, or return 0 if no arguments
		are given.  If x is a number, return x.__int__().  For floating point
		numbers, this truncates towards zero.
		
		If x is not a number or if base is given, then x must be a string,
		bytes, or bytearray instance representing an integer literal in the
		given base.  The literal can be preceded by '+' or '-' and be surrounded
		by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
		Base 0 means to interpret the base from the string as an integer literal.
		>>> int('0b100', base=0)
		4
		"""

	def from_bytes(???):
		"""
		int.from_bytes(bytes, byteorder, *, signed=False) -> int
		
		Return the integer represented by the given array of bytes.
		
		The bytes argument must either support the buffer protocol or be an
		iterable object producing bytes.  Bytes and bytearray are examples of
		built-in objects that support the buffer protocol.
		
		The byteorder argument determines the byte order used to represent the
		integer.  If byteorder is 'big', the most significant byte is at the
		beginning of the byte array.  If byteorder is 'little', the most
		significant byte is at the end of the byte array.  To request the native
		byte order of the host system, use `sys.byteorder' as the byte order value.
		
		The signed keyword-only argument indicates whether two's complement is
		used to represent the integer.
		"""

	def imag(???):
		"""
		int(x=0) -> integer
		int(x, base=10) -> integer
		
		Convert a number or string to an integer, or return 0 if no arguments
		are given.  If x is a number, return x.__int__().  For floating point
		numbers, this truncates towards zero.
		
		If x is not a number or if base is given, then x must be a string,
		bytes, or bytearray instance representing an integer literal in the
		given base.  The literal can be preceded by '+' or '-' and be surrounded
		by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
		Base 0 means to interpret the base from the string as an integer literal.
		>>> int('0b100', base=0)
		4
		"""

	def numerator(???):
		"""
		int(x=0) -> integer
		int(x, base=10) -> integer
		
		Convert a number or string to an integer, or return 0 if no arguments
		are given.  If x is a number, return x.__int__().  For floating point
		numbers, this truncates towards zero.
		
		If x is not a number or if base is given, then x must be a string,
		bytes, or bytearray instance representing an integer literal in the
		given base.  The literal can be preceded by '+' or '-' and be surrounded
		by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
		Base 0 means to interpret the base from the string as an integer literal.
		>>> int('0b100', base=0)
		4
		"""

	def real(???):
		"""
		int(x=0) -> integer
		int(x, base=10) -> integer
		
		Convert a number or string to an integer, or return 0 if no arguments
		are given.  If x is a number, return x.__int__().  For floating point
		numbers, this truncates towards zero.
		
		If x is not a number or if base is given, then x must be a string,
		bytes, or bytearray instance representing an integer literal in the
		given base.  The literal can be preceded by '+' or '-' and be surrounded
		by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
		Base 0 means to interpret the base from the string as an integer literal.
		>>> int('0b100', base=0)
		4
		"""

	def to_bytes(???):
		"""
		int.to_bytes(length, byteorder, *, signed=False) -> bytes
		
		Return an array of bytes representing an integer.
		
		The integer is represented using length bytes.  An OverflowError is
		raised if the integer is not representable with the given number of
		bytes.
		
		The byteorder argument determines the byte order used to represent the
		integer.  If byteorder is 'big', the most significant byte is at the
		beginning of the byte array.  If byteorder is 'little', the most
		significant byte is at the end of the byte array.  To request the native
		byte order of the host system, use `sys.byteorder' as the byte order value.
		
		The signed keyword-only argument determines whether two's complement is
		used to represent the integer.  If signed is False and a negative integer
		is given, an OverflowError is raised.
		"""

