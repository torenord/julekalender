#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Luke 8

# Vi definerer et primtall som et MIRPTALL dersom vi fortsatt har er
# primtall når sifrene reverseres. Regelen gjelder imidlertid ikke
# dersom tallet samtidig er et palindrom (dvs likt samme hvilken ende
# det leses fra, som 969).

# Eksempel 1: 13 er et primtall. Det er også et MIRPTALL, fordi tallet
# i revers, 31, også er et primtall.

# Eksempel 2: 23 er et primtall. Det er imidlertid ikke et MIRPTALL,
# da vi får 32 om vi reverserer det, som ikke er et primtall.

# Eksempel 3: 5 og 101 er ikke MIRPTALL, selv om de er primtall, da
# disse er palindromer.

# Hvor mange positive heltall under 1000 er MIRPTALL?

# Tips: Selv om 13 og 31 reverseres til hverandre er de fortsatt
# MIRPTALL “hver for seg” (på grunn av definisjonen). Begge må derfor
# telles med som en del av resultatet.

def prime(n):
    return all(n % i != 0 for i in range(2, int(n**0.5)+1))

def reverse(n):
    return int(str(n)[::-1])

def palindrome(n):
    return n == reverse(n)

print sum(prime(i) and prime(reverse(i)) and not palindrome(i) for i in range(1, 1000))
