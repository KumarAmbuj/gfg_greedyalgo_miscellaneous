def findminsquare(a,b):
    count=0
    rem=0
    if a<b:
        a,b=b,a
    while(b>0):

        count+=int(a/b)
        rem=int(a%b)
        a=b
        b=rem

    return count


n = 13
m = 29

print(findminsquare(n, m))
