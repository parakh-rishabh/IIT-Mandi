# List Multiples of a Number

# Write a function named listMultiples that takes two numbers n and limit. The function should print the first n multiples of limit.

# E.g., listMultiples(3, 5) should print 3, 6, 9, 12, 15

def listMultiple(n,limit):
    for i in range(1,limit+1):
        print(i*n,end=" ")
    print()    
listMultiple(3,5)        