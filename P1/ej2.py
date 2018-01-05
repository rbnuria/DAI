#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, random, time
from random import randint
from time import time
import selection
import burbuja


size = 200

## Creación de la matriz
M1 = []

for i in range(size):
	M1.append(random.randint(1,20))

M2 = M1

t_inicial_1 = time()
selection.sort(M1)
t_final_1 = time()

t_selection = t_final_1 - t_inicial_1

t_inicial_2 = time()
burbuja.sort(M2)
t_final_2 = time()

t_burbuja = t_final_2 - t_inicial_2

print "El tiempo de ejecucion del algoritmo de la burbuja es", t_burbuja
print "El tiempo de ejecucion del algoritmo de seleccion es", t_selection
