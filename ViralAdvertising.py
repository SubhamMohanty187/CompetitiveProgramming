def viralAdvertising(n):
    # Write your code here
    liked = 2   # 1st day floor(5/2) = 2 will like the ad.
    tmp = 2     # temporary value for like
    for i in range(1,n):
        recieved = tmp * 3
        tmp = math.floor(recieved / 2)
        liked += tmp
        
    return liked
