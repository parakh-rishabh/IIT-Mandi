def findMinMax(arr):
    max=arr[0]
    for num in arr:
        if(num>max):
            max=num
    return max
arr = [15, 2, 34, 8, 19]            
result=findMinMax(arr)
print(result)