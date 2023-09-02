#Count number of subsets with the difference of their sum equal to the given diff
#Given an array Arr[] and a difference diff, find the number of subsets that array can be divided so that each the difference between the two subset is the given diff.

#Example1:
#Input: Arr[] : 1,1,2,3
#diff: 1
#Output: 3 .


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

def countOfSubsetsWithGivenDiff(arr, diff):
    
    s1 = abs((diff - sum(arr))//2)
    #print(s1)
    
    return countOfSubsets(arr, s1, len(arr))
    
arr = [1,1,2,3]
diff = 1
print(countOfSubsetsWithGivenDiff(arr, diff))