def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    s1 = []
    t1 = []
    for i in apples:
        s1.append(a+i)
    for j in oranges:
        t1.append(b+j)
        
    c =0
    d=0
    for i in s1:
        if i>=s and i<=t:
            c+=1
    for j in t1:
        if j>=s and j<=t:
            d+=1
    print(c)
    print(d)
