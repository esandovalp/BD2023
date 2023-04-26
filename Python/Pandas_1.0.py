# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 14:22:49 2023

@author: coron
"""
import pandas as pd 
import bibArchivos as bib

# crea la serie con los datos de los jugadores 
series = bib.leeVariasSeries('Ej2_1_SeleccionMexicana.csv',1)
selMex = series[0]
print(selMex,'\n')

# inciso a: encontrar el mayor dorsal, imprimir el jugador 
print(f'Mayor dorsal: {selMex.max()}')
print(f'Jugador con el mayor dorsal: {selMex[selMex==selMex.max()]}')

# inciso b: crea y escribe una serie con los jugadores con dorsal < 15
menor15 = selMex[selMex < 15]
print(f'Jugadores con dorsal menor a 15: {menor15}')

# inciso c: crea dos series, una con el nombre de jugadores en orden asc,
# y otra con los dorsales en forma descendente, usando la serie anterior
serieAsc = menor15.sort_index()
print('Orden ascendente por nombre: {serieAsc}')
serieDesc = menor15.sort_values(ascending = False)
print('Orden descendente por dorsal: {serieDesc}')

# inciso d: escribe en un archivo de salida a los jugadores con dorsal < 15
fesc = open('IncisoD.txt','w')
fesc.write(menor15)