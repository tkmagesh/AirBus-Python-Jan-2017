

import shelve
from contextlib import closing

with closing(shelve.open('test_shelf.db')) as s:
    s['key1'] = { 'int': 10, 'float':9.5, 'string':'Sample data' }
    s['key2'] = { 'int': 120, 'float':6.5, 'string':'Sample data' }
    s['key3'] = { 'int': 130, 'float':9.5, 'string':'Sample data' }
    s['key4'] = { 'int': 150, 'float':8.5, 'string':'Sample data' }
