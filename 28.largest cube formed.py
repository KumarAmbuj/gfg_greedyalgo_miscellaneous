import math
def findcubes(n):
    l=[]
    for i in range(1,math.ceil(n**(1.0/3.0))):
        l.append(str(i**3))
    print(l)
    return l


def findlargestcube(n):

    arr=findcubes(n)

    s=str(n)

    for i in range(1,len(s)):
        for j in range(i,len(s)+1):
            a=s[0:j-i]+s[j:]
            if a in arr:
                return a

print(findlargestcube(876))




