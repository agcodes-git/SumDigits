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
def repeat(f, n):
     if n==0:
             return (lambda x: x)
     return (lambda x: f (int(repeat(f, n-1)(x))))

# The base of the number is analogous to the size of the neighborhood.
# The number of digits is analogous to the number of CA.
base = 2
k = 512

# For binary. Map the result of the application of a rule to the original set of CA, expressed as a number.
def apply_rule(n,rule_number):
    s = num2list(n,2) # This is our set of starting automata.
    ns = [] # The new set. Empty at first.

    #print('Starting set: ', s)

    rule = num2list(rule_number,2)
    while len(rule)<8: rule.insert(0,0)
    #print('Rule',rule_number,rule)

    # We will assume that the edge elements are 0s.
    #print('Left edge: ', [0]+s[0:2])
    ns.append( int(rule[int(list2num([0]+s[0:2],2))]))
    for x in range(1,len(s)-1):
        set_of_3 = s[x-1:x+2]
        ns.append( int(rule[int(list2num(s[x-1:x+2],2))]) )
        #print(set_of_3)
    #print('Right edge: ', s[len(s)-2:len(s)]+[0])
    ns.append( int(rule[int(list2num(s[len(s)-2:len(s)]+[0] , 2))]))
    return list2num(ns,2)

iterations = 5 # How many times should we apply the rule to each set of cellular automata?
                # Keep in mind that currently one can't propagate outside of the magnitude borders.

for r in range(0,255):
    composed_rule = repeat( lambda x: apply_rule(x,r), 1 ) # Curry and repeatedly compose apply_rule.
    plt.plot( range(0,100), [composed_rule(x) for x in range(0,100)])

plt.show()