def xo(s):
    return sum((c == 'x') - (c == 'o') for c in s.lower()) == 0