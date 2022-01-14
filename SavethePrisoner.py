def saveThePrisoner(n, m, s):
    # Write your code here
    sm = m-1 + s
    val = sm % n
    if val == 0:
        val = n
    return val
