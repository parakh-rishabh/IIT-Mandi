# Reverse a String
# Write a function named reverseString that takes a string as input and returns the reverse of the string. Use this function to reverse a given string.
# reversedString = reverseString("hello");
# // Sample Output: reversedString = "olleh"


def reverseString(str1):
    n=len(str1)
    ans=""
    for char in range(n-1,-1,-1):
        ans+=str1[char]
    return ans    
        # print(char,end=" ")
result=reverseString("hello")
print(result)    
    


