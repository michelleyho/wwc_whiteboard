#print even array items in backwards order. 

def printEvenBackwards(a):
    print "original"
    print a
    endIndex = ((len(a)-1)/2)*2
    for i in range(endIndex,-1,-2):
        print a[i],
    print
    
if __name__ == "__main__":
    a = [2,4,6,8]
    printEvenBackwards(a)
    b = [2,4,6]
    printEvenBackwards(b)
    c = [1,2,3,4,6]
    printEvenBackwards(c)
    d = [10,34,53,21,100,2,4]
    printEvenBackwards(d)

