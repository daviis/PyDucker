class list():
	def __add__(???):
		"""
		Return self+value.
		"""

	def __class__(???):
		"""
		list() -> new empty list
		list(iterable) -> new list initialized from iterable's items
		"""

	def __contains__(???):
		"""
		Return key in self.
		"""

	def __delattr__(???):
		"""
		Implement delattr(self, name).
		"""

	def __delitem__(???):
		"""
		Delete self[key].
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
		x.__getitem__(y) <==> x[y]
		"""

	def __gt__(???):
		"""
		Return self>value.
		"""

	def __hash__(???):
		"""
		None
		"""

	def __iadd__(???):
		"""
		Implement self+=value.
		"""

	def __imul__(???):
		"""
		Implement self*=value.
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

	def __reversed__(???):
		"""
		L.__reversed__() -- return a reverse iterator over the list
		"""

	def __rmul__(???):
		"""
		Return self*value.
		"""

	def __setattr__(???):
		"""
		Implement setattr(self, name, value).
		"""

	def __setitem__(???):
		"""
		Set self[key] to value.
		"""

	def __sizeof__(???):
		"""
		L.__sizeof__() -- size of L in memory, in bytes
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

	def append(???):
		"""
		L.append(object) -> None -- append object to end
		"""

	def clear(???):
		"""
		L.clear() -> None -- remove all items from L
		"""

	def copy(???):
		"""
		L.copy() -> list -- a shallow copy of L
		"""

	def count(???):
		"""
		L.count(value) -> integer -- return number of occurrences of value
		"""

	def extend(???):
		"""
		L.extend(iterable) -> None -- extend list by appending elements from the iterable
		"""

	def index(???):
		"""
		L.index(value, [start, [stop]]) -> integer -- return first index of value.
		Raises ValueError if the value is not present.
		"""

	def insert(???):
		"""
		L.insert(index, object) -- insert object before index
		"""

	def pop(???):
		"""
		L.pop([index]) -> item -- remove and return item at index (default last).
		Raises IndexError if list is empty or index is out of range.
		"""

	def remove(???):
		"""
		L.remove(value) -> None -- remove first occurrence of value.
		Raises ValueError if the value is not present.
		"""

	def reverse(???):
		"""
		L.reverse() -- reverse *IN PLACE*
		"""

	def sort(???):
		"""
		L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
		"""

