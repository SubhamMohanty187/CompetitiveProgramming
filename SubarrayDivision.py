def birthday(s, d, m):
    # Write your code here
    res = 0
    for i in range(len(s)+1 - m):
        if sum(s[i : i+m]) == d:
            res += 1
            
    return res 
