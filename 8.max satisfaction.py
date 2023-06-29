class Bag():
    def __init__(self,w,index):
        self.w=w
        self.index=index

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

    if l<n and heap[l].w<heap[i].w:
        min=l
    if r<n and heap[r].w<heap[min].w:
        min=r

    if min!=i:
        heap[min],heap[i]=heap[i],heap[min]
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
def Top(heap):
    if len(heap)>0:
        return heap[0]




def solve(n,d,a,b,arr):
    bag=[]

    for i in range(len(arr)):
        bag.append(Bag((arr[i][0]*a + arr[i][1]*b),i+1))



    heap=Minheap()
    Add(heap,bag)



    sum=0
    count=0
    l=[]

    while((d-sum)>Top(heap).w):
        x=Extractmin(heap)
        sum+=x.w
        count+=1
        l.append(x.index)

    print(count)
    for x in l:
        print(x,end=' ')



n = 5
d = 5
a = 1
b = 1
arr = [[2, 0], [3, 2],
       [4, 4], [10, 0],
       [0, 1]]

solve(n, d, a, b, arr)

n = 6
d = 1000000000
a = 9999
b = 10000

arr = [[10000, 9998], [10000, 10000],
       [10000, 10000],
       [70000, 70000],[10000,10000],[10000,10000]]
solve(n,d,a,b,arr)