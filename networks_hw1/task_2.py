import math

b = 3000
v = 16

print "max data rate: {0} b/sec".format(2 * b * math.log(v, 2))
print "max data rate: {0} b/sec".format(b * math.log(1 + 100, 2))