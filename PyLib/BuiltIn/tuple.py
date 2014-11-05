"""
A python implementation of built in classes for looking at method signatures.

Modified on 2014-11-05
"""

class tuple():
	def __add__(???):
		"""
		Return self+value.
		"""

	def __class__(???):
		"""
		tuple() -> empty tuple
		tuple(iterable) -> tuple initialized from iterable's items
		
		If the argument is a tuple, the return value is the same object.
		"""

	def __contains__(???):
		"""
		Return key in self.
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

	def __format__(???):
		"""
		default object formatter
		"""

	def __ge__(???):
		"""
		Return self>=value.
		"""

	def __getattribute__(???):
		"""
		Return getattr(self, name).
		"""

	def __getitem__(???):
		"""
		Return self[key].
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

	def __init__(???):
		"""
		Initialize self.  See help(type(self)) for accurate signature.
		"""

	def __iter__(???):
		"""
		Implement iter(self).
		"""

	def __le__(???):
		"""
		Return self<=value.
		"""

	def __len__(???):
		"""
		Return len(self).
		"""

	def __lt__(???):
		"""
		Return self<value.
		"""

	def __mul__(???):
		"""
		Return self*value.n
		"""

	def __ne__(???):
		"""
		Return self!=value.
		"""

	def __new__(???):
		"""
		Create and return a new object.  See help(type) for accurate signature.
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

	def __rmul__(???):
		"""
		Return self*value.
		"""

	def __setattr__(???):
		"""
		Implement setattr(self, name, value).
		"""

	def __sizeof__(???):
		"""
		T.__sizeof__() -- size of T in memory, in bytes
		"""

	def __str__(???):
		"""
		Return str(self).
		"""

	def __subclasshook__(???):
		"""
		Abstract classes can override this to customize issubclass().
		
		This is invoked early on by abc.ABCMeta.__subclasscheck__().
		It should return True, False or NotImplemented.  If it returns
		NotImplemented, the normal algorithm is used.  Otherwise, it
		overrides the normal algorithm (and the outcome is cached).
		
		"""

	def count(???):
		"""
		T.count(value) -> integer -- return number of occurrences of value
		"""

	def index(???):
		"""
		T.index(value, [start, [stop]]) -> integer -- return first index of value.
		Raises ValueError if the value is not present.
		"""

