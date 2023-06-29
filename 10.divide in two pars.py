def findingroup(n):
    sum=0
    for i in range(1,n+1):
        sum+=i

    group1sum=sum//2
    group1=[]
    group2=[]

    for i in range(n,0,-1):

        if group1sum-i>=0:
            group1.append(i)
            group1sum-=i
        else:
            group2.append(i)

    print(len(group1))
    for x in group1:
        print(x,end=' ')
    print()
    print(len(group2))
    for x in group2:
        print(x, end=' ')

findingroup(6)