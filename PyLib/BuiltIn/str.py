"""
A python implementation of built in classes for looking at method signatures.

Modified on 2014-11-06
"""

class str():
	def __add__(self, ???):
		"""
		Return self+value.
		"""

	def __class__(self, ???):
		"""
		str(object='') -> string
		str(bytes_or_buffer[, encoding{, errors]]) -> str
		
		Create a new string object from the given object. If encoding or
		errors is specified, then the object must expose a data buffer
		that will be decoded using the given encoding and error handler.
		Otherwise, returns the result of object.__str__() (if defined)
		or repr(object).
		encoding defaults to sys.getdefaultencoding().
		errors defaults to 'strict'.
		
		"""

	def __contains__(self, ???):
		"""
		Return key in self.
		"""

	def __delattr__(self, ???):
		"""
		Implement delattr(self, name).
		"""
		
	def __dir__(self):
		"""
		__dir__() -> list
		default dir() implementation
		"""

	def __doc__(self, ???):
		"""
		str(object='') -> string
		str(bytes_or_buffer[, encoding[, errors]]) -> str
	
		Create a new string object from the given object. If encoding or
		errors is specified, then the object must expose a data buffer
		that will be decoded using the given encoding and error handler.
		Otherwise, returns the result of object.__str__() (if defined)
		or repr(object).
		encoding defaults to sys.getdefaultencoing().
		errors defaults to 'strict'.
		"""

	def __eq__(self, ???):
		"""
		Return self===value.
		"""

	def __format__(self, ???):
		"""
		S.__format__(format_spec) -> string
		
		Return a formatted version of S as described by format_spec.
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
		
	def __iter__(self):
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

	def __mod__(self, ???):
		"""
		Return self%value.
		"""

	def __mul__(self, ???):
		"""
		Reutrn self*value.n
		"""

	def __ne__(self, ???):
		"""
		Return self!=value.
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

	def __rmod__(self, ???):
		"""
		Return value%self.
		"""

	def __rmul__(self, ???):
		"""
		REturn self*value.
		"""

	def __setattr__(self, ???):
		"""
		Implement setattr(self, name, value).
		"""

	def __sizeof__(self, ???):
		"""
		S.__sizeof__() -> size of S in memory, in bytes
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

	def capitalize(self, ???):
		"""
		S.capitalize() -> string
		
		Return a copy of the string S with only its first character
		capitalized.
		"""

	def center(self, ???):
		"""
		S.center(width[, fillchar]) -> string
		
		Return S centered in a string of length width. Padding is
		done using the specified fill character (default is a space)
		"""

	def count(self, ???):
		"""
		S.count(sub[, start[, end]]) -> int
		
		Return the number of non-overlapping occurrences of substring sub in
		string S[start:end].  Optional arguments start and end are interpreted
		as in slice notation.
		"""

	def decode(self, ???):
		"""
		S.decode([encoding[,errors]]) -> object
		
		Decodes S using the codec registered for encoding. encoding defaults
		to the default encoding. errors may be given to set a different error
		handling scheme. Default is 'strict' meaning that encoding errors raise
		a UnicodeDecodeError. Other possible values are 'ignore' and 'replace'
		as well as any other name registered with codecs.register_error that is
		able to handle UnicodeDecodeErrors.
		"""

	def encode(self, ???):
		"""
		S.encode([encoding[,errors]]) -> object
		
		Encodes S using the codec registered for encoding. encoding defaults
		to the default encoding. errors may be given to set a different error
		handling scheme. Default is 'strict' meaning that encoding errors raise
		a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
		'xmlcharrefreplace' as well as any other name registered with
		codecs.register_error that is able to handle UnicodeEncodeErrors.
		"""

	def endswith(self, ???):
		"""
		S.endswith(suffix[, start[, end]]) -> bool
		
		Return True if S ends with the specified suffix, False otherwise.
		With optional start, test S beginning at that position.
		With optional end, stop comparing S at that position.
		suffix can also be a tuple of strings to try.
		"""

	def expandtabs(self, ???):
		"""
		S.expandtabs([tabsize]) -> string
		
		Return a copy of S where all tab characters are expanded using spaces.
		If tabsize is not given, a tab size of 8 characters is assumed.
		"""

	def find(self, ???):
		"""
		S.find(sub [,start [,end]]) -> int
		
		Return the lowest index in S where substring sub is found,
		such that sub is contained within S[start:end].  Optional
		arguments start and end are interpreted as in slice notation.
		
		Return -1 on failure.
		"""

	def format(self, ???):
		"""
		S.format(*args, **kwargs) -> string
		
		Return a formatted version of S, using substitutions from args and kwargs.
		The substitutions are identified by braces ('{' and '}').
		"""

	def index(self, ???):
		"""
		S.index(sub [,start [,end]]) -> int
		
		Like S.find() but raise ValueError when the substring is not found.
		"""

	def isalnum(self, ???):
		"""
		S.isalnum() -> bool
		
		Return True if all characters in S are alphanumeric
		and there is at least one character in S, False otherwise.
		"""

	def isalpha(self, ???):
		"""
		S.isalpha() -> bool
		
		Return True if all characters in S are alphabetic
		and there is at least one character in S, False otherwise.
		"""

	def isdigit(self, ???):
		"""
		S.isdigit() -> bool
		
		Return True if all characters in S are digits
		and there is at least one character in S, False otherwise.
		"""

	def islower(self, ???):
		"""
		S.islower() -> bool
		
		Return True if all cased characters in S are lowercase and there is
		at least one cased character in S, False otherwise.
		"""

	def isspace(self, ???):
		"""
		S.isspace() -> bool
		
		Return True if all characters in S are whitespace
		and there is at least one character in S, False otherwise.
		"""

	def istitle(self, ???):
		"""
		S.istitle() -> bool
		
		Return True if S is a titlecased string and there is at least one
		character in S, i.e. uppercase characters may only follow uncased
		characters and lowercase characters only cased ones. Return False
		otherwise.
		"""

	def isupper(self, ???):
		"""
		S.isupper() -> bool
		
		Return True if all cased characters in S are uppercase and there is
		at least one cased character in S, False otherwise.
		"""

	def join(self, ???):
		"""
		S.join(iterable) -> string
		
		Return a string which is the concatenation of the strings in the
		iterable.  The separator between elements is S.
		"""

	def ljust(self, ???):
		"""
		S.ljust(width[, fillchar]) -> string
		
		Return S left-justified in a string of length width. Padding is
		done using the specified fill character (default is a space).
		"""

	def lower(self, ???):
		"""
		S.lower() -> string
		
		Return a copy of the string S converted to lowercase.
		"""

	def lstrip(self, ???):
		"""
		S.lstrip([chars]) -> string or unicode
		
		Return a copy of the string S with leading whitespace removed.
		If chars is given and not None, remove characters in chars instead.
		If chars is unicode, S will be converted to unicode before stripping
		"""

	def partition(self, ???):
		"""
		S.partition(sep) -> (head, sep, tail)
		
		Search for the separator sep in S, and return the part before it,
		the separator itself, and the part after it.  If the separator is not
		found, return S and two empty strings.
		"""

	def replace(self, ???):
		"""
		S.replace(old, new[, count]) -> string
		
		Return a copy of string S with all occurrences of substring
		old replaced by new.  If the optional argument count is
		given, only the first count occurrences are replaced.
		"""

	def rfind(self, ???):
		"""
		S.rfind(sub [,start [,end]]) -> int
		
		Return the highest index in S where substring sub is found,
		such that sub is contained within S[start:end].  Optional
		arguments start and end are interpreted as in slice notation.
		
		Return -1 on failure.
		"""

	def rindex(self, ???):
		"""
		S.rindex(sub [,start [,end]]) -> int
		
		Like S.rfind() but raise ValueError when the substring is not found.
		"""

	def rjust(self, ???):
		"""
		S.rjust(width[, fillchar]) -> string
		
		Return S right-justified in a string of length width. Padding is
		done using the specified fill character (default is a space)
		"""

	def rpartition(self, ???):
		"""
		S.rpartition(sep) -> (head, sep, tail)
		
		Search for the separator sep in S, starting at the end of S, and return
		the part before it, the separator itself, and the part after it.  If the
		separator is not found, return two empty strings and S.
		"""

	def rsplit(self, ???):
		"""
		S.rsplit([sep [,maxsplit]]) -> list of strings
		
		Return a list of the words in the string S, using sep as the
		delimiter string, starting at the end of the string and working
		to the front.  If maxsplit is given, at most maxsplit splits are
		done. If sep is not specified or is None, any whitespace string
		is a separator.
		"""

	def rstrip(self, ???):
		"""
		S.rstrip([chars]) -> string or unicode
		
		Return a copy of the string S with trailing whitespace removed.
		If chars is given and not None, remove characters in chars instead.
		If chars is unicode, S will be converted to unicode before stripping
		"""

	def split(self, ???):
		"""
		S.split([sep [,maxsplit]]) -> list of strings
		
		Return a list of the words in the string S, using sep as the
		delimiter string.  If maxsplit is given, at most maxsplit
		splits are done. If sep is not specified or is None, any
		whitespace string is a separator and empty strings are removed
		from the result.
		"""

	def splitlines(self, ???):
		"""
		S.splitlines(keepends=False) -> list of strings
		
		Return a list of the lines in S, breaking at line boundaries.
		Line breaks are not included in the resulting list unless keepends
		is given and true.
		"""

	def startswith(self, ???):
		"""
		S.startswith(prefix[, start[, end]]) -> bool
		
		Return True if S starts with the specified prefix, False otherwise.
		With optional start, test S beginning at that position.
		With optional end, stop comparing S at that position.
		prefix can also be a tuple of strings to try.
		"""

	def strip(self, ???):
		"""
		S.strip([chars]) -> string or unicode
		
		Return a copy of the string S with leading and trailing
		whitespace removed.
		If chars is given and not None, remove characters in chars instead.
		If chars is unicode, S will be converted to unicode before stripping
		"""

	def swapcase(self, ???):
		"""
		S.swapcase() -> string
		
		Return a copy of the string S with uppercase characters
		converted to lowercase and vice versa.
		"""

	def title(self, ???):
		"""
		S.title() -> string
		
		Return a titlecased version of S, i.e. words start with uppercase
		characters, all remaining cased characters have lowercase.
		"""

	def translate(self, ???):
		"""
		S.translate(table [,deletechars]) -> string
		
		Return a copy of the string S, where all characters occurring
		in the optional argument deletechars are removed, and the
		remaining characters have been mapped through the given
		translation table, which must be a string of length 256 or None.
		If the table argument is None, no translation is applied and
		the operation simply removes the characters in deletechars.
		"""

	def upper(self, ???):
		"""
		S.upper() -> string
		
		Return a copy of the string S converted to uppercase.
		"""

	def zfill(self, ???):
		"""
		S.zfill(width) -> string
		
		Pad a numeric string S with zeros on the left, to fill a field
		of the specified width.  The string S is never truncated.
		"""

