import random


# INPUT
def getGenome(length=1000): #generate a random genome seq ending with $ character
    genome = "".join(random.choice('ATCG') for i in range(length))
    genome+='$'
    return genome


#computes all the rotations (each time the first char of the running string is placed at the end of it) of the string t
def Rotations(t):
    s=t #copy of t
    s = s[1:] + s[0] #place the first character at the endo of the string
    rot = [s] #store all rotations in a list
    while s!=t: #until u reach back the initial string
        s = s[1:] + s[0] #place the first character at the endo of the string
        rot.append(s) #append new rotation to the list
    return rot


#computes the Burrows-Wheeler transformation of the string
def bwt(t):
    r=sorted(Rotations(t))  #generate sorted rotations of the string
    bwtstring='' #initialize empty string
    for s in r: #iterate through all char of the last line in each rotation after sorting them
        bwtstring+=s[-1] #adding last char of each rotation string to the bwt string
    return bwtstring


#stores the index of each of the occurencies of the element c in the list l
def all_indexes(l, c):
    # for each index i and element x of the list l
    idxs = [i for i, x in enumerate(l) if x == c]  # if x is equal to the searched character c its position index in l is stored in a list
    return idxs


#returns the rank of a given character c in position i in a given list l
def rank(c,l,i):
    count=l[0: (i + 1)].count(c) #in the sliced list l from 0 to the index of c (c included) i+1, counts how many c characters occur
    return (count-1) #rank starts from 0


#returns the index of a character c in a list l known its rank r
def position(c,l,r):
    count=-1 #count of the rank encountered
    pos=-1 #store position
    while count<r and pos<len(l)-1: #count must not exceed the rank and we cannot count over the length of the list l
        pos += 1
        n=l[pos]
        if n==c:
            count+=1
    return pos


#compute reverse transformation of bwt
def revBwt(b):
    L= list(b) #last line of the bwt matrix is the bwt
    F = sorted(b) #the first line of the bwt matrix is  basically the bwt sorted
    index = 0 #start from the first position
    c = L[index] #character corresponding to $ in L
    inverted = "$" #intantiate the reverse transformation string of bwt
    while(c != '$'): #until we find in L a $
        inverted += c #add characters
        rank_c = rank(c, L, index)  #find rank of that character in L
        index = position(c,F,rank_c) #find the index of that character with given rank in F
        c = L[index]
    original = inverted[::-1] #we recunstructed from the bottom of the string so we need to invert it to have the original
    return original

#return array of offset matching with list l in its bwt
def offset(l):
    comb=[] #initialize list of tuple of (rotation,offset) combination
    o=1 #first offset
    rot=Rotations(l) #compute all rotation of the original string
    for r in rot: #iterate over each rotation
        comb.append((r,o)) #append tuple (rot,corresponding offset)
        o+=1 #increment the offset each iteration
    comb.sort()#sort combination (sorting works comparing first elements of the tuple)
    off=[] #initialize list of offsets after sorting
    for c in comb:
        off.append(c[1]) #append only the second element of the tuple which is the corresponding offset of that rotation
    return off


#defines if p read maps on t at which offset position
def match(t, p):
    F = list(sorted(t))  # first string
    L = list(bwt(t))  # bwt string
    q = list(p) #list of query string characters
    sol=[] #initialize solution list indx in L, more than one solution is possible
    c = q.pop(-1) #last query character
    
    #operations for first character check, check all in F list at the beginning
    indx = all_indexes(F, c)  # list of indexes of occurence of c in F
    for i in indx:
        if L[i] == q[-1]:  # if the corresponding character in L is equal to the characater before the current one in p
            sol.append(i) #add the index to the list
            
    #further operations on the rest of the character
    while len(q)>1 and len(sol)>0:
        f = sol.copy()  # create a copy of sol
        sol.clear()
        c=q.pop(-1) #remove the last character of query sequence and assign it to the variable c
        for i in f: #for each position stored in f
            r = rank(c,L,i) #get the rank of c in L list
            index=position(c,F,r) #from their rank retrieve their position in F
            if L[index]==q[-1]:
                sol.append(index) #if then there is a correspondance btw F and L, append the position to the solution
    if sol: #if sol is not empty
        o=offset(t) #generate the list of offsets of t
        off=[] #initialize list of the solutions offsets
        for s in sol: #for each element in the solutions list
            off.append(o[s]) #retrieve the offset corresponding to that position of L
        return (f'The query string {p} matches {t} at offset {off}')
    else:
        return 'No match has been found'
        


if __name__=="__main__":
    t=getGenome(20)
    #t = 'GAGTCCATTGAGTTTAG$'
    p='AG'
    print("Original: ", t)
    print('Query: ',p)
    #rotations= Rotations(t)
    #print("sorted rotations",sorted(rotations))
    #L = bwt(t)
    #print("Transformed: ", L)
    #original = revBwt(L)
    #print("Reversed bwt: ",original)
    print(match(t,p))
    #print('offset list', offset(t))
















