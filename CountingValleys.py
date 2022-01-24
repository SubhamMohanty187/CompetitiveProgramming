def countingValleys(steps, path):
    level = 0         # sea-level
    valley = 0
    for i in path:
        if i == "U":
            level += 1
            if level == 0:   # Since we count a valley only after
                valley += 1  # we come out of D
        else:
            level -= 1
    
    return valley
