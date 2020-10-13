#!/usr/bin/env python3.7
import sys
import os

# Componente: Codificación de fuente
# Grupo LM741

# fuente.txt simula la fuente de información del sistema
input_file = open("fuente.txt", "r")

# bfT_file.txt corresponde a la salida del codificador fuente
bfT_file = open("texto_codificado.txt", "w")

while True: 
    VT = input_file.read(1) # VT corresponde a cada caracter o simbolo
    if not VT: 
        break 
    codigo = ord(VT) # A cada caracter se le asigna su código ASCII
    bkT = int(bin(codigo)[2:]) # Retorna el binario del código ASCII
    bfT_file.write(str(bkT).zfill(7)) # bfT = secuencia de bits
    bfT_file.write("\n")

bfT_file.close()
input_file.close()

