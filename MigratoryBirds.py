def migratoryBirds(arr):
    # Write your code here
    count = [0] * len(arr)   #creattes a list of 0 whose length is same as the length of arr
    for i in arr:
        count[i] += 1
        
    return count.index(max(count)
