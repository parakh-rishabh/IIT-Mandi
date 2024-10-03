# Greatest Common Divisor (GCD)

# Write a function named findGCD that takes two integers as input and returns their greatest common divisor (GCD). Use this function to find the GCD of two given numbers.

# gcdResult = findGCD(36, 48);

# // Sample Output: gcdResult = 12

# Submission
import math
def findGCD (x,y):
    GCD=math.gcd(x,y)
    return GCD
result=findGCD(36,48)
print(result)