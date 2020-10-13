#!/usr/bin/env python3.7
import sys
import os
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from itertools import repeat

# salida_codificador_canal.txt contiene los bits de entrada
# Bloques de 7 bits
bkR = open("salida_codificador_canal.txt", "r")

# bfT_file.txt corresponde a los simbolos del generados por los bits del codificador de canal
simb = open("simbolos.txt", "w")

for line in bkR: 
    # Convierte de bits a simbolos
    codigo = str(int(str(line), 2)) # Convierte de binario a decimal
    simb.write(codigo) # bfT = secuencia de bits
    simb.write("\n")
    
simb.close()   
bkR.close()


# Se debe crear un array de decimales.
def file_array():
    dato = []
    try:
        archivo=open("simbolos.txt",'r') # archivo con k bits

        leer_fila= archivo.readlines()
        archivo.close()
        for lista in leer_fila:
            if lista[-1]=="\n":
                x = int(lista[:-1].split(", ")[0])
                dato.append(x)
            else:
                x = int(lista.split(", ")[0])
                dato.append(x)
    except(FileNotFoundError):
        advert = "File not found"
        print(advert)
    return dato


#LEE MENSAJE, SE DEBE VAMBIAR POR .TXT
texto = file_array()
#print(np.array(texto))

texto1 = []
# Método 2, con índice
for indice in range(len(texto)):
    caracter = str(texto[indice])
    texto1.append(caracter)
    #print(texto1[indice])

##################### texto es una matriz donde cada letra es una columna
##################### texto1 es una matriz donde cada letra es una fila


an = texto
T_s = 50
k = len(an)
#CANTIDAD DE SIMBOLOS
k = len(an)
#Longitud de señales
signal_0 = [0]*k

#Muestras/Pulso
sample = 50
#array contenedor de elementos duplicados
contain = [0]*k*sample

t = np.linspace(0,T_s, sample*k, endpoint=False)
signal_0 = signal.square(2 * np.pi * 2 * t)
for i in range(k):
    if signal_0[i] <= 0:
        signal_0[i] = 0
    

#Contiene elementos repetidos de an, sample veces, NO VEO LA NECESIDAD DE MULTIPLICAR
#POR 1  
contain = [x for item in an for x in repeat(item, sample)]
print(len(contain))

# Ruido blanco
noise_amplitude = 1
awgn = noise_amplitude * np.random.randn(k*sample)

#Señal con ruido
contain_ruido = contain + awgn

x_k = open("salida_modulador_ruido.txt", "w")
for i in range(len(contain_ruido)):
    x_k.write(str(contain_ruido[i]))
    x_k.write("\n")

x_k.close()      
plt.plot(t, contain_ruido)
plt.ylim(-130,130)





