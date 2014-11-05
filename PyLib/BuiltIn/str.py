class str():
	def __add__(???):
		"""
		Return self+value.
		"""

	def __class__(???):
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
		S.__format__(format_spec) -> str
		
		Return a formatted version of S as described by format_spec.
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

	def __mod__(???):
		"""
		Return self%value.
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

	def __rmod__(???):
		"""
		Return value%self.
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
		S.__sizeof__() -> size of S in memory, in bytes
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

	def capitalize(???):
		"""
		S.capitalize() -> str
		
		Return a capitalized version of S, i.e. make the first character
		have upper case and the rest lower case.
		"""

	def casefold(???):
		"""
		S.casefold() -> str
		
		Return a version of S suitable for caseless comparisons.
		"""

	def center(???):
		"""
		S.center(width[, fillchar]) -> str
		
		Return S centered in a string of length width. Padding is
		done using the specified fill character (default is a space)
		"""

	def count(???):
		"""
		S.count(sub[, start[, end]]) -> int
		
		Return the number of non-overlapping occurrences of substring sub in
		string S[start:end].  Optional arguments start and end are
		interpreted as in slice notation.
		"""

	def encode(???):
		"""
		S.encode(encoding='utf-8', errors='strict') -> bytes
		
		Encode S using the codec registered for encoding. Default encoding
		is 'utf-8'. errors may be given to set a different error
		handling scheme. Default is 'strict' meaning that encoding errors raise
		a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
		'xmlcharrefreplace' as well as any other name registered with
		codecs.register_error that can handle UnicodeEncodeErrors.
		"""

	def endswith(???):
		"""
		S.endswith(suffix[, start[, end]]) -> bool
		
		Return True if S ends with the specified suffix, False otherwise.
		With optional start, test S beginning at that position.
		With optional end, stop comparing S at that position.
		suffix can also be a tuple of strings to try.
		"""

	def expandtabs(???):
		"""
		S.expandtabs(tabsize=8) -> str
		
		Return a copy of S where all tab characters are expanded using spaces.
		If tabsize is not given, a tab size of 8 characters is assumed.
		"""

	def find(???):
		"""
		S.find(sub[, start[, end]]) -> int
		
		Return the lowest index in S where substring sub is found,
		such that sub is contained within S[start:end].  Optional
		arguments start and end are interpreted as in slice notation.
		
		Return -1 on failure.
		"""

	def format(???):
		"""
		S.format(*args, **kwargs) -> str
		
		Return a formatted version of S, using substitutions from args and kwargs.
		The substitutions are identified by braces ('{' and '}').
		"""

	def format_map(???):
		"""
		S.format_map(mapping) -> str
		
		Return a formatted version of S, using substitutions from mapping.
		The substitutions are identified by braces ('{' and '}').
		"""

	def index(???):
		"""
		S.index(sub[, start[, end]]) -> int
		
		Like S.find() but raise ValueError when the substring is not found.
		"""

	def isalnum(???):
		"""
		S.isalnum() -> bool
		
		Return True if all characters in S are alphanumeric
		and there is at least one character in S, False otherwise.
		"""

	def isalpha(???):
		"""
		S.isalpha() -> bool
		
		Return True if all characters in S are alphabetic
		and there is at least one character in S, False otherwise.
		"""

	def isdecimal(???):
		"""
		S.isdecimal() -> bool
		
		Return True if there are only decimal characters in S,
		False otherwise.
		"""

	def isdigit(???):
		"""
		S.isdigit() -> bool
		
		Return True if all characters in S are digits
		and there is at least one character in S, False otherwise.
		"""

	def isidentifier(???):
		"""
		S.isidentifier() -> bool
		
		Return True if S is a valid identifier according
		to the language definition.
		
		Use keyword.iskeyword() to test for reserved identifiers
		such as "def" and "class".
		
		"""

	def islower(???):
		"""
		S.islower() -> bool
		
		Return True if all cased characters in S are lowercase and there is
		at least one cased character in S, False otherwise.
		"""

	def isnumeric(???):
		"""
		S.isnumeric() -> bool
		
		Return True if there are only numeric characters in S,
		False otherwise.
		"""

	def isprintable(???):
		"""
		S.isprintable() -> bool
		
		Return True if all characters in S are considered
		printable in repr() or S is empty, False otherwise.
		"""

	def isspace(???):
		"""
		S.isspace() -> bool
		
		Return True if all characters in S are whitespace
		and there is at least one character in S, False otherwise.
		"""

	def istitle(???):
		"""
		S.istitle() -> bool
		
		Return True if S is a titlecased string and there is at least one
		character in S, i.e. upper- and titlecase characters may only
		follow uncased characters and lowercase characters only cased ones.
		Return False otherwise.
		"""

	def isupper(???):
		"""
		S.isupper() -> bool
		
		Return True if all cased characters in S are uppercase and there is
		at least one cased character in S, False otherwise.
		"""

	def join(???):
		"""
		S.join(iterable) -> str
		
		Return a string which is the concatenation of the strings in the
		iterable.  The separator between elements is S.
		"""

	def ljust(???):
		"""
		S.ljust(width[, fillchar]) -> str
		
		Return S left-justified in a Unicode string of length width. Padding is
		done using the specified fill character (default is a space).
		"""

	def lower(???):
		"""
		S.lower() -> str
		
		Return a copy of the string S converted to lowercase.
		"""

	def lstrip(???):
		"""
		S.lstrip([chars]) -> str
		
		Return a copy of the string S with leading whitespace removed.
		If chars is given and not None, remove characters in chars instead.
		"""

	def maketrans(???):
		"""
		Return a translation table usable for str.translate().
		
		If there is only one argument, it must be a dictionary mapping Unicode
		ordinals (integers) or characters to Unicode ordinals, strings or None.
		Character keys will be then converted to ordinals.
		If there are two arguments, they must be strings of equal length, and
		in the resulting dictionary, each character in x will be mapped to the
		character at the same position in y. If there is a third argument, it
		must be a string, whose characters will be mapped to None in the result.
		"""

	def partition(???):
		"""
		S.partition(sep) -> (head, sep, tail)
		
		Search for the separator sep in S, and return the part before it,
		the separator itself, and the part after it.  If the separator is not
		found, return S and two empty strings.
		"""

	def replace(???):
		"""
		S.replace(old, new[, count]) -> str
		
		Return a copy of S with all occurrences of substring
		old replaced by new.  If the optional argument count is
		given, only the first count occurrences are replaced.
		"""

	def rfind(???):
		"""
		S.rfind(sub[, start[, end]]) -> int
		
		Return the highest index in S where substring sub is found,
		such that sub is contained within S[start:end].  Optional
		arguments start and end are interpreted as in slice notation.
		
		Return -1 on failure.
		"""

	def rindex(???):
		"""
		S.rindex(sub[, start[, end]]) -> int
		
		Like S.rfind() but raise ValueError when the substring is not found.
		"""

	def rjust(???):
		"""
		S.rjust(width[, fillchar]) -> str
		
		Return S right-justified in a string of length width. Padding is
		done using the specified fill character (default is a space).
		"""

	def rpartition(???):
		"""
		S.rpartition(sep) -> (head, sep, tail)
		
		Search for the separator sep in S, starting at the end of S, and return
		the part before it, the separator itself, and the part after it.  If the
		separator is not found, return two empty strings and S.
		"""

	def rsplit(???):
		"""
		S.rsplit(sep=None, maxsplit=-1) -> list of strings
		
		Return a list of the words in S, using sep as the
		delimiter string, starting at the end of the string and
		working to the front.  If maxsplit is given, at most maxsplit
		splits are done. If sep is not specified, any whitespace string
		is a separator.
		"""

	def rstrip(???):
		"""
		S.rstrip([chars]) -> str
		
		Return a copy of the string S with trailing whitespace removed.
		If chars is given and not None, remove characters in chars instead.
		"""

	def split(???):
		"""
		S.split(sep=None, maxsplit=-1) -> list of strings
		
		Return a list of the words in S, using sep as the
		delimiter string.  If maxsplit is given, at most maxsplit
		splits are done. If sep is not specified or is None, any
		whitespace string is a separator and empty strings are
		removed from the result.
		"""

	def splitlines(???):
		"""
		S.splitlines([keepends]) -> list of strings
		
		Return a list of the lines in S, breaking at line boundaries.
		Line breaks are not included in the resulting list unless keepends
		is given and true.
		"""

	def startswith(???):
		"""
		S.startswith(prefix[, start[, end]]) -> bool
		
		Return True if S starts with the specified prefix, False otherwise.
		With optional start, test S beginning at that position.
		With optional end, stop comparing S at that position.
		prefix can also be a tuple of strings to try.
		"""

	def strip(???):
		"""
		S.strip([chars]) -> str
		
		Return a copy of the string S with leading and trailing
		whitespace removed.
		If chars is given and not None, remove characters in chars instead.
		"""

	def swapcase(???):
		"""
		S.swapcase() -> str
		
		Return a copy of S with uppercase characters converted to lowercase
		and vice versa.
		"""

	def title(???):
		"""
		S.title() -> str
		
		Return a titlecased version of S, i.e. words start with title case
		characters, all remaining cased characters have lower case.
		"""

	def translate(???):
		"""
		S.translate(table) -> str
		
		Return a copy of the string S, where all characters have been mapped
		through the given translation table, which must be a mapping of
		Unicode ordinals to Unicode ordinals, strings, or None.
		Unmapped characters are left untouched. Characters mapped to None
		are deleted.
		"""

	def upper(???):
		"""
		S.upper() -> str
		
		Return a copy of S converted to uppercase.
		"""

	def zfill(???):
		"""
		S.zfill(width) -> str
		
		Pad a numeric string S with zeros on the left, to fill a field
		of the specified width. The string S is never truncated.
		"""

