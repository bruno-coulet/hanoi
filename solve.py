def hanoi(a,c,b,k):
    i=0
    if k > 0:
        hanoi(a,b,c,k-1)
        i=i+1
        print ("deplacement de",a,"vers",c)
        i=i+1
        hanoi(b,c,a,k-1)
        i=i+1
    return i
print(hanoi(1,3,2,8))