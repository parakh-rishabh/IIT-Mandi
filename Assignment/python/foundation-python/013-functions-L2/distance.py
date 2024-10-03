# # d=√((x2 – x1)² + (y2 – y1)²)
# Distance Between Two Points

# Write a function named distance that takes the x and y coordinates of two points and returns the distance between them.

# Sample Input: (2, 3), (5, 7);

# Sample Output: 5.0
import math
def distance(p1,p2):
    x1=p1[0]
    x2=p2[0]
    y1=p1[1]
    y2=p2[1]
    d=((x2-x1)**2 + (y2-y1)**2)**0.5
    # d=math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return d
result=distance([2,3],[5,7])
print(result)
    
    