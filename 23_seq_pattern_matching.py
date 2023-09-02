#Sequence Pattern Matching
#Return True if A is a seq of B
#if LCS(A, B) = A, then True

def lcs(a, b, m, n, dp):
    
    for i in range(m+1):
        for j in range(n+1):
            
            if i == 0 or j ==0 :
               dp[i][j] = 0
            
            else:
                if a[i-1] == b[j-1] and i!=j:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
           
    return dp

def printLCS(a, b, m, n, dp):
    
    i = m
    j = n
    res = ""
    
    while i > 0 and j>0:
        
        if a[i-1] == b[j-1]:
            res+=a[i-1]
            i-=1
            j-=1
        
        else:
            if dp[i-1][j] > dp[i][j-1]:
                i-=1
            else:
                j-=1
    return res[::-1]

 
a = 'AXY'
b = 'ADXCPY'
m = len(a)
n = len(b)
t = [[-1 for i in range(n+1)]for j in range(m+1)]
dp= lcs(a, b, m, n, t)

ans = printLCS(a, b, m, n, dp)
print(ans)
print(ans == a)
#TRUE (AXY IS A SUBSEQ IN ADXCPY)
