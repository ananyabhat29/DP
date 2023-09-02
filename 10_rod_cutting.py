#Rod Cutting
#Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n. Determine the  maximum value obtainable by cutting up the rod and selling the pieces. 
#Example: 
#if length of the rod is 8 and the values of different pieces are given as following, then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6)

#Same as Unbounded KnapSack
#wt = lengths
#val = prices
#bag capacity = length of rod

def rodCutting(lengths, prices, rod, n, t):
    
    
    for i in range(0,n+1):
        for j in range(0,rod+1):
            
            if i==0 or j ==0:
                t[i][j] = 0
            else:
            
                if lengths[i-1] > j:
                    t[i][j]  = t[i-1][j]
                   
                
                else:
                    t[i][j] =  max(prices[i-1] + t[i][j-lengths[i-1]], t[i-1][j])
    
    return t[n][rod]
                    
lengths = [1, 2, 3, 4, 5, 6, 7, 8]
prices = [1, 5, 8, 9, 10, 17, 17, 20]
rod = 8

t = [[-1 for i in range(rod+1)] for j in range(len(lengths)+1)]
max_value = rodCutting(lengths, prices, rod, len(lengths), t)
print(max_value)
    