N=7

arr = [[int(i%2==0) for i in range(N)] for j in range(N)]

for i in range(N):
    for j in range(N):
        print(arr[i][j]," ", end=" ")
    print("")    