#!/usr/bin/env python3.7
import sys
import os
import numpy as np
import random

#Multiplicacion de matriz H con vector V = V0
def decoding(v0):
    
    v0 = np.matrix(v0)
    H = np.array([[ 1, 0, 0], [ 0, 1, 0], [ 0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 0],[1,1,1]])
    decode = v0 * H 
    return np.array(decode)

# salida_codificador_canal.txt contiene los bits de entrada
bkR = open("texto_con_errores.txt", "r")

# texto_decodificado.txt corresponde a la salida del decodificador fuente
output_file = open("texto_decodificado.txt", "w")

k = 4
n = 7
a_S = []
a_error = []
a_m = ""
n = 7
H = np.array([[ 1, 0, 0], [ 0, 1, 0], [ 0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 0],[1,1,1]])
for v in bkR: 
    v = v[:-1]
    v_array = np.array(list(v), dtype = int )
    print(v_array)
    s  = np.dot(v_array, H)
    for i in range(0, 3): 
        if (s[i] % 2 != 0) :
            s[i] = 1
        if (s[i] % 2 == 0) :
            s[i] = 0      
    #print(s)
    for i in range(0,128): 
        error_bin = "{0:b}".format(i)
        error_vector = error_bin.zfill(7) 
        error_array = np.array(list(error_vector), dtype = int )
        s_error  = np.dot(error_array, H)
        #print(s)
        comparison = s_error == s 
        equal_array = comparison.all()
        if (equal_array != 0) :
            u = v_array - error_array 
     
        else : 
            u = v_array 
    print(u)
    m = u[-4:]
    m_str = np.array_str(m)
    m_str = m_str.strip("[]")
    m_str = m_str.replace(" ", "")
    a_m = a_m + m_str
    print(m)
    print(m_str)


print(a_m)
u_array = [a_m[i:i+n] for i in range(0, len(a_m), n)]
print(u_array)
for u_element in u_array: 
    output_file.write (u_element)
    output_file.write("\n")
output_file.close()
bkR.close()