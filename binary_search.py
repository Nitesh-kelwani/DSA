def binary_search(data,key):
    start=0
    end=len(data)-1

    while start<=end:
        middle=(start+end)//2

        if key==data[middle]:
            return middle
        elif key>data[middle]:
            start=middle+1
        else:
            end=middle-1
    return -1



data_l=[10,20,27,36,45,69,75,84]
serach_key=84

output=binary_search(data_l,serach_key)

if output!=-1:
    print(f"{data_l[output]} is found at index {output}")
else:
    print("Element not found")