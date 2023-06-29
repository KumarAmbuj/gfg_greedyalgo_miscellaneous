def findmincurrency(amount,notes):
    i=0
    res=0
    n=len(notes)
    arr=[0]*n
    while(i<n):
        res=amount//notes[i]
        arr[i]=res
        amount=amount%notes[i]
        i+=1

    for i in range(len(arr)):
        if arr[i]!=0:
            print(notes[i],':',arr[i])

notes = [2000, 500, 200, 100,
               50, 20, 10, 5, 1]
findmincurrency(868,notes)
findmincurrency(2456,notes)
findmincurrency(800,notes)

