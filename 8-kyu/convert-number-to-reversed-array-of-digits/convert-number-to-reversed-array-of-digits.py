def digitize(n):
    result = []
    while n > 0:
        result.append(n % 10)
        n //= 10
    return result if len(result) > 1 else [0]