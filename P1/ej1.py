#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, random
from random import randint


n = random.randint(1,100)
num = int(input("Adivina el numero que estoy pensando (entre 1 y 100)"))


count = 1

while (n != num and count < 10):
	if n < num:
		num = int(input("El numero que estoy pensando es menor"))
	elif n > num:
		num = int(input("El numero que estoy pensando es mayor"))


if n == num:
	print("Has adivinado el número")
else:
	print("No has adivinado el número")
