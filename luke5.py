from sys import stdin
from collections import Counter

print sum(i for i in Counter(map(lambda l: "".join(sorted(l.strip())), stdin)).values() if i > 1)
