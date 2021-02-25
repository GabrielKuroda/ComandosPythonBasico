# -*- coding: utf-8 -*-

numero1 = int(input("Digite o 1ºnúmero:\n"))

sinal = input("Digite o sinal:\n")

numero2 = int(input("Digite o 2ºnúmero:\n"))

if sinal == "+":

	resultado = numero1 + numero2
	print(resultado)

elif sinal == "-":

	resultado = numero1 - numero2
	print(resultado)

elif sinal == "*":

	resultado = numero1 * numero2
	print("\n"+resultado)

elif sinal == "/":

	resultado = numero1 / numero2
	print(resultado)

else:

	print("Sinal invalido!")

