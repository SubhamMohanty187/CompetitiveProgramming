def breakingRecords(scores):
    # Write your code here
    h = scores[0]
    l = scores[0]
    h1 = 0
    l1 = 0
    for i in scores:
        if i > h:
            h = i
            h1 += 1
        elif i < l:
            l = i
            l1 += 1
    res = [h1,l1]
    return res
