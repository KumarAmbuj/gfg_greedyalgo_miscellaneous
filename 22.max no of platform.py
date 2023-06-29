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

def findmaxplat(arv,depar):
    n=len(arv)

    Quicksort(arv,0,n-1)
    Quicksort(depar,0,n-1)

    ans=0
    i=0
    j=0
    pform=0

    while(i<n and j<n):
        if arv[i]<depar[j]:
            pform+=1
            ans=max(ans,pform)
            i+=1
        else:
            pform-=1
            ans=max(ans,pform)
            j+=1

    while(i<n):
        pform+=1
        ans=max(pform,ans)
        i+=1
    while(j<n):
        pform-=1
        ans=max(pform,ans)
        j+=1

    return ans

arr = [ 900, 940, 950, 1100, 1500, 1800 ];
dep = [ 910, 1200, 1120, 1130, 1900, 2000 ];
print(findmaxplat(arr,dep))


arr = [900, 940]
dep = [910, 1200]
print(findmaxplat(arr,dep))

