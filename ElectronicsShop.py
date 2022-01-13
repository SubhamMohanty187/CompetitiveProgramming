def getMoneySpent(keyboards, drives, b):
    # Write your code here.
    keyboards.sort(reverse=True)
    drives.sort(reverse=True)
    s = -1
    for i in keyboards:
        for j in drives:
            if i > b or j > b:
                continue
            if i + j <= b:
                s = max(s,i+j)
                
    return s
