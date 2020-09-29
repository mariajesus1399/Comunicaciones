#!/usr/bin/env python3.7
import sys
import os
import numpy as np

#Recibe los simbolos y los ordena para obtener los niveles
a_simbolos = []
try:
	simbolos_file=open("simbolos.txt",'r') # archivo con k bits
	simbolos= simbolos_file.readlines()
	simbolos_file.close()
	for simbolo in simbolos:
		if simbolo[-1]=="\n":
			x = int(simbolo[:-1].split(", ")[0])
			a_simbolos.append(x)
		else:
			x = int(simbolo.split(", ")[0])
			a_simbolos.append(int(x))
except(FileNotFoundError):
	advert = "File not found"
	print(advert)

a_muestras = []
try:
	muestras_file=open("salida_modulador.txt",'r') 
	muestras= muestras_file.readlines()
	muestras_file.close()
	for muestra in muestras:
		if muestra[-1]=="\n":
			x = int(muestra[:-1].split(", ")[0])
			a_muestras.append(x)
		else:
			x = int(muestra.split(", ")[0])
			a_muestras.append(int(x))
except(FileNotFoundError):
	advert = "File not found"
	print(advert)

a_simbolos = list(dict.fromkeys(a_simbolos)) #Eliminar elementos repetidos
levels = sorted(a_simbolos, key=int) #ordenar de menor a mayor
sample = 50
len_muestras = len(a_muestras)
count = 0
out_demodulador = open("salida_demodulador.txt", "w")
while count*sample < len_muestras:
	muestra = a_muestras[count*sample]
	absolute_difference_function = lambda list_value : abs(list_value - muestra)
	closest_value = min(a_simbolos, key=absolute_difference_function)
	binary = int(bin(closest_value)[2:])
	out_demodulador.write(str(binary).zfill(7))
	out_demodulador.write("\n")
	count += 1
out_demodulador.close()

	


