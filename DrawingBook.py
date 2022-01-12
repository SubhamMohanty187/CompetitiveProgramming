def pageCount(n, p):
    # We divide by 2 because we are flipping 2 pages per flip.
    return min(p//2, n//2 - p//2)
