def findMinMax(arr):
    minn=arr[0]
    for num in arr:
        if(num<minn):
            minn=num
    return minn       

arr = [15, 2, 34, 8, 19]
result=findMinMax(arr)
print(result)

