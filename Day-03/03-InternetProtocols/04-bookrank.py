#!/usr/bin/env python

from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib2 import urlopen as uopen

REGEX = compile('#([\d,]+) in Books ')
AMZN = 'https://www.amazon.com/dp/'
ISBNs = {
    '1539406660': 'Node.js Jump start',
    '1617290572': 'Node.js in action',
    '0137143419': 'Python Fundamentals',
}

def getRanking(isbn):
    url = '{0}{1}'.format(AMZN, isbn)
    print url
    page = uopen('{0}{1}'.format(AMZN, isbn)) # '{0}{1}'.format(AMZN, isbn)) for 2.6+
    data = page.read()
    page.close()
    return REGEX.findall(data)[0]

def _showRanking(isbn):
    print '- %r ranked %s' % (
        ISBNs[isbn], getRanking(isbn))

def _main():
    print 'At', ctime(), 'on Amazon...'
    for isbn in ISBNs:
        Thread(target=_showRanking, args=(isbn,)).start()#_showRanking(isbn)

@register
def _atexit():
    print 'all DONE at:', ctime()

if __name__ == '__main__':
    _main()
