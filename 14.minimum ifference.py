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


def findmindiff(arr):
    n=len(arr)
    Quicksort(arr,0,n-1)

    diff=99

    for i in range(n//2):
        diff=min(diff,arr[n-1-i]-arr[i])
    return diff

a = [ 2, 6, 4, 3 ]
n = len(a)
print(findmindiff(a))