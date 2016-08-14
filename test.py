l = []

for x in xrange(-1,2):
	for y in xrange(-1,2):
		for z in xrange(-1,2):
			for a in xrange(-1,2):
				for b in xrange(-1,2):
					for c in xrange(-1,2):
						res = x*1 + y*3 + z*9 + a*27 + b*81 + c*243
						if res == 135:
							print str(x)+str(y)+str(z)+str(a)+str(b)+str(c)
						#if res >= 0:
						l.append(res)

l.sort()

print l