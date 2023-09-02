#MATRIX CHAIN MULTIPLICATION (Recursive)
#Given a sequence of matrices, find the most efficient way to multiply these matrices together.
#The problem is not actually to  perform the multiplications, but merely to decide in which order to perform the multiplications. 

def MCM(arr, i, j):
    
    if i >= j:
        return 0
    
    min_cost = float("inf")
    #for(k=i; k<= j-1; k++)
    for k in range(i, j-1+1):
        temp = MCM(arr, i, k) + MCM(arr, k+1, j) + (arr[i-1]*arr[k]*arr[j])
        
        if temp < min_cost:
            min_cost = temp
    return min_cost
    
arr = [1, 2, 3, 4, 3]
N = len(arr)

#i = 1, j=n-1
ans = MCM(arr, 1, N-1)
print(ans)

#30
#1*2*3 + 1*3*4 + 1*4*3 = 30

