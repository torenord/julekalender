#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Luke 2

# Lenken http://pastebin.com/sJVZp7BH inneholder en liste av tall. Den
# første linja inneholder prisen på en aksje på dag 1, den andre linja
# inneholder prisen på den samme aksjen på dag 2 og så videre.

# Gitt at du kun har lov til å gjøre én transaksjon, hva er den
# høyeste fortjenesten du kan oppnå gitt de vedlagte aksjeprisene?

# En transaksjon betyr at du kjøper en aksje før du, én eller flere
# dager senere, selger den igjen.

# Svar skal oppgis med fire desimaler. Bruk punktum som
# desimalskilletegn. Eksempel: 12.2446

from sys import stdin

prices = map(float, stdin)
low, diff = prices[0], 0
for p in prices[1:]:
    low, diff = min(p, low), max(p - low, diff)

print('{0:.4f}'.format(diff))
