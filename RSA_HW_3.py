# RSA
import random
from fractions import gcd
import inspect

# uncomment this print to see the python implementation of gcd(a,b)
#print(inspect.getsource(gcd))
##def gcd(a, b):
##    """Calculate the Greatest Common Divisor of a and b.
##
##    Unless b==0, the result will have the same sign as b (so that when
##    b is divided by it, the result comes out positive).
##    """
##    while b:
##        a, b = b, a%b
##    return a

#helpers
def getE(x):
    '''gcd x by random ints less than it till you get a prime'''

    e = random.randrange(1,x)

    while gcd(e,x) != 1:
    
        e = random.randrange(1,x)
        
    return e

#GenerateKeys


def GenerateKeys():
    '''make p,q,n,m,e,d'''

    # k can be anything. start at 32 to force me to code efficiantly
    # but try to make 2048 work for the lawls
    p = random.getrandbits(32)
    q = random.getrandbits(32)
    n = p * q
    x = (p - 1) * (q - 1)
    e = getE(x)
    #d is broken, fix d.
    d = pow(e, -1, n)
    print(d)

    #test -this works pretty fast
    #print(hex(p))

GenerateKeys()

#Encrypt



#Decrypt

