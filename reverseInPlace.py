#reverse an array in place. 

def reverseSwap(a):
   for i in range(len(a)/2):
        a[i],a[len(a)-i-1] = a[len(a)-i-1],a[i] 


if __name__=="__main__":
    a = [2,4,6,8]
    print a, "-->",
    reverseSwap(a)
    print a
    b = [2,4,6]
    print b, "-->",
    reverseSwap(b)
    print b
    c = [1,2,3,4,6]
    print c, "-->",
    reverseSwap(c)
    print c
    d = [10,34,53,21,100,2,4]
    print d, "-->",
    reverseSwap(d)
    print d
