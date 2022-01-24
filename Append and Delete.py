def appendAndDelete(s, t, k):
    # Write your code here
    prefix = 0
    for c1, c2 in zip(s, t):
        if c1 == c2:
            prefix += 1
        else:
            break
    if k >= len(s) + len(t):
        return "Yes"
    elif k >= len(s) + len(t) - 2 * prefix and k % 2 == (len(s) + len(t)) % 2:
        return "Yes"
    else:
        return "No"
