def circularArrayRotation(a, k, queries):
    # Write your code here
    res = []
    k = k % n
    for i in queries:
        res.append(a[(n-k +i) % n])
    return res
