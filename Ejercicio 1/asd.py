

import sys
import operator as op
def ncr(n, r):
	if n == 1: return 1
	r = min(r, n-r)
	if r == 0: return 1
	numer = reduce(op.mul, xrange(n, n-r, -1))
	denom = reduce(op.mul, xrange(1, r+1))
	return numer//denom


a = int(sys.argv[1])
c = int(sys.argv[2])

print 'ac: ' + str(a * c)
print 'cc: ' + str(ncr(c, 2))
print 'aa: ' + str(ncr(a, 2))

print 'a: ' + str(a)
print 'c: ' + str(c)

print 'suma: ' + str((a * c) + ncr(c, 2) + ncr(a, 2) + a + c)
