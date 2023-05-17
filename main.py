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

    rot = sorted(rot)
    print("Sorted Rotations: ", rot)
    return rot


def bwt(t): #implement Burrows-Wheeler transform compression of the string
    r=sortedRotations(t)
    bwtstring=''
    for s in r:
        bwtstring+=s[-1:]
    return bwtstring


def revBwt(b):
    t=""
    #Counts each char occurrencies
    chars = list(b)  #corresponds to last matrix column
    ordered = sorted(chars) #corresponds to the first matrix column
    print(chars, "\n", ordered)
    inverted = ""
    c = ordered[0]
    i = 0
    count = 0
    countOccorrenze = 0
    countNuoveOccorrenze = 0
    for i in range(len)


        countOccorrenze = 0
        countNuoveOccorrenze = 0
        count += 1

    while True:
        inverted += c
        c = chars[i]
        occ = chars[0:i + 1].count(c)

        idxs = [i for i, x in enumerate(ordered) if x == c] #given a list and an element, find all the occurrencies of that element in the list
        i = idxs[occ-1]




    original = inverted[::-1]
    return original


if __name__=="__main__":
    #t=getGenome(5)
    t='AAACTTG$'
    print("Orig.: ", t)

    transformed = bwt(t)
    print("Transformed: ", transformed)

    original = revBwt(transformed)
    print(original)



