def partition(arr,p,r):
    x=arr[r]
    i=p-1

    for j in range(p,r):
        if arr[j]<x:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[r]=arr[r],arr[i+1]
    return i+1

def Quicksort(arr,p,r):
    if p<r:
        q=partition(arr,p,r)
        Quicksort(arr,p,q-1)
        Quicksort(arr,q+1,r)

def findmax(arr,k):

    n=len(arr)

    sum=0
    i=-1
    j=n-1

    while(True):

        a=arr[j]
        sum+=a
        arr[j]=0

        for c in range(k):
            i+=1
            if arr[i]==0:
                return sum
            else:
                arr[i]=0
        j-=1

def findmin(arr,k):
    n=len(arr)
    j=0
    i=n
    sum=0

    while(True):
        a=arr[j]
        sum+=a
        arr[j]=0
        for c in range(k):
            i-=1
            if arr[i]==0:
                return sum
            else:
                arr[i]=0
        j+=1



def findminmax(arr,k):
    n=len(arr)
    Quicksort(arr,0,n-1)

    a=arr.copy()
    b=arr.copy()

    print(findmax(a,k))
    print(findmin(b, k))


price = [3, 2, 1, 4]
k = 2

findminmax(price,k)


