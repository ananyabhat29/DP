# min Subset Sum Diff
#Given a set of integers, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum.
#If there is a set S with n elements, then if we assume Subset1 has m elements, Subset2 must have n-m elements and the value of abs(sum(Subset1) – sum(Subset2)) should be minimum.

#Example:
#Input:  arr[] = {1, 6, 11, 5} 
#Output: 1
#Explanation:
#Subset1 = {1, 5, 6}, sum of Subset1 = 12 
#Subset2 = {11}, sum of Subset2 = 11 



def subsetSum1(arr, r):
    
    t = [[False for i in range(r+1)] for j in range(len(arr)+1)]
    
    for i in range(len(arr)+1):
        for j in range(r+1):
            
            if i == 0:
                t[i][j] = False
            if j==0:
                t[i][j] = True
            
            else:
                
                if arr[i-1] > j:
                    t[i][j] = t[i-1][j]
                
                else:
                    t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
                    
    #get vector V
    v_boolean = t[len(arr)]
    v = [i for i in range(len(v_boolean)//2) if v_boolean[i] == True]
    return v
    
def minSubsetSumDiff(arr, n):
    
    r = sum(arr) #range
    v  = subsetSum1(arr, r)
    
    min_diff = float('inf')
    
    for s1 in v:
        min_diff = min(min_diff, r - (2*s1))
    return min_diff
    
    
arr = [1,2,7]
print(minSubsetSumDiff(arr, len(arr)))
    
    