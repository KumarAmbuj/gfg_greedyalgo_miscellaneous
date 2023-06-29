def findminsquare(l,b,h):
    volume=l*b*h
    side=0
    i=1
    mn=999
    s=0
    while(i**3<volume):

        v=i**3
        s=volume/v
        if s==int(s):
            mn=min(mn,s)
            side=i
        i+=1
    print(side,mn)
findminsquare(2,4,6)
findminsquare(1,2,3)