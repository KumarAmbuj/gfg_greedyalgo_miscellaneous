def fibo(k):
    l=[]
    l.append(1)
    l.append(1)
    i=2
    sum=l[i-1]+l[i-2]
    while(sum<k):

        l.append(sum)
        i=len(l)
        sum = l[i - 1] + l[i - 2]

    return l

def minfibo(k):

    arr=fibo(k)



    count=0

    i=len(arr)-1


    while(i>=0):

        count+=k//arr[i]
        k=k%arr[i]

        i-=1


    return count



K = 17
print(minfibo(K))

print(minfibo(77))