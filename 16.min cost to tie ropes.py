class Node:
    def __init__(self,d):
        self.d=d
        self.left=None
        self.right=None

def Minheap():
    heap=[]
    return heap

def Add(heap,arr):
    for i in range(len(arr)):
        heap.append(arr[i])
    Buildminheap(heap)

def Minheapify(heap,i,n):
    min=i

    l=2*i+1
    r=2*i+2

    if l<n and heap[l].d<heap[i].d:
        min=l
    if r<n and heap[r].d<heap[min].d:
        min=r

    if min!=i:
        heap[i],heap[min]=heap[min],heap[i]
        Minheapify(heap,min,n)

def Buildminheap(heap):
    n=len(heap)

    for i in range((n-1)//2,-1,-1):
        Minheapify(heap,i,n)

def Extractmin(heap):
    n=len(heap)
    a=heap[0]
    heap[0]=heap[n-1]
    heap.pop()
    n=len(heap)
    Minheapify(heap,0,n)
    return a
def Insert(heap,x):
    heap.append(x)
    i=len(heap)-1
    while(i>0 and heap[i].d<heap[i//2].d):
        heap[i],heap[i//2]=heap[i//2],heap[i]
        i=i//2
def Size(heap):
    return len(heap)




def findmincost(arr):

    l=[]

    for i in range(len(arr)):
        l.append(Node(arr[i]))

    heap=Minheap()
    Add(heap,l)

    sum=0

    while(Size(heap)>1):

        a=0

        x=Extractmin(heap)
        y=Extractmin(heap)

        a=x.d+y.d
        sum+=a
        root=Node(a)
        root.left=x
        root.right=y
        Insert(heap,root)

    return sum

arr=[4,3,2,6]
print(findmincost(arr))




