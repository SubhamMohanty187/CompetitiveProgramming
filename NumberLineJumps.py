def kangaroo(x1, v1, x2, v2):
    # Write your code here
    #Since x1<x2 (always acc. to constraints) so if v1 is not      greater than v2 then they will not meet. (v1>v2)
    # let both meet after "y" jumps. so, x1 + v1*y = x2 + v2*y if we solve this then, (x2-x1)/(v1-v2) for some y.
    
    if v1 > v2 and (x2-x1)%(v1-v2) == 0:
        return "YES"
    else:
        return "NO"
