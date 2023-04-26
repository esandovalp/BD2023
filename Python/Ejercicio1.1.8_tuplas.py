# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 13:20:58 2023

@author: coron

Ej 1.1.8 ejemplo con tuplas 
"""

def tuplaPares(tupla):
  resul = ()
  for i in range(0,len(tupla),2):
    resul += tupla[i],
  return resul


# Programa principal
r1 = tuplaPares(())
print('Resultado r1: ', r1)

r2 = tuplaPares((1,))
print('Resultado r2: ',r2)

r3 = tuplaPares(('Yo', 'mi', 'a', 'prueba', 'tupla'))
print('Resultado r3: ',r3)