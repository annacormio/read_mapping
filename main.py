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

"""
t=""
    #Counts each char occurrencies
    chars = list(b)  #corresponds to last matrix column
    ordered = sorted(chars) #corresponds to the first matrix column
    print(chars, "\n", ordered)
    inverted = ""
    
    c = ordered[0]
    i = 0
    x = ''
    count = 0
    countOccorrenze = 0
    countNuoveOccorrenze = 0
    while x != '$':
        x = chars[i]
        inverted += x
        for j in range(count + 1):
            if chars[j] == x:
                countOccorrenze += 1
        for j in range(len(ordered)):
            if ordered[j] == x:
                countNuoveOccorrenze += 1
                if countNuoveOccorrenze == countOccorrenze:
                    i = j
                    break
        countOccorrenze = 0
        countNuoveOccorrenze = 0
        count = i
        x = chars[i]
    original = inverted[::-1]
    original += '$'
    return original
"""
def revBwt(b):
    #given a list and an element, find all the occurrencies_indexes of that element in the list
    def all_indexes(list, c):
          idxs = [i for i, x in enumerate(list) if x == c]
          return idxs
    #given a list and an index, and an element, find
    def occurrences(list,index):
          return list[0: (index + 1)].count(c)

    chars = list(b)
    ord_chars = sorted(chars)

    index = 0
    c =  chars[index]
    inverted = "$"

    while(c != '$'):
        inverted = inverted + c
        occ_c = occurrences(chars, index)
        index = all_indexes(ord_chars,c)[occ_c-1]
        c = chars[index]

    print(inverted)
    original = inverted[::-1]
    return original

if __name__=="__main__":
    #t=getGenome(5)
    t = 'abtttttaajjccba$'
    print("Orig.: ", t)

    transformed = bwt(t)
    print("Transformed: ", transformed)

    original = revBwt(transformed)
    print(original)



