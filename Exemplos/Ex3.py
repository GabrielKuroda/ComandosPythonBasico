# -*- coding: utf-8 -*-

from math import sqrt

print("ax2 + bx + c")

a = int(input("Digite o Valor a:\n"))

b = int(input("Digite o Valor b:\n"))

c = int(input("Digite o Valor c:\n"))

try:
	delta = b**2 -4*a*c
	raiza_delta = sqrt(delta)
except:
	print("Não é possivel fazer raiz negativa ou zero!")

x1 = (-b + raiza_delta)/(2*a)
x2 = (-b - raiza_delta)/(2*a)

print("x1 = ",round(x1,1))
print("x2 = ",round(x2,1))
