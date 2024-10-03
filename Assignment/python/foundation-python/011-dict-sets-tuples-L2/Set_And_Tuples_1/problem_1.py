arr=[1, 2, 2, 3, 4, 5, 3, 6, 4]
dic={}
for i in arr:
    if dic.get(i)==None:
      dic[i]=1
    else:
       dic[i]+=1
for key in dic:
   if(dic[key]==1):
      print(key,end=" ")
print()      

