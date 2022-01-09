def compute_gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm
    
        
def getTotalX(a, b):
    # Write your code here
    lcm = a[0]
    gcd = b[0]
    
    for i in a:
        lcm = compute_lcm(lcm,i)
        
    for i in b:
        gcd = compute_gcd(gcd,i)
    
    r = 0
    res = 0
    while r <= gcd:
        r += lcm
        if gcd % r == 0:
            res += 1
    return res        
