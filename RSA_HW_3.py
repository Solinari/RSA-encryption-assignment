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

    p = random.randrange(32768, 65535 + 1)
    q = random.randrange(32768, 65535 + 1)
    
    c = [p, q]
    f = True

    while f:
        for i in range(len(c)):
            
            y = int(math.sqrt(c[i])) + 1

            for j in range(2, y):

                if pow(c[i],1,j) == 0:
                    #print("Not a prime: {}, this prime mod {} = {}".format(c[i], j,pow(c[i],1,j)))
                    c[i] = random.randrange(32768, 65535 + 1)               
                    continue
            print("confirmed prime: {} this prime mod it's square root:{} = {}".format(c[i], y-1,pow(c[i],1,y)))
        f = False

    return c

def getE(m):
    '''gcd x by random ints less than it till you get a prime'''

    #idk how small orlarge to make e...
    e = random.randint(3,int(math.sqrt((math.sqrt(m)))))
    #e = random.randint(3,int(math.sqrt((math.sqrt(m)))))

    while gcd(e,m) != 1:

        e = random.randint(3,int(math.sqrt((math.sqrt(m)))))


        
    return e

def getInv(w, u):
    '''get inverse mod'''

    t = 0
    nt = 1
    r = u
    nr = w

    while nr != 0:
        qu = r // nr
        t, nt = nt, t - qu * nt
        r, nr = nr, r - qu * nr

    if r > 1:
        return 0

    if t < 0:
        t += u

    return t


#GenerateKeys



def GenerateKeys():
    '''make p,q,n,m,e,d'''

    # k can be anything. start at 32 to force me to code efficiantly
    # but try to make 2048 work for the lawl
    
    #check p and q fix them if they ain't prime
    c = checkPrimes()

    p = int(c[0])
    q = int(c[1])
                    
    print("p: {}\nq: {}".format(p,q))
        
    n = p * q
    print("n: {}".format(n))
    m = (p - 1) * (q - 1)
    print("m: {}".format(m))
    e = getE(m)
    print("e: {}".format(e))
    d = getInv(e, m)
    print("d: {}".format(d))

    out = [p,q,n,m,e,d]

    return out

# now the easy parts

#Encrypt
def RSAEncrypt(theint, e, n):

    return pow(theint, e, n)


#Decrypt
def RSADecrypt(theint,d,e, n):

    return  pow(pow(theint,e), d, n)

gen = GenerateKeys()

myint = random.randrange(3, gen[3])

print(myint)

print(RSAEncrypt(myint, gen[4],gen[2]))

print(RSADecrypt(myint, gen[5], gen[4],gen[2]))

