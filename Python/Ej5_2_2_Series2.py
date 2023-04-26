import bibArchivos as bib

# inciso a: crea las dos series
series = bib.leeVariasSeries('Ej2_2_PoblacionMundial.csv',2)
pm10 = series[0]
pm17 = series[1]
print('Poblacion 2010:',pm10,'\n')
print('Poblacion 201:',pm17,'\n')

# inciso b: porcentaje de crecimiento de 2010 a 2017
porcen = (pm17-pm10)/pm10
print('Porcentaje de crecimiento:',porcen,'\n')

# inciso c: paises con mayor crecimiento
maxim = porcen.max()
print('Crecimiento maximo:',maxim,'\n')
print('Paises con crecimiento maximo:',porcen[porcen == maxim],'\n') # toma los paises que cumplen con la condicion

# inciso d: porcentaje promedio de crecimiento
promedio = porcen.mean()
print('Porcentaje promedio de crecimiento',promedio,'\n')

# inciso e: paises con crecimiento >= al promedio
print('Paises con crecimiento >= al promedio:',porcen[porcen >= promedio],'\n')

# inciso f: para casa :D
def cantPaises(serie):
    lista = [0,0,0]
    delta = 0.000001
    for i in serie.index:
        if abs(serie[i]) <= delta:
            lista[1] += 1
        else:
            if serie[i] < 0:
                lista[0] += 1
            else:
                lista[2] += 1
    return lista