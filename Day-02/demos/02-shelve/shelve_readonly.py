

import shelve
from contextlib import closing

with closing(shelve.open('test_shelf.db', flag='r')) as s:
    print(s['key1'])
    print(s['key3'])


