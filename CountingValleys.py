def countingValleys(steps, path):
    level = 0         # sea-level
    valley = 0
    for i in path:
        if i == "U":
            level += 1
            if level == 0:   # Since we count a valley only after we come out of D
                valley += 1  
        else:
            level -= 1
    
    return valley
