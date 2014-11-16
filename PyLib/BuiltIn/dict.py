"""
A python implementation of built in classes for looking at method signatures.

Modified on 2014-11-14
"""

class dict():
	def __class__(self):
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
		"""
		return {}
	

	def __contains__(self, key):
		"""
		True if D has a key k ,else False.
		@key:object
		"""
		return True

#	def __delattr__(self):
		"""
		Implemen delattr(self, name).
		"""

	def __delitem__(self, value):
		"""
		Delete self[key].
		@value:object
		"""
		

#	def __doc__(self, ???):
		"""
		str(object='') -> string
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
		@value:object
		"""
		return True

	def __format__(self):
		"""
		default object formatter
		"""
		return ''

	def __ge__(self, value):
		"""
		Return self>=value.
		@value:object
		"""
		return True

#	def __getattribute__(self):
		"""
		Return getattr(self, name).
		"""

	def __getitem__(self, value):
		"""
		x.__getitem__(y) <==> x[y]
		@value:object
		"""
		return object

	def __gt__(self, value):
		"""
		Return self>value
		"""
		return True

#	def __hash__(self, ???):
		"""
		None
		"""

#	def __init__(self, ???):
		"""
		Initialize self. see help(type(x)) for signature
		"""

#	def __iter__(self, ???):
		"""
		Implement iter(self)
		"""

	def __le__(self, value):
		"""
		Return self<=value.
		@value:object
		"""
		return True

	def __len__(self):
		"""
		Return len(self).
		"""
		return 1   

	def __lt__(self, value):
		"""
		Return self<value
		@value: object
		"""
		return True

	def __ne__(self, value):
		"""
		Return self!=value
		@value:object
		"""
		return True

#	def __new__(self):
		"""
		Create and return a new object. See help(type) for accurate signature
		"""
		

#	def __reduce__(self, ???):
		"""
		helper for pickle
		"""

#	def __reduce_ex__(self, ???):
		"""
		helper for pickle
		"""

	def __repr__(self):
		"""
		Return repr(self).
		"""
		return ''

#	def __setattr__(self, ???):
		"""
		Implement setattr(self, name, value).
		"""

	def __setitem__(self, key, value):
		"""
		Set self[key] to value.
		@key:object
		@value:object
		"""

	def __sizeof__(self):
		"""
		D.__sizeof__() -> size of D in memory, in bytes
		"""
		return 1

	def __str__(self):
		"""
		Return str(self)
		"""
		return ''

#	def __subclasshook__(self, ???):
		"""
		Abstract classes can override this to customize issubclass().
		
		This is invoked early on by abc.ABCMeta.__subclasscheck__().
		It should return True, False or NotImplemented.  If it returns
		NotImplemented, the normal algorithm is used.  Otherwise, it
		overrides the normal algorithm (and the outcome is cached).
		
		"""

	def clear(self):
		"""
		D.clear() -> None.  Remove all items from D.
		"""

	def copy(self):
		"""
		D.copy() -> a shallow copy of D
		"""
		return {}

	def fromkeys(self, value):
		"""
		Return a new dict with key from iterable and value equal to value.
		@value:object
		"""
		return {}
	
	def get(self, key):
		"""
		D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
		@key:object
		"""
		return object

	def has_key(self, key):
		"""
		D.has_key(k) -> True if D has a key k, else False
		@key:object
		"""
		return True

	def items(self):
		"""
		D.items() -> list of D's (key, value) pairs, as 2-tuples
		"""
		return ()

	def keys(self):
		"""
		D.keys() -> list of D's keys
		"""
		return []

	def pop(self, value):
		"""
		D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
		If key is not found, d is returned if given, otherwise KeyError is raised
		@value:object
		"""
		return object
	
	def popitem(self):
		"""
		D.popitem() -> (k, v), remove and return some (key, value) pair as a
		2-tuple; but raise KeyError if D is empty.
		"""
		return ()

	def setdefault(self, key, value ):
		"""
		D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
		@key:object
		@value:object
		"""
		return object

	def update(self, key, value):
		"""
		D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
		If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
		If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
		In either case, this is followed by: for k in F: D[k] = F[k]
		@key:object
		@value:object
		"""

	def values(self):
		"""
		D.values() -> list of D's values
		"""
		return object
