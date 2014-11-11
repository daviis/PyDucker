"""
A python implementation of built in classes for looking at method signatures.

Modified on 2014-11-06
"""

class list():
	def __add__(self, value):
		"""
		Return self+value.
		@value:*
		"""
		return []

	def __class__(self, it = None):
		"""
		list() -> new empty list
		list(iterable) -> new list initialized from iterable's items
		@it:*
		"""
		return []
		

	def __contains__(self, key):
		"""
		Return key in self.
		@key:obj
		"""
		return True

	def __delattr__(self, key):
		"""
		Implement delattr(self, name).
		"""
		pass 

# 	def __delitem__(self, key):
		"""
		Delete self[key].
		"""
# 		pass

# 	def __dir__(self, ):
		"""
		__dir__() -> list
		default dir() implementation
		"""
# 		pass

# 	def __doc__(self, ):
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
		
	def __eq__(self, value):
		"""
		Return self==value.
		@value:*
		"""
		return True

# 	def __format__(self, ???):
		"""
		default object formatter
		"""

	def __ge__(self, value):
		"""
		Return self>=value.
		"""
		return True

# 	def __getattribute__(self, name):
		"""
		Return getattr(self, name).
		"""
		

	def __getitem__(self, idx):
		"""
		x.__getitem__(y) <==> x[y]
		@idx:int
		"""
		a = object()
		return a

	def __gt__(self, other):
		"""
		Return self>value.
		@other:*
		"""
		return True

# 	def __hash__(self, ???):
		"""
		None
		"""

	def __iadd__(self, value):
		"""
		Implement self+=value.
		@vlaue:object
		"""
		return []

	def __imul__(self, value):
		"""
		Implement self*=value.
		@value:int
		"""
		return []

	def __init__(self, args, kwargs):
		"""
		Initialize self.  See help(type(self)) for accurate signature.
		@args:*
		@kwargs:**
		"""
		return []

# 	def __iter__(self):
		"""
		Implement iter(self).
		"""
		

	def __le__(self, value):
		"""
		Return self<=value.
		@value:*
		"""
		return True

	def __len__(self):
		"""
		Return len(self).
		"""
		return 1;

	def __lt__(self, other):
		"""
		Return self<value.
		@other:*
		"""
		return True

	def __mul__(self, anInt):
		"""
		Return self*value.n
		@anInt:int
		"""
		return []

	def __ne__(self, value):
		"""
		Return self!=value.
		@value:*
		"""
		return True

# 	def __new__(self, ???):
		"""
		Create and return a new object.  See help(type) for accurate signature.
		"""

# 	def __reduce__(self, ???):
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

	def __reversed__(self):
		"""
		L.__reversed__() -- return a reverse iterator over the list
		"""
		return []

	def __rmul__(self, anInt):
		"""
		Return self*value.
		@anInt:int
		"""
		return anInt

# 	def __setattr__(self, ???):
		"""
		Implement setattr(self, name, value).
		"""

	def __setitem__(self, anInt):
		"""
		Set self[key] to value.
		@anInt:int
		"""
		return anInt

	def __sizeof__(self):
		"""
		L.__sizeof__() -- size of L in memory, in bytes
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

	def append(self, val):
		"""
		L.append(object) -> None -- append object to end
		@val:object
		"""
		return None

	def clear(self):
		"""
		L.clear() -> None -- remove all items from L
		"""
		return None

	def copy(self):
		"""
		L.copy() -> list -- a shallow copy of L
		"""
		return []

	def count(self, obj):
		"""
		L.count(value) -> integer -- return number of occurrences of value
		@obj:object
		"""
		return 1

	def extend(self, lst):
		"""
		L.extend(iterable) -> None -- extend list by appending elements from the iterable
		@lst:list
		"""
		return None

	def index(self, value, start=None, stop=None):
		"""
		L.index(value, [start, [stop]]) -> integer -- return first index of value.
		Raises ValueError if the value is not present.
		@value:int
		@start:int
		@stop:int
		"""
		return 1
		

	def insert(self, idx, object):
		"""
		L.insert(index, object) -- insert object before index
		"""
		return None

	def pop(self, idx=None):
		"""
		L.pop([index]) -> item -- remove and return item at index (default last).
		Raises IndexError if list is empty or index is out of range.
		@idx:int
		"""
		return object

	def remove(self, obj):
		"""
		L.remove(value) -> None -- remove first occurrence of value.
		Raises ValueError if the value is not present.
		@obj:object
		"""
		return None

	def reverse(self):
		"""
		L.reverse() -- reverse *IN PLACE*
		"""
		return None

	def sort(self, key=None, reverse=False):
		"""
		L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
		@key:obj
		@reverse:bool
		"""
		return None

