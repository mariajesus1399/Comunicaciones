# -*- coding: utf-8 -*-
from random import *
import numpy as np
import sys
import os

def encoding(msg):
    d1 = [1,0,0,0]
    d2 = [0,1,0,0]
    d3 = [0,0,1,0]
    d4 = [0,0,0,1]
    g = []
    G = []
    p1 = [] #Vector for parity bit 1
    p2 = [] #Vector for parity bit 2
    p3 = [] #Vector for parity bit 3
    for i in range(4):
        p1.append((d2[i] ^ d3[i] ^ d4[i]))  
    for i in range(4):
        p2.append((d1[i] ^ d3[i] ^ d4[i]))	
    for i in range(4):
        p3.append((d1[i] ^ d2[i] ^ d4[i]))
    for i in range(len(d1)): #Bien podria ser cualquier databit
        g.append(p1[i])
        g.append(p2[i])
        g.append(p3[i]) # For parity	
        g.append(d1[i]) 
        g.append(d2[i])
        g.append(d3[i])
        g.append(d4[i]) # For databits 
        G.append(g)				
        g = []
    matriz0 = np.matrix(msg)
    matriz1 = np.matrix(G)
    coding = matriz0 * matriz1 # vectores u= Gm
    return np.array(coding)

def file_array():
    dato = []
    try:
        archivo=open("texto_codificado.txt",'r') # archivo con k bits

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
# print(np.array(texto))

texto1 = []
# Método 2, con índice
for indice in range(len(texto)):
    caracter = str(texto[indice])
    texto1.append(caracter)
    #print(texto1[indice])

##################### texto es una matriz donde cada letra es una columna
##################### texto1 es una matriz donde cada letra es una fila

aux = 0
word =" "
#blf = [1][]
for i in range(len(texto1)) :
    word += texto1[aux]
    aux += 1

def split(word): 
    lista = list(word)
    #lista = np.array(word)
    print(len(lista))
    #print(lista)
    lista_num = []
    #xs = list(map(int, lista)) 
    
    for ind in range(len(lista)):
        if lista[ind].isdigit():
            num = int(lista[ind])
            lista_num.append(num)
    
    # print(lista_num) # se tiene una lista con cada digito separado
    return lista_num 


blf = split(word) # lista con cada digito

k = 4
n = 7
R = k/n
cant = int (len(blf)/k) # cantidad de vectores m de k bits a la entrada del codificador
m = [0]*cant
u = [0]*cant

print ("tamaño :",len(blf)) # cantidad de bits

#Se realiza division del vector blf en grupos de k bits
for i in range(cant):
    if i == 0 :
        m[i] = blf[0:k]
    else:
        m[i] = blf[(i*k):(i*k)+k]
    # print (m[i])
    # m[i] es una matriz donde en cada fila hay un vector de k bits
        
#Multiplicacion de m*G
for i in range(cant):

    u[i] = encoding(m[i]) # se llama a la función que hace u = G*m
    # print (u[i])


BCT_file = open("salida_codificador_canal.txt", "w") # en este archivo se envian los bits codificados

# Acá se cambian los bits pares por ceros e impares por unos
for i in range(cant):
    for j in range(len(np.array(u[i]))): 
        for k in range(0, n):
            if (np.matrix(u[i][j][k]) % 2 != 0) :
               u[i][j][k] = 1
            if (np.matrix(u[i][j][k])%2 == 0) :
                u[i][j][k] = 0        
        
        vector_u_array = str(np.array(u[i]))
        vector_u_string = vector_u_array.strip("[]")
        vector_u = vector_u_string.replace(" ", "")
        BCT_file.write(vector_u) # bfT = secuencia de bits
        BCT_file.write("\n")

BCT_file.close()
