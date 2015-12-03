from sys import stdin

prices = map(float, stdin)
low, diff = prices[0], 0
for p in prices[1:]:
    low, diff = min(p, low), max(p - low, diff)

print('{0:.4f}'.format(diff))
