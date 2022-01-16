def permutationEquation(p):
    # Write your code here
    res = []
    for x in range(1,n+1):
        for y in range(n):
            if p[p[y]-1] == x:
              res.append(y+1)  
        
    return res
