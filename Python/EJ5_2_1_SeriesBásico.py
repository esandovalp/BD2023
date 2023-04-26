# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 13:46:48 2023

@author: psdist
"""

import pandas as pd
import bibArchivos as bib

#Crea la serie con los datos de los jugadores.
series= bib.leeVariasSeries("Ej2_1_SeleccionMexicana.csv", 1)
selMex= series[0]
print(selMex,'\n')

#Inc. a: escribir el jugador con mayor dorsal.
print("Mayor dorsal: ",selMex.max())
print("Jugador con el mayor dorsal: ",selMex[selMex == selMex.max()],'\n')

#Inc. b: crea y escribe una serie con los jugadores con dorsal < 15.
menor15= selMex[selMex < 15]
print("Jugadores con dorsal < 15: ",'\n',menor15,'\n')

#Inc. c: crea dos series, una con el nombre de jugadores en orden ascendente,
# y otra con los dorsales en forma descendente, usando la serie anterior.
serieAsc= menor15.sort_index()
print("Orden ascendente por nombre: ",'\n',serieAsc,'\n')
serieDesc= menor15.sort_values(ascending=False)
print("Orden descendente por dorsal: ",'\n',serieDesc,'\n')

#Inc. d: escribe en un archivo de salida a los jugadores con dorsal < 15.


