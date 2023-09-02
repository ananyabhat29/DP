#Unbounded KnapSack
#minimum number of coins needed to get sum
#Leetcode : https://leetcode.com/problems/coin-change/?envType=study-plan-v2&envId=top-interview-150

def coinchange2(coins,s,n, t):
    
    #Initialization
    for j in range(s+1):
        t[0][j] = 999
    for i in range(n+1):
        t[i][0] = 0
        
    for i in range(1, n+1):
        for j in range(1, s+1):
            
            if coins[i-1] > j:
                t[i][j] = t[i-1][j]
            
            else:
                t[i][j] = min(1 + t[i][j - coins[i-1]], t[i-1][j])
    return t[n][s]

coins = [25, 10, 5]
s = 30
n = len(coins)
t = [[0 for i in range(s+1)]for j in range(n+1)]

print(coinchange2(coins, s, n, t))
            
            
