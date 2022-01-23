def jumpingOnClouds(c, k):
    i = 0
    e = 100
    while True:
        i = (i+k)%n
        if c[i] == 1:
            e = e - 3
        else:
            e = e - 1
        if i == 0:
            break
    return e
            
