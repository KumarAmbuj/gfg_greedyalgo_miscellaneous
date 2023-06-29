def findmin(arr,k):
    mx=max(arr)
    res=0

    for i in range(len(arr)):

        if (mx-arr[i])%k!=0:
            return -1
        else:
            res+=(mx-arr[i])//k

    return res

arr = [21, 33, 9, 45, 63]
n = len(arr)
k = 6
print(findmin(arr, k))