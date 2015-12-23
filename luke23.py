#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Luke 23

# Vi har en liste som inneholder n trær, der hvert tre har en lengde
# som er et positivt heltall. Vi definerer en kuttoperasjon som
# utføres på hvert tre i lista. Denne operasjonen reduserer lengden på
# alle trærne i lista med lengden av det korteste treet, og trær med
# lengde 0 fjernes fra lista.
# Gitt følgende liste: [5 4 4 2 2 8]
# Etter vi har utført en kuttoperasjon står vi igjen med: [3 2 2 6]
# Kuttoperasjonen blir gjentatt til det ikke er flere trær igjen.

# Oppgaven er å finne antall trær som blir kuttet i hver operasjon
# inntil det ikke er flere trær igjen.
# For eksempel så vil svaret for [5, 4, 4, 2, 2, 8] en være en
# kommaseparert liste av tall:

# 6,4,2,1
# Der 6 er antall trær som blir kuttet i første operasjon, 4 i andre
# operasjon, osv.

# Finn svaret for følgende liste:
# [23, 74, 26, 23, 92, 92, 44, 13, 34, 23, 69, 4, 19, 94, 94, 38, 14,
# 9, 51, 98, 72, 46, 17, 25, 21, 87, 99, 50, 59, 53, 82, 24, 93, 16,
# 88, 52, 14, 38, 27, 7, 18, 81, 13, 75, 80, 11, 29, 39, 37, 78, 55,
# 17, 78, 12, 77, 84, 63, 29, 68, 32, 17, 55, 31, 30, 3, 17, 99, 6,
# 45, 81, 75, 31, 50, 93, 66, 98, 94, 59, 68, 30, 98, 57, 83, 75, 68,
# 85, 98, 76, 91, 23, 53, 42, 72, 77]

# Svar oppgis som en kommaseparert liste.

def solve(t):
    l = len(t)
    res = []

    for c in [t.count(n) for n in sorted(set(t))]:
        res.append(l)
        l -= c

    return ",".join(map(str, res))

t = [23, 74, 26, 23, 92, 92, 44, 13, 34, 23, 69, 4, 19, 94, 94, 38,
     14, 9, 51, 98, 72, 46, 17, 25, 21, 87, 99, 50, 59, 53, 82, 24,
     93, 16, 88, 52, 14, 38, 27, 7, 18, 81, 13, 75, 80, 11, 29, 39,
     37, 78, 55, 17, 78, 12, 77, 84, 63, 29, 68, 32, 17, 55, 31, 30,
     3, 17, 99, 6, 45, 81, 75, 31, 50, 93, 66, 98, 94, 59, 68, 30, 98,
     57, 83, 75, 68, 85, 98, 76, 91, 23, 53, 42, 72, 77]

print solve(t)
