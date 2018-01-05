#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, math
from math import sqrt

## Definimos un método

def criba_erastotenes(tam):
	prime = [False, False]

	for i in range(2, tam+1):
		prime.append(True)


	for i in range(2, int(sqrt(tam))+1):
		if(prime[i]):
			for h in range(2, int(tam/i)+1):
				prime[i*h] = False


	return prime

primos = criba_erastotenes(1000)

for i in range(0, 1000):
	if primos[i]:
		print i , "\n"


