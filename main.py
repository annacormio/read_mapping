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


#returns the rank of a given character c in position i in a given list l
def rank(c,l,i):
    count=l[0: (i + 1)].count(c)
    return (count-1) #in the sliced list from 0 to the index i+1 of c (c included) in the list l, counts how many c characters occur

#return array of offset matching with L list
#def offset(t):



#returns the index of a character c in a list l known its rank r
def position(c,l,r):
    count=-1 #count of the rank encountered
    pos=-1 #store position
    while count<r and pos<len(l)-1:
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
        inverted += c
        rank_c = rank(c, L, index)  #counting number of occurences of c in L up to the position of L in which we are
        index = position(c,F,rank_c)
        c = L[index]
    original = inverted[::-1] #we recunstructed from the bottom of the string so we need to invert it to have the original
    return original

#defines if p read maps on t
def match(t, p):
    F = list(sorted(t))  # first string
    L = list(bwt(t))  # bwt string
    q = list(p)
    sol=[] #initialize solution list indx in L, more than one solution is possible
    c = q.pop(-1) #last query character
    
    #operations for first character check, check all in F list at the beginning
    indx = all_indexes(F, c)  # list of indexes of occurence of c in F
    for i in indx:
        if L[i] == q[-1]:  # if the corresponding character in L is equal to the characater befoe the current one in p
            sol.append(i) #add the index to the list
            
    #further operations on the rest of the character
    while len(q)>1 and len(sol)>0:
        pos = sol.copy()  # create a copy of sol
        sol.clear()
        c=q.pop(-1)
        for p in pos:
            r = rank(c,L,p) #get the rank of c in L list
            i=position(c,F,r) #from their rank I retrieve their position in F
            if L[i]==q[-1]:
                sol.append(i) #if then there is a correspondance btw F and L, append the position to the solution

    return sol
        


if __name__=="__main__":
    #t=getGenome(20)
    t = 'ACGCATGCA$'
    p='GCA'
    print("Original: ", t)
    print('Query: ',p)
    rotations=sortedRotations(t)
    #print("soted rotations",rotations)
    L = bwt(t)
    F = sorted(t)
    print("Transformed: ", L)
    original = revBwt(L)
    print("Reversed bwt: ",original)
    match=match(t,p)
    print('matching? ',match)
    #print('position',position('G',list(t),0))













