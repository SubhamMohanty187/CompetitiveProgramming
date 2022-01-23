def findDigits(n):
    # Write your code here
    count = 0
    num = n
    while n > 0:
        rem = n % 10
        n = n // 10
        if rem == 0:
            continue
        if num % rem == 0:
            count += 1
    return count
