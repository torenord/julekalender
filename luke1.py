#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Luke 1

# Hver innbygger i Ruritania har en unik ID. IDen er en streng bygd
# opp etter følgende regler:

# * Id strengen må begynne med 0-3 små bokstaver (fra a-z).
# * Rett etter bokstavene må det følge 2-8 tall. Tallene har verdi fra
#   og med 0 til og med 9
# * Rett etter tallene må det følge en streng med minst 3 store
#   bokstaver (fra A-Z)

# Eksempler:
# nbm675626906YGX -> Ugyldig
# nbm67562690YGX -> Gyldig
# nbM675626YGX -> Ugyldig
# 67YGX -> Gyldig
# 675626YG -> Ugyldig

# Hver linje i filen http://pastebin.com/F8z0JWqa inneholder en slik
# ID streng. Oppgaven er å finne hvor mange av disse som er gyldige i
# henhold til reglene over. Hadde eksemplene over vært oppgaven, ville
# svaret vært 2. Lykke til :)

from sys import stdin
from re import match

pattern = "[a-z]{,3}[0-9]{2,8}[A-Z]{3,}"

print sum(1 for line in stdin if match(pattern, line))
