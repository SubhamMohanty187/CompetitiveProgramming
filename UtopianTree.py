def utopianTree(n):
    # Write your code here
    count = 0
    for i in range(n+1):
        if i % 2 == 0:
            count += 1
        else:
            count = count * 2
    return count
