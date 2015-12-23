#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Luke 7

# Finn summen av alle positive heltall mellom 0 og 1000 som er har 7
# som en primtallsfaktor, der det reverserte tallet også har 7 som en
# primtallsfaktor.

# For eksempel teller 259 da en får 952 om en reverserer sifrene og
# begge disse tallene har 7 som en primtallsfaktor.

print sum(i for i in range(0, 1000+1) if i % 7 == int(str(i)[::-1]) % 7 == 0)
