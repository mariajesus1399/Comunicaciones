#!/usr/bin/env python3.7
import sys
import os

# texto_codificado.txt contiene los bits de entrada
bkR = open("texto_decodificado.txt", "r")

# texto_decodificado.txt corresponde a la salida del decodificador fuente
output_file = open("texto_decodificado_final.txt", "w")

for line in bkR: 
    codigo = int(str(line), 2) # Convierte de binario a ASCII
    VR = chr(int(codigo)) # VR corresponde a cada caracter
    output_file.write(str(VR)) # Almacena cada caracter en decodificado
output_file.close()
bkR.close()
