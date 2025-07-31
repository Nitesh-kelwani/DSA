d=int(input("Enter the number of rotations :"))

def rotate_arr(arr,d):
    n=len(arr)
    
    for i in range(d):
        first=arr[0]
        for j in range(n-1):
            arr[j]=arr[j+1]
        arr[n-1]=first

def rotate_arr2(arr,d):
    n=len(arr)

    d%=n
    temp=[0]*n
    for i  in range(n-d):
        temp[i]=arr[d+i]

    for j in range(d):
        e=(n-d)+j
        temp[e]=arr[j]

    for i in range(n):
        arr[i]=temp[i]
    
# if __name__ == "__main__":


# rotate_arr(arr, d)
arr = [1, 2, 3, 4, 5, 6]
rotate_arr2(arr, d)

for i in range(len(arr)):
   print(arr[i], end=" ")
        