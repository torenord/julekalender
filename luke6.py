def f(l, r):
    if l == 0 or r == 0:
        return 1
    if l == r:
        return f(l-1, r)
    if l < r:
        return f(l-1, r) + f(l, r-1)

print f(13, 13)
