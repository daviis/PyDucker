"""
A python implementation of built in classes for looking at method signatures.

Modified on 2014-11-06
"""

class tuple(object):
	def __add__(self, value):
		"""
		Return self+value.
		@value:object
		"""
		return ()

	def __class__(self, it=None):
		"""
		tuple() -> empty tuple
		tuple(iterable) -> tuple initialized from iterable's items
		
		If the argument is a tuple, the return value is the same object.
		@it:iterable
		"""
		return ()

	def __contains__(self, obj):
		"""
		Return key in self.
		@obj:object
		"""
		return True

# 	def __delattr__(self, ???):
		"""
		Implement delattr(self, name).
		"""

# 	def __dir__(self, ???):
		"""
		__dir__() -> list
		default dir() implementation
		"""

# 	def __doc__(self, ???):
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

	def __eq__(self, tup):
		"""
		Return self==value.
		@tup:tuple
		"""
		return True

# 	def __format__(self, ):
		"""
		default object formatter
		"""

	def __ge__(self, val):
		"""
		Return self>=value.
		@val:tuple
		"""
		return True

	def __getattribute__(self, name):
		"""
		Return getattr(self, name).
		@name:str
		"""
		return ""

	def __getitem__(self, key):
		"""
		Return self[key].
		@key:str
		"""
		return ""

# 	def __getnewargs__(self, ):
		"""
		None
		"""

	def __gt__(self, val):
		"""
		Return self>value.
		@val:tuple
		"""
		return True

	def __hash__(self):
		"""
		Return hash(self).
		"""
		return 1

	def __init__(self, iter=None):
		"""
		Initialize self.  See help(type(self)) for accurate signature.
		@iter:iterable
		"""
		pass

	def __iter__(self):
		"""
		Implement iter(self).
		"""
		return iterable

	def __le__(self, val):
		"""
		Return self<=value.
		@val:tuple
		"""
		return True

	def __len__(self):
		"""
		Return len(self).
		"""
		return 1

	def __lt__(self, val):
		"""
		Return self<value.
		@val:tuple
		"""
		return True

	def __mul__(self, anInt):
		"""
		Return self*value.n
		@anInt:int
		"""
		return ()

	def __ne__(self, tup):
		"""
		Return self!=value.
		@tup:tuple
		"""
		return True

# 	def __new__(self, ???):
		"""
		Create and return a new object.  See help(type) for accurate signature.
		"""

# 	def __reduce__(self ):
		"""
		helper for pickle
		"""

# 	def __reduce_ex__(self, ???):
		"""
		helper for pickle
		"""

	def __repr__(self):
		"""
		Return repr(self).
		"""
		return ""

	def __rmul__(self, val):
		"""
		Return self*value.
		@val:int
		"""
		return ()

	def __setattr__(self, name, value):
		"""
		Implement setattr(self, name, value).
		@name:str
		@value:object
		"""
		return

	def __sizeof__(self):
		"""
		T.__sizeof__() -- size of T in memory, in bytes
		"""
		return 1

	def __str__(self):
		"""
		Return str(self).
		"""
		return ""

# 	def __subclasshook__(self, ???):
		"""
		Abstract classes can override this to customize issubclass().
		
		This is invoked early on by abc.ABCMeta.__subclasscheck__().
		It should return True, False or NotImplemented.  If it returns
		NotImplemented, the normal algorithm is used.  Otherwise, it
		overrides the normal algorithm (and the outcome is cached).
		
		"""

	def count(self, value):
		"""
		T.count(value) -> integer -- return number of occurrences of value
		@value:object
		"""
		return 1

	def index(self, value, start=None, stop=None):
		"""
		T.index(value, [start, [stop]]) -> integer -- return first index of value.
		Raises ValueError if the value is not present.
		@value:object
		@start:int
		@stop:int
		"""
		return 1

