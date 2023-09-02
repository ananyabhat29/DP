#Subset sum
#Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.
#Example:
#Input:  set[] = {3, 34, 4, 12, 5, 2}, sum = 9
#Output:  True  //There is a subset (4, 5) with sum 9.

#arr is equivalent to weights
#x is equivalent to bag capacity

def subsetSum(arr, x, t):
    
    for i in range(len(arr)+1):
        for j in range(x+1):
            
            if i == 0:
                t[i][j] = False
            if j==0:
                t[i][j] = True
            
            else:
                
                if arr[i-1] > j:
                    t[i][j] = t[i-1][j]
                
                else:
                    t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
    return t[len(arr)][x]
    
arr = [2, 3, 7, 8, 9]
x =11

t = [[False for i in range(x+1)] for j in range(len(arr)+1)]
ans = subsetSum(arr, x, t)
print(ans)