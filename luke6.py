#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Luke 6

# Gitt at vi har n par parenteser, hvor mange kombinasjoner av
# balanserte parenteser (dvs alle åpne parenteser er lukket) kan en
# lage?

# Eksempel:
# Gitt n=3, har vi følgende kombinasjoner som gir balanserte parenteser:
# "((()))", "(()())", "(())()", "()(())", "()()()"
# Altså fem ulike måter.

# Hvor mange velformede kombinasjoner finnes det for n = 13?

def f(l, r):
    if l == 0 or r == 0:
        return 1
    if l == r:
        return f(l-1, r)
    if l < r:
        return f(l-1, r) + f(l, r-1)

print f(13, 13)
