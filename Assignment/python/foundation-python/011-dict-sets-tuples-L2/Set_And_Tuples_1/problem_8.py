set1={1, 2, 3, 4}
set2={3, 4, 5, 6}
str1=""
for i in set1:
    if(i not in set2):
        str1+=str(i)+" "
for i in set2:
    if(i not in set1):
        str1+=str(i)+" " 
print(str1)               
    