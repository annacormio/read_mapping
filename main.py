import random
import itertools


# INPUT
def getGenome(length=1000):
    genome = "".join(random.choice('ATCG') for i in range(length))
    return genome



def sortedRotations(t):
    s=t
    rot=[s]
    s=s[1:]+s[0]
    while s!=t:
        rot.append(s)
        s = s[1:] + s[0]
    return sorted(rot)


def bwt(t): #implement Burrows-Wheeler transform compression of the string
    r=sortedRotations(t)
    bwtstring=''
    for s in r:
        bwtstring+=s[-1:]
    return bwtstring











#def revBwt():




if __name__=="__main__":
    #t=getGenome(5)
    t='ATCG$'
    print(t)
    print(sortedRotations(t))
    print(bwt(t))