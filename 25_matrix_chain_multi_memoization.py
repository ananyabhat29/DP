#MATRIX CHAIN MULTIPLICATION (Memoization)
#Given a sequence of matrices, find the most efficient way to multiply these matrices together.
#The problem is not actually to  perform the multiplications, but merely to decide in which order to perform the multiplications. 

def MCM(arr, i, j, t):
    
    if i >= j:
        return 0
    
    if t[i][j]!=-1:
        return t[i][j]
        
    t[i][j] = float("inf")
    
    #for(k=i; k<= j-1; k++)
    for k in range(i, j-1+1):
        t[i][j] = min(t[i][j], MCM(arr, i, k, t) + MCM(arr, k+1, j, t) + (arr[i-1]*arr[k]*arr[j]))
        
        
    return t[i][j]
    
arr = [1, 2, 3, 4, 3]
N = len(arr)
t = [[-1 for i in range(101)]for j in range(101)]
#i = 1, j=n-1
ans = MCM(arr, 1, N-1, t)
print(ans)

#30
#1*2*3 + 1*3*4 + 1*4*3 = 30

