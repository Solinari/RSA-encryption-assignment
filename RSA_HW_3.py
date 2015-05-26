# RSA
import math
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

def checkPrimes():
    '''fix p and q to be prime'''

    p = random.getrandbits(32)
    q = random.getrandbits(32)
    
    c = [p, q]
    f = True

    while f:
        for i in range(len(c)):
            
            y = int(math.sqrt(c[i])) + 1

            for j in range(2, y):

                if pow(c[i],1,j) == 0:
                    print("Not a prime: {}, this prime mod {} = {}".format(c[i], j,pow(c[i],1,j)))
                    c[i] = random.getrandbits(32)
                    continue
            print("confirmed prime: {}, this prime mod it's square root:{} = {}".format(c[i], y,pow(c[i],1,y)))
        f = False

    return c

def getE(m):
    '''gcd x by random ints less than it till you get a prime'''

    e = random.randrange(1,m)

    while gcd(e,m) != 1:
    
        e = random.randrange(1,m)
        
    return e

#GenerateKeys


def GenerateKeys():
    '''make p,q,n,m,e,d'''

    # k can be anything. start at 32 to force me to code efficiantly
    # but try to make 2048 work for the lawl
    
    #check p and q fix them if they ain't prime
    c = checkPrimes()

    p = c[0]
    q = c[1]   
                    
    print("p: {} q: {} are prime!".format(p,q))
        
    n = p * q
    m = (p - 1) * (q - 1)
    print("m {}".format(m))
    e = getE(m)
    print("e {}".format(e))
    d = 1 ##    FIX THIS. USE EXTENDED EUCLIDIAN ALGORITHM!!!!
    print("d {}".format(d))



GenerateKeys()

#Encrypt



#Decrypt

