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

	for i in range(0, n-1):
		minimo = i
		for j in range(i+1, n):
			if v[j] < v[minimo]:
				minimo = j

		swap(v,i,minimo)