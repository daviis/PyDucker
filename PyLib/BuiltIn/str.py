"""
A python implementation of built in classes for looking at method signatures.

Modified on 2014-11-06
"""

class str():
	def __add__(self, value):
		"""
		Return self+value.
		
		@value:str
		"""
		return ""

# 	def __class__(self, ???):
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

	def __contains__(self, key):
		"""
		Return key in self.
		
		@key:str
		"""
		return True

# 	def __delattr__(self, ???):
		"""
		Implement delattr(self, name).
		"""

	def __dir__(self):
		"""
		__dir__() -> list
		default dir() implementation
		"""
		return {}

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

	def __eq__(self):
		"""
		Return self==value.
		"""
		return True

	def __format__(self, st, lst):
		"""
		S.__format__(format_spec) -> str
		
		Return a formatted version of S as described by format_spec.
		
		@st:str
		@lst:*
		"""
		return ""

	def __ge__(self):
		"""
		Return self>=value.
		"""
		return True
	
	def __getattribute__(self, name):
		"""
		Return getattr(self, name).
		
		@name:str 
		"""
		return object

	def __getitem__(self, key):
		"""
		Return self[key].
		
		@key:int
		"""
		return ""

# 	def __getnewargs__(self, ???):
		"""
		None
		"""

	def __gt__(self, value):
		"""
		Return self>value.
		
		@value:str
		"""
		return True

	def __hash__(self, ???):
		"""
		Return hash(self).
		"""

# 	def __init__(self):
		"""
		Initialize self.  See help(type(self)) for accurate signature.
		"""

	def __iter__(self):
		"""
		Implement iter(self).
		
		"""
		return iterator

	def __le__(self, ???):
		"""
		Return self<=value.
		"""
		return True

	def __len__(self):
		"""
		Return len(self).
		"""
		return 1

	def __lt__(self, value):
		"""
		Return self<value.
		
		@value:str
		"""
		return True

	def __mod__(self, value):
		"""
		Return self%value.
		
		@value:int
		"""
		return ""

	def __mul__(self, value):
		"""
		Return self*value.n
		
		@value:int
		"""
		return ""

	def __ne__(self, value):
		"""
		Return self!=value.
		
		@value:str
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

	def __rmod__(self, value):
		"""
		Return value%self.
		"""
		return ""

	def __rmul__(self, value):
		"""
		Return self*value.
		
		@value:int
		"""
		return ""

	def __setattr__(self, name, value):
		"""
		Implement setattr(self, name, value).
		
		@name:str
		@value:object
		"""
		return 

	def __sizeof__(self:
		"""
		S.__sizeof__() -> size of S in memory, in bytes
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

	def capitalize(self):
		"""
		S.capitalize() -> str
		
		Return a capitalized version of S, i.e. make the first character
		have upper case and the rest lower case.
		"""
		return ""

	def casefold(self):
		"""
		S.casefold() -> str
		
		Return a version of S suitable for caseless comparisons.
		"""
		return ""

	def center(self, width, fillchar=None):
		"""
		S.center(width[, fillchar]) -> str
		
		Return S centered in a string of length width. Padding is
		done using the specified fill character (default is a space)
		
		@width:int
		@fillchar:str
		"""
		return ""

	def count(self, sub, start=None, end=None):
		"""
		S.count(sub[, start[, end]]) -> int
		
		Return the number of non-overlapping occurrences of substring sub in
		string S[start:end].  Optional arguments start and end are
		interpreted as in slice notation.
		
		@sub:str
		@start:int
		@end:int
		"""
		return 1

	def encode(self, encoding='utf-8', errors='strict'):
		"""
		S.encode(encoding='utf-8', errors='strict') -> bytes
		
		Encode S using the codec registered for encoding. Default encoding
		is 'utf-8'. errors may be given to set a different error
		handling scheme. Default is 'strict' meaning that encoding errors raise
		a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
		'xmlcharrefreplace' as well as any other name registered with
		codecs.register_error that can handle UnicodeEncodeErrors.
		
		@encoding:str
		@errors:str
		"""
		return 1

	def endswith(self, suffix, start=None, end=None):
		"""
		S.endswith(suffix[, start[, end]]) -> bool
		
		Return True if S ends with the specified suffix, False otherwise.
		With optional start, test S beginning at that position.
		With optional end, stop comparing S at that position.
		suffix can also be a tuple of strings to try.
		
		@suffix:str
		@start:int
		@end:int
		"""
		return True

	def expandtabs(self, tabsize=8):
		"""
		S.expandtabs(tabsize=8) -> str
		
		Return a copy of S where all tab characters are expanded using spaces.
		If tabsize is not given, a tab size of 8 characters is assumed.
		
		@tabsize:int
		"""
		return ""

	def find(self, sub, start=None, end=None):
		"""
		S.find(sub[, start[, end]]) -> int
		
		Return the lowest index in S where substring sub is found,
		such that sub is contained within S[start:end].  Optional
		arguments start and end are interpreted as in slice notation.
		
		Return -1 on failure.
		
		@sub:str
		@start:int
		@end:int
		"""
		return 1

	def format(self, args, kwargs):
		"""
		S.format(*args, **kwargs) -> str
		
		Return a formatted version of S, using substitutions from args and kwargs.
		The substitutions are identified by braces ('{' and '}').
		@args:*
		@kwargs:**
		"""
		return ""

	def format_map(self, mapping):
		"""
		S.format_map(mapping) -> str
		
		Return a formatted version of S, using substitutions from mapping.
		The substitutions are identified by braces ('{' and '}').
		
		@mapping:**
		"""
		return ""

	def index(self, sub, start=None, end=None):
		"""
		S.index(sub[, start[, end]]) -> int
		
		Like S.find() but raise ValueError when the substring is not found.
		
		@sub:str
		@start:int
		@end:int
		"""
		return 1

	def isalnum(self):
		"""
		S.isalnum() -> bool
		
		Return True if all characters in S are alphanumeric
		and there is at least one character in S, False otherwise.
		"""
		return True

	def isalpha(self):
		"""
		S.isalpha() -> bool
		
		Return True if all characters in S are alphabetic
		and there is at least one character in S, False otherwise.
		"""
		return True

	def isdecimal(self):
		"""
		S.isdecimal() -> bool
		
		Return True if there are only decimal characters in S,
		False otherwise.
		"""
		return True

	def isdigit(self):
		"""
		S.isdigit() -> bool
		
		Return True if all characters in S are digits
		and there is at least one character in S, False otherwise.
		"""
		return True

	def isidentifier(self):
		"""
		S.isidentifier() -> bool
		
		Return True if S is a valid identifier according
		to the language definition.
		
		Use keyword.iskeyword() to test for reserved identifiers
		such as "def" and "class".
		
		"""
		return True

	def islower(self):
		"""
		S.islower() -> bool
		
		Return True if all cased characters in S are lowercase and there is
		at least one cased character in S, False otherwise.
		"""
		return True

	def isnumeric(self):
		"""
		S.isnumeric() -> bool
		
		Return True if there are only numeric characters in S,
		False otherwise.
		"""
		return True

	def isprintable(self):
		"""
		S.isprintable() -> bool
		
		Return True if all characters in S are considered
		printable in repr() or S is empty, False otherwise.
		"""
		return True

	def isspace(self):
		"""
		S.isspace() -> bool
		
		Return True if all characters in S are whitespace
		and there is at least one character in S, False otherwise.
		"""
		return True

	def istitle(self):
		"""
		S.istitle() -> bool
		
		Return True if S is a titlecased string and there is at least one
		character in S, i.e. upper- and titlecase characters may only
		follow uncased characters and lowercase characters only cased ones.
		Return False otherwise.
		"""
		return True

	def isupper(self):
		"""
		S.isupper() -> bool
		
		Return True if all cased characters in S are uppercase and there is
		at least one cased character in S, False otherwise.
		"""
		return True

	def join(self, iter):
		"""
		S.join(iterable) -> str
		
		Return a string which is the concatenation of the strings in the
		iterable.  The separator between elements is S.
		
		@iter:iterable
		"""
		return ""

	def ljust(self, width, fillchar=None):
		"""
		S.ljust(width[, fillchar]) -> str
		
		Return S left-justified in a Unicode string of length width. Padding is
		done using the specified fill character (default is a space).
		
		@width:int
		@fillchar:str
		"""
		return ""

	def lower(self):
		"""
		S.lower() -> str
		
		Return a copy of the string S converted to lowercase.
		"""
		return ""

	def lstrip(self, chars=None):
		"""
		S.lstrip([chars]) -> str
		
		Return a copy of the string S with leading whitespace removed.
		If chars is given and not None, remove characters in chars instead.
		
		@chars:str
		"""
		return ""

	def maketrans(self, first, second, third):
		"""
		Return a translation table usable for str.translate().
		
		If there is only one argument, it must be a dictionary mapping Unicode
		ordinals (integers) or characters to Unicode ordinals, strings or None.
		Character keys will be then converted to ordinals.
		If there are two arguments, they must be strings of equal length, and
		in the resulting dictionary, each character in x will be mapped to the
		character at the same position in y. If there is a third argument, it
		must be a string, whose characters will be mapped to None in the result.
		
		@first:str|**
		@second:str
		@third:str
		"""
		return {}

	def partition(self, sep):
		"""
		S.partition(sep) -> (head, sep, tail)
		
		Search for the separator sep in S, and return the part before it,
		the separator itself, and the part after it.  If the separator is not
		found, return S and two empty strings.
		
		@sep:str
		"""
		return ()

	def replace(self, old, new, count=None):
		"""
		S.replace(old, new[, count]) -> str
		
		Return a copy of S with all occurrences of substring
		old replaced by new.  If the optional argument count is
		given, only the first count occurrences are replaced.
		
		@old:str
		@new:str
		@count:int
		"""
		return ""

	def rfind(self, sub, start=None, end=None):
		"""
		S.rfind(sub[, start[, end]]) -> int
		
		Return the highest index in S where substring sub is found,
		such that sub is contained within S[start:end].  Optional
		arguments start and end are interpreted as in slice notation.
		
		Return -1 on failure.
		
		@sub:str
		@start:int
		@end:int
		"""
		return 1

	def rindex(self, sub, start=None, end=None):
		"""
		S.rindex(sub[, start[, end]]) -> int
		
		Like S.rfind() but raise ValueError when the substring is not found.
		@sub:str
		@start:int
		@end:int
		"""
		return 1

	def rjust(self, width, fillchar=None):
		"""
		S.rjust(width[, fillchar]) -> str
		
		Return S right-justified in a string of length width. Padding is
		done using the specified fill character (default is a space).
		
		@width:int
		@fillchar:str
		"""
		return ""

	def rpartition(self, sep):
		"""
		S.rpartition(sep) -> (head, sep, tail)
		
		Search for the separator sep in S, starting at the end of S, and return
		the part before it, the separator itself, and the part after it.  If the
		separator is not found, return two empty strings and S.
		@sep:char
		"""
		return ()

	def rsplit(self, sep=None, maxsplit=-1):
		"""
		S.rsplit(sep=None, maxsplit=-1) -> list of strings
		
		Return a list of the words in S, using sep as the
		delimiter string, starting at the end of the string and
		working to the front.  If maxsplit is given, at most maxsplit
		splits are done. If sep is not specified, any whitespace string
		is a separator.
		
		@sep:str
		@maxsplit:int
		"""
		return []

	def rstrip(self, chars=None):
		"""
		S.rstrip([chars]) -> str
		
		Return a copy of the string S with trailing whitespace removed.
		If chars is given and not None, remove characters in chars instead.
		@chars:str
		"""
		return ""

	def split(self, sep=None, maxsplit=-1):
		"""
		S.split(sep=None, maxsplit=-1) -> list of strings
		
		Return a list of the words in S, using sep as the
		delimiter string.  If maxsplit is given, at most maxsplit
		splits are done. If sep is not specified or is None, any
		whitespace string is a separator and empty strings are
		removed from the result.
		
		@sep:str
		@maxsplit:int
		"""
		return []
		

	def splitlines(self, keepends=None):
		"""
		S.splitlines([keepends]) -> list of strings
		
		Return a list of the lines in S, breaking at line boundaries.
		Line breaks are not included in the resulting list unless keepends
		is given and true.
		@keepends:boolean
		"""
		return []

	def startswith(self, prefix, start=None, end=None):
		"""
		S.startswith(prefix[, start[, end]]) -> bool
		
		Return True if S starts with the specified prefix, False otherwise.
		With optional start, test S beginning at that position.
		With optional end, stop comparing S at that position.
		prefix can also be a tuple of strings to try.
		
		@prefix:str
		@start:int
		@end:int
		"""
		return True

	def strip(self, chars=None):
		"""
		S.strip([chars]) -> str
		
		Return a copy of the string S with leading and trailing
		whitespace removed.
		If chars is given and not None, remove characters in chars instead.
		@chars:str*
		"""
		return ""

	def swapcase(self):
		"""
		S.swapcase() -> str
		
		Return a copy of S with uppercase characters converted to lowercase
		and vice versa.
		"""
		return ""

	def title(self):
		"""
		S.title() -> str
		
		Return a titlecased version of S, i.e. words start with title case
		characters, all remaining cased characters have lower case.
		"""
		return ""

	def translate(self, table):
		"""
		S.translate(table) -> str
		
		Return a copy of the string S, where all characters have been mapped
		through the given translation table, which must be a mapping of
		Unicode ordinals to Unicode ordinals, strings, or None.
		Unmapped characters are left untouched. Characters mapped to None
		are deleted.
		
		@table:**
		"""
		return ""

	def upper(self):
		"""
		S.upper() -> str
		
		Return a copy of S converted to uppercase.
		"""
		return ""

	def zfill(self, wid):
		"""
		S.zfill(width) -> str
		
		Pad a numeric string S with zeros on the left, to fill a field
		of the specified width. The string S is never truncated.
		@wid:int
		"""
		return ""

