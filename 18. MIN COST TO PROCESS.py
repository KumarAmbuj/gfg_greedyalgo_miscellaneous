def findmincost(arr,n):
    core=[0 for i in range(n)]
    cost=0
    i=0
    for x in arr:

        if x in core:
            core[i]=x
            i+=1
            if i==n:
                i=0

        else:
            core[i] = x
            cost += 1
            i += 1
            if i == n:
                i = 0
    return cost

n = 3
m = 6
arr = {1, 2, 1, 3, 4, 1}
print(findmincost(arr,n))

n = 3
m = 31,
arr = {7, 11, 17, 10, 7, 10, 2, 9, 2, 18, 8, 10, 20, 10, 3, 20,
       17, 17, 17, 1, 15, 10, 8, 3, 3, 18, 13, 2, 10, 10, 11}
print(findmincost(arr,n))

n = 2
m = 6
arr = {1, 2, 1, 3, 2, 1}
print(findmincost(arr,n))