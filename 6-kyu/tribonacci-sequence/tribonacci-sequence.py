def tribonacci(signature, n):
    if n <= 0: return []
    r = signature[:n]
    while len(r) < n:
        r.append(sum(r[-3:]))
    return r