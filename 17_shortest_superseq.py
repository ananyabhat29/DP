#Shortest Super Sequence
#supersequence should contain the subsequences of both the strings
#return the length of the shortest super sequence

def lcs(a, b, m, n, dp):
    
    for i in range(m+1):
        for j in range(n+1):
            
            if i == 0 or j ==0 :
               dp[i][j] = 0
            
            else:
                if a[i-1] == b[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
                    
    return dp[m][n]

a = 'AGGTAB'
b = 'GXTXAYB'
m = len(a)
n = len(b)
t = [[-1 for i in range(n+1)]for j in range(m+1)]
ans = lcs(a, b, m, n, t)

print("Length of SCS:",len(a) + len(b) - ans)
#AGGXTXAYB
