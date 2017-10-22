import math
import matplotlib.pyplot as plt

def num2list(n,b):
    if b == 2: return([int(x) for x in list("{0:b}".format(n))])
    elif b == 10: return([int(x) for x in list("{0:d}".format(n))])


def list2num(l,b):
    n = 0
    for x in range(0,len(l)):
        n += math.pow(b,x)*int(l[len(l)-x-1])
    return n

# Note that the order of magnitude won't change.
def pairsum(n,b):
    l = num2list(n,b)
    pl = [] if len(l) != 1 else l
    if pl != l:
        pl.append( (0+l[0]+l[1]) %b)
        for x in range(1,len(l)-1):
            pl.append( (l[x-1]+l[x]+l[x+1]) %b)
        if len(l)>2: pl.append( (l[len(l)-2]+l[len(l)-1]+0) %b)
    return list2num( pl,b )

base = 10
k = 100000
plt.plot(range(0,k), [pairsum(x,base) for x in range(0,k)])

plt.ylabel('triplet digit sum, mod '+str(base))
plt.show()

# Every power of the base, the pattern repeats.
# The pattern for 10-100 is the pattern of 1-10 repeated 10 times plus
# the pattern of 1-10 slowed down by a factor of 10 and increased in amplitude
# by a factor of 10. Super-positioned fractal 'waves' for each period.
# Hence it is easy to see how changing the number of actors in a set of
# CA changes the first step.