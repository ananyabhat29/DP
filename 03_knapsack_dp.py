#KnapScak Problem using BottomUp Approach

def knapsack(wt, val, bag, n, t):
    
    
    for i in range(0,n+1):
        for j in range(0,bag+1):
            
            if i==0 or j ==0:
                t[i][j] = 0
            else:
            
                if wt[i-1] > j:
                    t[i][j]  = t[i-1][j]
                   
                
                else:
                    t[i][j] =  max(val[i-1] + t[i-1][j-wt[i-1]], t[i-1][j])
    print(t)
    return t[n][bag]
                    
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

t = [[-1 for i in range(capacity+1)] for j in range(len(weights)+1)]
max_value = knapsack(weights, values, capacity, len(weights), t)
print(max_value)