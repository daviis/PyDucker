"""
A python implementation of built in classes for looking at method signatures.

Modified on 2014-11-06
"""

class dict():
	def __class__(self, ???):
		"""
		dict() -> new empty dictionary
		dict(mapping) -> new dictionary initialized from a mapping object's
		    (key, value) pairs
		dict(iterable) -> new dictionary initialized as if via:
		    d = {}
		    for k, v in iterable:
		        d[k] = v
		dict(**kwargs) -> new dictionary initialized with the name=value pairs
		    in the keyword argument list.  For example:  dict(one=1, two=2)
		@returntype:dict
		"""

	def __contains__(self, ???):
		"""
		True if D has a key k, else False.
		@returntype:bool
		"""

	def __delattr__(self, ???):
		"""
		Implement delattr(self, name).
		
		"""

	def __delitem__(self, ???):
		"""
		Delete self[key].
		@returntype:None
		"""

	def __dir__(self, ???):
		"""
		__dir__() -> list
		default dir() implementation
		@returntype:list
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
		@returntype:bool
		"""

	def __format__(self, ???):
		"""
		default object formatter
		"""

	def __ge__(self, ???):
		"""
		Return self>=value.
		@returntype:bool
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
		@returntype:bool
		"""

	def __hash__(self, ???):
		"""
		None
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
		@returntype:bool
		"""

	def __len__(self, ???):
		"""
		Return len(self)
		@returntype:int.
		"""

	def __lt__(self, ???):
		"""
		Return self<value.
		"""

	def __ne__(self, ???):
		"""
		Return self!=value.
		@returntype:bool
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
		D.__sizeof__() -> size of D in memory, in bytes
		"""

	def __str__(self, ???):
		"""
		Return str(self).
		@returntype:str
		"""

	def __subclasshook__(self, ???):
		"""
		Abstract classes can override this to customize issubclass().
		
		This is invoked early on by abc.ABCMeta.__subclasscheck__().
		It should return True, False or NotImplemented.  If it returns
		NotImplemented, the normal algorithm is used.  Otherwise, it
		overrides the normal algorithm (and the outcome is cached).
		
		"""

	def clear(self, ???):
		"""
		D.clear() -> None.  Remove all items from D.
		"""

	def copy(self, ???):
		"""
		D.copy() -> a shallow copy of D
		"""

	def fromkeys(self, ???):
		"""
		Returns a new dict with keys from iterable and values equal to value.
		"""

	def get(self, ???):
		"""
		D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
		"""

	def items(self, ???):
		"""
		D.items() -> a set-like object providing a view on D's items
		"""

	def keys(self, ???):
		"""
		D.keys() -> a set-like object providing a view on D's keys
		"""

	def pop(self, ???):
		"""
		D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
		If key is not found, d is returned if given, otherwise KeyError is raised
		"""

	def popitem(self, ???):
		"""
		D.popitem() -> (k, v), remove and return some (key, value) pair as a
		2-tuple; but raise KeyError if D is empty.
		"""

	def setdefault(self, ???):
		"""
		D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
		"""

	def update(self, ???):
		"""
		D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
		If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
		If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
		In either case, this is followed by: for k in F:  D[k] = F[k]
		"""

	def values(self, ???):
		"""
		D.values() -> an object providing a view on D's values
		"""

