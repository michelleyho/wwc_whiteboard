#rotate array to the right by N
def rotateRightByN(a,n):
    #optimization:
    if n%len(a) == 0:
        print "same as not rotating"
        return a
    aNew = [0]*len(a)
    for i in range(len(a)):
        newIndex = (i+n)%(len(a))
        aNew[newIndex] = a[i]
    return aNew

if __name__=="__main__":
    a = [2,4,6,8]
    b = [2,4,6]
    c = [1,2,3,4,6]
    d = [10,34,53,21,100,2,4]
    print a
    a = rotateRightByN(a,3)
    print a
    print d
    d = rotateRightByN(d,6)
    print d
    print b
    b = rotateRightByN(b,6)
    print b
