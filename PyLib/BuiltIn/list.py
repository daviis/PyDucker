"""
A python implementation of built in classes for looking at method signatures.

Modified on 2014-11-06
"""

class list():
	def __add__(self, ???):
		"""
		Return self+value.
		"""

	def __class__(self, ???):
		"""
		list() -> new empty list
		list(iterable) -> new list initialized from iterable's items
		"""

	def __contains__(self, ???):
		"""
		Return key in self.
		"""

	def __delattr__(self, ???):
		"""
		Implement delattr(self, name).
		"""

	def __delitem__(self, ???):
		"""
		Delete self[key].
		"""

	def __dir__(self, ???):
		"""
		__dir__() -> list
		default dir() implementation
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
		x.__getitem__(y) <==> x[y]
		"""

	def __gt__(self, ???):
		"""
		Return self>value.
		"""

	def __hash__(self, ???):
		"""
		None
		"""

	def __iadd__(self, ???):
		"""
		Implement self+=value.
		"""

	def __imul__(self, ???):
		"""
		Implement self*=value.
		"""

	def __init__(self, ???):
		"""
		Initialize self.  See help(type(self)) for accurate signature.
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
		Return len(self).
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
		Return self!=value.
		"""

	def __new__(self, ???):
		"""
		Create and return a new object.  See help(type) for accurate signature.
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

	def __reversed__(self, ???):
		"""
		L.__reversed__() -- return a reverse iterator over the list
		"""

	def __rmul__(self, ???):
		"""
		Return self*value.
		"""

	def __setattr__(self, ???):
		"""
		Implement setattr(self, name, value).
		"""

	def __setitem__(self, ???):
		"""
		Set self[key] to value.
		"""

	def __sizeof__(self, ???):
		"""
		L.__sizeof__() -- size of L in memory, in bytes
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

	def append(self, ???):
		"""
		L.append(object) -> None -- append object to end
		"""

	def clear(self, ???):
		"""
		L.clear() -> None -- remove all items from L
		"""

	def copy(self, ???):
		"""
		L.copy() -> list -- a shallow copy of L
		"""

	def count(self, ???):
		"""
		L.count(value) -> integer -- return number of occurrences of value
		"""

	def extend(self, ???):
		"""
		L.extend(iterable) -> None -- extend list by appending elements from the iterable
		"""

	def index(self, ???):
		"""
		L.index(value, [start, [stop]]) -> integer -- return first index of value.
		Raises ValueError if the value is not present.
		"""

	def insert(self, ???):
		"""
		L.insert(index, object) -- insert object before index
		"""

	def pop(self, ???):
		"""
		L.pop([index]) -> item -- remove and return item at index (default last).
		Raises IndexError if list is empty or index is out of range.
		"""

	def remove(self, ???):
		"""
		L.remove(value) -> None -- remove first occurrence of value.
		Raises ValueError if the value is not present.
		"""

	def reverse(self, ???):
		"""
		L.reverse() -- reverse *IN PLACE*
		"""

	def sort(self, ???):
		"""
		L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
		"""

