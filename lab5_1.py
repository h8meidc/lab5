suma=0
count=0
N=int(input("N = "))
print(f"Enter {N} array elements:")

arr = [int(input()) for _ in range(N)]

for i in range(0,N):
    if arr[i]%2!=0:
        suma+=arr[i]
        count+=1
print("Середнє арифметичне непарчих чисел масиву = ", suma/count)
print("Від'ємні елементи масив у зворотньому порядку: ", end=" ")
count=0
for i in range(N-1,-1,-1):
     if arr[i]<0:
         print(arr[i]," ", end=" ")
         count=1
if count==0:
    print("Від'ємних чисел не знайдено")
         