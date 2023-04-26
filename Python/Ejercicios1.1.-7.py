# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 13:27:48 2023

@author: coron
"""

# ejercicio 5.1.1
def factorial(n):
  if n >= 0:
    fac = 1
    for i in range(1,n+1):
      fac = fac * i
    print(fac)

def fibonacci():
  a,b=0,1
  while b < 20:
    print("a= ", a, "b=", b)
    a, b = b, a + b
    print()

# ejercicio 5.1.3
def ex3():
  cad = 'hola'
  n = len(cad)
  a,b=0,1
  while a < n :
    print(cad[a])
    a,b=a,a+b
    
# Ej. 5.1.5 manejo básico de listas 
import random

# Genera las califs. de manera aleatoria 
n = 5
califs = []
for i in range(n):
  califs.append(float(random.randint(6, 10)))
  
print('Califs: ', califs)

# Lista con los porcenatajes 
porcens = [0.1,0.2,0.23,0.30,0.17]

# Calcula el promedio ponderado
prom = 0
for i in range(n):
  prom = prom + califs[i]*porcens[i]
  
#print('Promedio (con decimales): ', prom)
#print('Promedio sin decimales: ', round(prom))

# ej 5.1.6 intersección entre listas
def hayInterseccion(a,b):
  n = 0
  if len(b) > len(a):
    n = len(b)
  else:
    n = len(a)
    
  A = False
  if n >= 3 and n <= 6:
    for i in range(n):
      j= i+1
      for j in range(n):
        if a[i] == b[j]:  
          A = True
  if A == True:
    print('Hay interseccion')
  else:
    print('No hay interseccion')
    

#hayInterseccion([1,2,3,4],[9,4,7,0])



