"""
A python implementation of built in classes for looking at method signatures.

Modified on 2014-11-14
"""

class tuple():
	def __add__(self, ???):
		"""
		Return self+value
		"""

	def __class__(self, ???):
		"""
		tuple() -> empty tuple
		tuple(iterable) -> tuple initialized from iterable's items
		
		If the argument is a tuple, the return value is the same object.
		"""

	def __contains__(self, ???):
		"""
		Return key in self.
		"""

	def __delattr__(self, ???):
		"""
		Implement delattr(self, name).
		"""

	def __doc__(self, ???):
		"""
		str(object='') -> string
		str(bytes_or_buffer[, encoding[, errors]]) -> str
		
		Create a new string object from the given object. If encoding or
		errors is specified, then the object msut expose a data buffer
		that will be decoded using the given encoding and eror handler.
		Otherwise, returns the result of object.__str__() (if defined)
		or repr(object).
		encoding defaults to sys.getdefaultencoding().
		errors defaults to 'strict'.
		"""

	def __eq__(self, ???):
		"""
		Return self==value.
		"""

	def __format__(self, ???):
		"""
		default object formatter
		"""

	def __ge__(self, ???):
		"""
		Return self>=value.
		"""

	def __getattribute__(self, ???):
		"""
		Return getattr(self, name).
		"""

	def __getitem__(self, ???):
		"""
		Return self[key].
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
		Initialize self. see help(type(x)) for signature
		"""

	def __iter__(self, ???):
		"""
		Implement iter(self).
		"""

	def __le__(self, ???):
		"""
		Return self<=value.
		"""

	def __len__(self, ???):
		"""
		Return len(self)
		"""

	def __lt__(self, ???):
		"""
		Return self<value.
		"""

	def __mul__(self, ???):
		"""
		Return self*value.n
		"""

	def __ne__(self, ???):
		"""
		Retur self!=value.
		"""

	def __new__(self, ???):
		"""
		Create and return a new object. See help(type) for accurate signature.
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

	def __rmul__(self, ???):
		"""
		Return self*value.
		"""

	def __setattr__(self, ???):
		"""
		Implement setattr(self, name, value).
		"""

	def __sizeof__(self, ???):
		"""
		T.__sizeof__() -- size of T in memory, in bytes
		"""

	def __str__(self, ???):
		"""
		Return str(self).
		"""

	def __subclasshook__(self, ???):
		"""
		Abstract classes can override this to customize issubclass().
		
		This is invoked early on by abc.ABCMeta.__subclasscheck__().
		It should return True, False or NotImplemented.  If it returns
		NotImplemented, the normal algorithm is used.  Otherwise, it
		overrides the normal algorithm (and the outcome is cached).
		
		"""

	def count(self, ???):
		"""
		T.count(value) -> integer -- return number of occurrences of value
		"""

	def index(self, ???):
		"""
		T.index(value, [start, [stop]]) -> integer -- return first index of value.
		Raises ValueError if the value is not present.
		"""

