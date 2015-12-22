#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Luke 19

# Et barn løper opp en trapp med 30 trinn, og kan ta enten ett, to
# eller tre steg omgangen. Hvor mange ulike måter kan barnet løpe opp
# trappen?

m = {}

def f(n):
    if n in m: return m[n]

    if n == 1: return 1
    if n == 2: return 2
    if n == 3: return 4

    m[n] = f(n-1) + f(n-2) + f(n-3)

    return m[n]

print f(30)
