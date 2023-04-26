# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 13:40:38 2023

@author: coron

Ejercicio 1.1.9 Diccionarios 
"""
# funcion que recibe una cadena y regresa un diccionario con la
# cantidad de apariciones de cada palabra en la cadena 

def palabras_Cad(cad):
  dic = {}
  lista = cad.split()
  for palabra in lista:
    if palabra in dic.keys():
      dic[palabra] += 1
    else:
      dic[palabra] = 1
  return dic
  
print(palabras_Cad('Escribir una funcion que reciba una cadena'))