def findminrooms(arr,n,m):
    count=[0 for i in range(m)]

    for i in range(n):
        for j in range(m):
            if arr[i][j]=='1':
                count[j]+=1

    return max(count)

n = 3;
m = 7;
slots = ["0101011", "0011001", "0110111"];
print(findminrooms(slots, n, m));

n = 2
m = 7
slots = ["0101010", "1010101"]
print(findminrooms(slots, n, m));

