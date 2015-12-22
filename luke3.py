#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Luke 3

# Programmererenes dag feires hvert år på den 256. dagen (eller
# 2^8. dagen om du vil) i året. Hvor mange ganger fra og med år 1 til
# og med år 2015 har dette forekommet på en fredag om en antar at
# 1. januar år 1 var en fredag i, samt at dagens skuddårsregler og
# kalendersystem har vært gjeldende i hele perioden?

# Hint: Skuddår er forøvrig et år som er delelig på 4 og ikke 100 med
# mindre det er delelig på 400

# OBS: Er blitt gjort oppmerksom på et avvik i oppgaven. Svaret som er
# lagt inn på oppgaven later til å anta at den første dagen i året er
# den "nulte" dagen i året.

from datetime import date, timedelta

friday = date(1, 1, 1).weekday()
print sum((date(y, 1, 1) + timedelta(256)).weekday() == friday for y in range(1, 2015+1))
