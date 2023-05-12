import random
import itertools


# INPUT
def getGenome(length=1000):
    genome = "".join(random.choice('ATCG') for i in range(length))
    return genome

def bwt(t): #implement Burrows-Wheeler transform compression of the string
    s=t.copy()
    s.remove(t[0])
    s.append(t[0])


    rot=[]





def revBwt():




if __name__=="__main__":
    t=getGenome(20)