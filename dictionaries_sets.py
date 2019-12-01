from collections import defaultdict
from collections import Counter
from collections import OrderedDict
from collections import UserDict
from types import MappingProxyType
import collections.abc as abc

from pprint import pprint


"""
handling missing keys with setdefault instead of
the get method to avoid scanning the dict twice
"""

#using get
get_dict = {'a': [1,2,3]}
val_result = get_dict.get('b', [])
val_result.append(1)
get_dict['b'] = val_result
pprint(get_dict)


#using default value
test_dict = {'a': [1,2,3]}
test_dict.setdefault('b', []).append(1)
pprint(test_dict)

"""
dictionary comprehnsion - dynamically create dictionaries
much like list comprehnsion
"""

country_codes = [
				(1, 'United States'),
				(86, 'China'),
				(91, 'India')
]

code_dict = {country: code for code, country in country_codes}
pprint(code_dict)

"""
default dict as an alternative to using get
or setdefault method

__missing__ method using the default_factory used to initialize 
"""

df_dict = defaultdict(list)
df_dict[1].append('hello world')

pprint(df_dict[1])
pprint(df_dict[2])

"""
Varitations of dict

	* Counter
	* OrderDict
"""

c = Counter(['dog', 'dog', 'cat', 'dog'])
pprint(c)
pprint(c.most_common(1))


"""
Userdict for dictionary subclassing
"""

class StrKeyDict(UserDict):
	"""
	garentees keys in dictionary are cast to strings
	"""
	def __contains__(self, key):
		return str(key) in self.data

	def __setitem__(self, key, item):
		self.data[str(key)] = item


custom_dict = StrKeyDict()
custom_dict[100] = 'hello world'
pprint(custom_dict)


"""
Immutable Mappings
dynamic view mapping entries 
"""

d = {'02134': 'Allston, MA', '02871': 'Portsmouth, RI'}

pprint(MappingProxyType(d))



