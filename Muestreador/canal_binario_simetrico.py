#!/usr/bin/env python3.7
import sys
import os
import numpy as np
import random


# texto_codificado.txt contiene los bits de entrada
bkR0 = open("salida_codificador_canal.txt", "r")

#Se introduce un error cada 4 bits 
p_e = 1/7

# texto_con_errores corresponde a la salida del canal simétrico
output_file = open("texto_con_errores.txt", "w")

for line in bkR0: 
	#Cada símbolo se representa con 7 bits agregándole 0 a la izquierda. 
	line_7_bits = line.zfill(8)
	code = list(line_7_bits)
	#Se obtiene la posicion de donde se introduce el error tanto para la parte alta como baja.  
	pos_error = random.randint(3,6)
	#Se cambia la posicion a su valor contrario para introducir el error. 
	if (code[pos_error]  == "0"):
		code[pos_error] = "1"
	else:
		code[pos_error]  = "0"
	code = "".join(code)
	output_file.write(str(code)) 
output_file.close()
bkR0.close()


    

