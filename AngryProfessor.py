def angryProfessor(k, a):
    # Write
    n = 0
    p = 0
    for i in a:
        if i <= 0:
            p += 1
        else:
            n += 1
    if p >= k:
        return "NO"   # Classes will NOT be cancelled
    else:
        return "YES"  # Classes will be cancelled
