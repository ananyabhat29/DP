#Count of subsets with a given sum
#Given an array arr[] of length N and an integer X, the task is to find the number of subsets with sum equal to X.
#Example:
#Input: arr[] = {1, 2, 3, 3}, X = 6
#Output: 3
#All the possible subsets are {1, 2, 3},{1, 2, 3} and {3, 3}


def countOfSubsets(arr, x, n):
    
    t = [[0 for i in range(x+1)] for j in range(n+1)]
    
    for i in range(n+1):
        for j in range(x+1):
            
            if i == 0:
                t[i][j] = 0
            if j == 0:
                t[i][j] = 1
            
            else:
                if arr[i-1] > j:
                    t[i][j] = t[i-1][j]
                
                else:
                    t[i][j] = t[i-1][j] + t[i-1][j -arr[i-1]]
                    
    return t[n][x]
arr = [2, 3 ,5, 6, 8, 10,4]
x = 10
print(countOfSubsets(arr, x, len(arr)))