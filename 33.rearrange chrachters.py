import math
class Group:
    def __init__(self,d,f):
        self.d=d
        self.f=f

def Maxheap():
    heap=[]
    return heap
def Add(heap,arr):
    for i in range(len(arr)):
        heap.append(arr[i])
    Buildminheap(heap)

def Maxheapify(heap,i,n):
    max=i

    l=2*i+1
    r=2*i+2

    if l<n and heap[l].f>heap[i].f:
        max=l

    if r<n and heap[r].f>heap[max].f:
        max=r

    if max!=i:
        heap[i],heap[min]=heap[min],heap[i]
        Maxheapify(heap,min,n)

def Buildminheap(heap):
    n=len(heap)

    for i in range((n-1)//2,-1,-1):
        Maxheapify(heap,i,n)

def Extractmax(heap):
    a=heap[0]
    n=len(heap)
    heap[0]=heap[n-1]
    heap.pop()
    n=len(heap)
    Maxheapify(heap,0,n)
    return a
def Insert(heap,x):
    heap.append(x)
    i=len(heap)-1

    while(i>0 and heap[i].f>heap[i//2].f):
        heap[i],heap[i//2]=heap[i//2],heap[i]
        i=i//2

def Size(heap):
    return len(heap)



def rearrange(s):
    dic={}
    for x in s:
        if x in dic:
            dic[x]+=1
        else:
            dic[x]=1

    for x in dic:
        if dic[x]>math.ceil(len(s)/2):
            print('not possible')
            return

    arr=[]
    for x in dic:
        arr.append(Group(x,dic[x]))

    heap=Maxheap()
    Add(heap,arr)

    prev=Group('#',-1)

    res=''

    while(Size(heap)):
        x=Extractmax(heap)

        res=res+x.d

        if prev.f>0:
            Insert(heap,prev)

        x.f=x.f-1
        prev=x

    print(res)

str = "aaabb" ;
rearrange(str)

str = "aaabc" ;
rearrange(str)


