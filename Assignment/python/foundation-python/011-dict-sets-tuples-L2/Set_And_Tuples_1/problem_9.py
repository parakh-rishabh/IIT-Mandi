set1={10, 20, 30, 40, 50}
set2={40, 50, 60, 70, 80}
str1=""
for i in set1:
    if(i not in set2):
        str1+=str(i)+" "
print(str1)  