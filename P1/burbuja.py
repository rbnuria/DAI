#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

#ALGORITMO DE SELECTION SORT:

def swap(v, pos1, pos2):
	aux = v[pos1]
	v[pos1] = v[pos2]
	v[pos2] = aux

def sort(v):
	n = len(v)

	for i in range(2, n):
		for j in range(0, n-i):
			if v[j] > v[j+1]:
				swap(v, j, j+1)

