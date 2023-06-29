#think greedily
def partition(arr,p,r):
    x=arr[r]
    i=p-1

    for j in range(p,r):
        if arr[j]>x:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[r]=arr[r],arr[i+1]
    return i+1
def Quicksort(arr,p,r):
    if p<r:
        q=partition(arr,p,r)
        Quicksort(arr,p,q-1)
        Quicksort(arr,q+1,r)

def findmincost(X,Y):
    n=len(X)
    m=len(Y)
    Quicksort(X,0,n-1)
    Quicksort(Y,0,m-1)

    cost=0
    vert=1
    hzntl=1
    i=0
    j=0

    while(i<n and j<m):
        if X[i]>Y[j]:
            cost+=X[i]*vert
            hzntl+=1
            i+=1
        else:
            cost+=Y[j]*hzntl
            vert+=1
            j+=1

    total=0
    while(i<n):
        total+=X[i]
        i+=1
    cost+=total*vert

    total=0
    while(j<m):
        total+=Y[j]
        j+=1
    cost+=total*hzntl
    return cost


X = [2, 1, 3, 1, 4]
Y = [4, 1, 2]
print(findmincost(X,Y))