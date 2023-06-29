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

def findlargestpalindrome(s):
    l=list(s)

    dic={}

    for x in l:
        if x in dic:
            dic[x]+=1
        else:
            dic[x]=1

    arr=[]
    for x in dic:
        arr.append(int(x))

    odd=0

    for x in dic:
        if dic[x]%2==1:
            odd+=1
    if odd>1:
        print('not possible')
        return


    Quicksort(arr,0,len(arr)-1)




    number=[]

    for i in range(len(arr)):
        number.append(str(arr[i]))

    for j in range(len(arr)-1,-1,-1):
        number.append(str(arr[j]))



    print(''.join(number))









s = "313551"
findlargestpalindrome(s)

s = "313351"
findlargestpalindrome(s)



