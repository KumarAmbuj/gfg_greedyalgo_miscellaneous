def findsmallest(s,n):
    res=[0]*n
    s=s-1

    for i in range(n-1,0,-1):
        if s>9:
            res[i]=9
            s=s-9
        else:
            res[i]=s
            s=0
    res[0]=s+1
    for x in res:
        print(x,end=' ')

findsmallest(20,3)