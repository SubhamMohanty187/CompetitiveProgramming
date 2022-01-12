from collections import Counter
def sockMerchant(n, ar):
    # Write your code here
    s = 0
    for i in Counter(ar).values():
        s += i//2
    return s 
