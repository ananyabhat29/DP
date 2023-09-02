#Unbounded KnapSack
#max number of ways to get sum
#Leetcode : https://leetcode.com/problems/coin-change-ii/submissions/?envType=study-plan-v2&envId=top-interview-150

def coinchange1(coins, s, n, t):
    
    #Initialization
    for j in range(s+1):
        t[0][j] = 0
    for i in range(n+1):
        t[i][0] = 1
        
    for i in range(1,n+1):
        for j in range(1,s+1):
           
          
        
            if coins[i-1] > j:
                t[i][j]  = t[i-1][j]
               
            
            else:
                t[i][j] = t[i-1][j] + t[i][j-coins[i-1]]
                
    print(t)
    return t[n][s]
                    
coins = [1, 2, 3]

s = 4

t = [[0 for i in range(s+1)] for j in range(len(coins)+1)]
print(t)
max_value = coinchange1(coins, s, len(coins), t)
print(max_value)