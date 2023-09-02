#Equal Sum Partition Problem
#Partition problem is to determine whether a given set can be partitioned into two subsets such that the sum of elements in both subsets #is same.
#Examples:
#arr[] = {1, 5, 11, 5}
#Output: true 
#The array can be partitioned as {1, 5, 5} and {11}

def subsetSum(arr, x):
    
    t = [[False for i in range(x+1)] for j in range(len(arr)+1)]
    
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


ans = subsetSum(arr, x)
print(ans)


def equalPartition(arr, n):
    
    s = sum(arr)
    
    if s%2 !=0:
        return False
    else:
        return subsetSum(arr, s//2)
    
arr = [1,5,11,5]
print(equalPartition(arr, len(arr)))
    