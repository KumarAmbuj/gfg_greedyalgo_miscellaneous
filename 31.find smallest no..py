def findsmallest(n):
    m=n
    number=''
    for i in range(9,0,-1):
        res=n//i
        n=n%i
        a=(str(i))*res
        number=a+number
    s=('0')*m

    number=number+s
    return number

print(findsmallest(5))