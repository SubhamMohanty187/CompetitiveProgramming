def beautifulDays(i, j, k):
    # Write your code here
    count = 0
    res = 0
    for day in range(i, j+1):
        r = str(day)
        rev = r[::-1]
        rev = int(rev)
        res = int(abs(day - rev))
        if res % k == 0:
            count += 1
    return count
