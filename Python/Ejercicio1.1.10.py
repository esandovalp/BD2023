# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 14:10:20 2023

@author: coron
Ejercicio 1.1.10
"""

import random 

def cantVecesSuma(cantidad):
  dic = {}
  for i in range(0,cantidad):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    
    if dice1+dice2 in dic.keys():
      dic[dice1+dice2] += 1
    else:
      dic[dice1+dice2] = 1
  return dic

print(cantVecesSuma(40))

def cantVecesSuma2(cantidad):
  dic = {}
  for i in range(0,cantidad):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    
    if (dice1,dice2) in dic.keys():
      dic[dice1,dice2] += 1
    else:
      dic[dice1,dice2] = 1
  return dic

print(cantVecesSuma2(4))
  

