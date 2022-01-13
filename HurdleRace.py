def hurdleRace(k, height):
    # Write your code here
    if k >= max(height):
        return 0
    else:
        return max(height) - k
