def squares(a, b):
    # Write your code here
    count = 0
    
    na = int(a**0.5)
    nb = int(b**0.5)
    
    count = nb - na
    
    if na**2 == a:
        count += 1
            
    return count
