def deleteZeros_1(l):
    return [x for x in l if x != 0]

if __name__=="__main__":
    a = [1,3,4,2,0,0,1,0,2,3]
    a_1 = deleteZeros_1(a)
    print a_1
    b = [0,0,0]
    b_1 = deleteZeros_1(b)
    print b_1
    c = [2,3,4]
    c_1 = deleteZeros_1(c)
    print c_1
