import random

# INPUT
def getGenome(length=1000): #generate a random genome seq ending with $ character
    genome = "".join(random.choice('ATCG') for i in range(length))
    genome+='$'
    return genome


#computes all the rotations (each time the first char of the running string is placed at the end of it) of the string t
def sortedRotations(t):
    s=t
    rot=[s]
    s=s[1:]+s[0]
    while s!=t:
        rot.append(s)
        s = s[1:] + s[0]
    return sorted(rot)


#computes the Burrows-Wheeler transform compression of the string
def bwt(t):
    r=sortedRotations(t) #generate sorted rotations of the string
    bwtstring=''
    for s in r: #iterate through all char of the last line building BWT
        bwtstring+=s[-1] #adding last char of each rotation string
    return bwtstring


#stores the index of each of the occurencies of the element c in the list l
def all_indexes(l, c):
    # for each index i and element x of the list l
    idxs = [i for i, x in enumerate(l) if x == c]  # if x is equal to the searched character c its position index in l is stored in a list
    return idxs


#finds the number of occurrences of an element c in the list l searching it up to the indexed position i
def occurrences(l,i,c):
    return l[0: (i + 1)].count(c) #in the sliced list from 0 to the index i+1 of c (c included) in the list l, counts how many c characters occur

def revBwt(b):
    L= list(b) #last line of the bwt matrix is the bwt
    F = sorted(b) #the first line of the bwt matrix is  basically the bwt sorted
    index = 0 #start from the first position
    c = L[index] #character corresponding to $ in L
    inverted = "$" #intantiate the reverse transformation string of bwt
    while(c != '$'): #until we find in L a $
        inverted += c
        occ_c_L = occurrences(L,index,c) #counting number of occurences of c in L up to the position of L in which we are
        index = all_indexes(F,c)[occ_c_L-1]
        c = L[index]
    original = inverted[::-1] #we recunstructed from the bottom of the string so we need to invert it to have the original
    return original

if __name__=="__main__":
    t=getGenome(10)
    #t = 'ACACAGTACCGTA$'
    print("Original: ", t)
    rotations=sortedRotations(t)
    print("soted rotations",rotations)
    transformed = bwt(t)
    print("Transformed: ", transformed)
    original = revBwt(transformed)
    print("Reversed bwt: ",original)



