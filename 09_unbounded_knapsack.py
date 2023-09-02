#Unbounded KnapSack
#This is different from classical Knapsack problem, here we are allowed to use unlimited number  of instances of an item.
#Examples:

#Input : W = 100
 #      val[]  = {1, 30}
 #     wt[] = {1, 50}
#Output : 100


def knapsack(wt, val, bag, n, t):
    
    
    for i in range(0,n+1):
        for j in range(0,bag+1):
            
            if i==0 or j ==0:
                t[i][j] = 0
            else:
            
                if wt[i-1] > j:
                    t[i][j]  = t[i-1][j]
                   
                
                else:
                    t[i][j] =  max(val[i-1] + t[i][j-wt[i-1]], t[i-1][j])
    print(t)
    return t[n][bag]
                    
weights = [1, 3, 4, 5]
values = [10, 40, 50, 70]
capacity = 8

t = [[-1 for i in range(capacity+1)] for j in range(len(weights)+1)]
max_value = knapsack(weights, values, capacity, len(weights), t)
print(max_value)
    