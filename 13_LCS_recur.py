#longest Common Subsequence using Recursion

def longestCommonSubstring(a, b, n, m):
    
    
    if n == 0 or m == 0:
        return 0
    
    if a[n-1] == b[m-1]:
        return 1 + longestCommonSubstring(a, b, n-1, m-1)
    else:
        return max(longestCommonSubstring(a, b, n-1, m), longestCommonSubstring(a, b, n, m-1))

a = 'aeg'
b = 'acefg'

print(longestCommonSubstring(a, b, len(a), len(b)))