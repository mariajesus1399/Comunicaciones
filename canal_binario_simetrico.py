#!/usr/bin/env python3.7
import sys
import os
import numpy as np
import random


# texto_codificado.txt contiene los bits de entrada
bkR0 = open("salida_codificador_canal.txt", "r")

#Se introduce un error cada 4 bits 
p_e = 2/7

# texto_con_errores corresponde a la salida del canal simétrico
output_file = open("texto_con_errores.txt", "w")

for line in bkR0: 
	#Cada símbolo se representa con 7 bits agregándole 0 a la izquierda. 
	line_8_bits = line.zfill(8)
	#Se obtiene la parte alta y baja de cada símbolo ya que se van a transferir en grupos de 4 bits. 
	high= list(line_8_bits[0:4])
	low = line_8_bits[-3:]
	low = list(low.zfill(4))
	#Se obtiene la posicion de donde se introduce el error tanto para la parte alta como baja.  
	pos_high = random.randint(0,3)
	pos_low = random.randint(0,2)
	#Se cambia la posicion a su valor contrario para introducir el error. 
	if (high[pos_high] == "0"):
		high[pos_high] = "1"
	else:
		high[pos_low] = "0"
	if (low[pos_low] == "0"):
		low[pos_low] = "1"
	else:
		low[pos_low] = "0"
	low = "".join(low)
	high = "".join(high)
	output_file.write(high) 
	output_file.write(low)
output_file.close()
bkR0.close()


    

