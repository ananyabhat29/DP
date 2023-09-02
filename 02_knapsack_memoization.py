#KnapScak Problem using Memoization

def knapsack(wt, val, bag, n, t):
    
    if n ==0 or bag ==0:
        return 0
    
    if t[n][bag] != -1:
        return t[n][bag]
    
    
    if wt[n-1] > bag:
        t[n-1][bag]  = knapsack(wt, val, bag, n-1,t)
        return t[n][bag]
    
    else:
        t[n][bag] =  max(val[n-1] + knapsack(wt, val, bag-wt[n-1], n-1, t), knapsack(wt, val, bag, n-1, t))
        return t[n][bag]

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

t = [[-1 for i in range(capacity+1)] for j in range(len(weights)+1)]
max_value = knapsack(weights, values, capacity, len(weights), t)
print(max_value)