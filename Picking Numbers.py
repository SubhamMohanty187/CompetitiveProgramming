def pickingNumbers(a):
    # Write your code here
    a.sort()
    res = 0
    for i in range(len(a)):
        for j in range(1,len(a)):
            if abs(a[i] - a[j])<=1:
                res = max(res, j-i + 1)
    return res
