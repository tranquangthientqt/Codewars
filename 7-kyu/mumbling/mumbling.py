def accum(st):
    return '-'.join((i * st[i - 1]).title() for i in range(1, len(st) + 1))