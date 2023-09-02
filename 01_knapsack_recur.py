#KnapScak Problem using Recursion

def knapsack(wt, val, bag, n):
    
    if n ==0 or bag ==0:
        return 0
    
    if wt[n-1] > bag:
        return knapsack(wt, val, bag, n-1)
    
    else:
        return max(val[n-1] + knapsack(wt, val, bag-wt[n-1], n-1), knapsack(wt, val, bag, n-1))

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

max_value = knapsack(weights, values, capacity, len(weights))
print(max_value)