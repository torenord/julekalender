from sys import stdin
from re import match

print sum(1 for line in stdin.readlines() if match("^[a-z]{,3}[0-9]{2,8}[A-Z]{3,}\n$", line))
