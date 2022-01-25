def cutTheSticks(arr):
    # Write your code here
    arr.sort()
    res = []
    count = 0
    i = 0
    while i < len(arr):
        res.append(len(arr) - i)
        count = arr[i]
        while i < len(arr) and arr[i] <= count:
            i += 1
            
    return res
