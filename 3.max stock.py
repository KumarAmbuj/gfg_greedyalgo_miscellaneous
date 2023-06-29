def maxstock(arr,k):
    n=len(arr)
    count=0
    sum=0
    i=1
    while(sum<k ):

        if i>n:
            return count

        a=arr[i-1]

        for j in range(i):
            sum=sum+a
            if sum>=k:
                return count
            else:
                count+=1
        i+=1

price = [ 10, 7, 19 ]
k = 45

print(maxstock(price,k))

price = [ 7, 10, 4 ]
k = 100

print(maxstock(price,k))