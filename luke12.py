#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Luke 12

# Finn summen av alle tall fra og med 1 og til og med 100 000 000 som
# er har 7 som en divisor, og samtidig IKKE har 5 som en divisor.

print sum(i for i in range(7, 100000000+1, 7) if i % 5 != 0)
