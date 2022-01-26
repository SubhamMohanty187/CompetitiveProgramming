def repeatedString(s, n):
    # Write your code here
    q = n // len(s)
    x = s.count("a")
    x1 = q * x
    x2 = s[: n % len(s)].count("a")
    return x1+x2
