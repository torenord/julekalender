#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Luke 5

# Et anagram er et ord som kan skrives om til et annet ord ved å
# omrokere bokstavene. Hvor mange av ordene totalt i ordlista
# http://pastebin.com/sGbqMyCa er anagrammer av andre ord i lista?
# Merk at vi kun er ute etter ord i lista, ikke ord som er sammensatt
# av flere ord.

# Eksempel input: acre, care, race, agnes, senga, eple
# Eksempel output: 5 (dvs alle unntatt eple er et anagram av et annet ord i lista)

from sys import stdin
from collections import Counter

print sum(i for i in Counter(map(lambda l: "".join(sorted(l.strip())), stdin)).values() if i > 1)
