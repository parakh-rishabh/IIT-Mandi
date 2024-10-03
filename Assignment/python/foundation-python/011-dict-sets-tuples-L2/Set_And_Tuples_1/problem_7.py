arr=[1, 2, 3, 4, 3, 2, 1]
arr.sort()
list1=[]
dic={}
for i in arr:
    if(dic.get(i)==None):
        dic[i]=1
for key in dic:
    list1.append(key)
tup=tuple(list1) 
print(tup)



        





