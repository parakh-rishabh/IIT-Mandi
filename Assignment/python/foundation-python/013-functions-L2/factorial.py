# Write a function named calculateFactorial that takes an integer n as input and returns the factorial of n (n!). Use this function to calculate the factorial of a given number.

# result = calculateFactorial(5);

# // Sample Output: result = 120

def calculateFactorial(n):
    fac=1
    for num in range(n,0,-1):
        fac=fac*num
    return fac 
      
result= calculateFactorial(5)
print(result)
    