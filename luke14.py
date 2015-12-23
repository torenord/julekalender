#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Luke 14

# I denne oppgaven skal vi forsøke å finne tall som kan leses likt når
# de blir rotert 180° (med andre ord; opp ned). Sifrene vi kan tolke
# opp ned er 0, 1, 6, 8 og 9 og noen eksempler på tall som blir like
# opp ned er: 181, 916 og 8008.

# Din oppgave er å finne antall heltall, fra og med 0 til og med 100
# 000, som kan leses likt opp ned.

def M(d):
    if d == '0': return '0'
    if d == '1': return '1'
    if d == '6': return '9'
    if d == '8': return '8'
    if d == '9': return '6'
    else:        return ''

print sum(str(i)[::-1] == "".join(map(M, str(i))) for i in range(0, 100000+1))
