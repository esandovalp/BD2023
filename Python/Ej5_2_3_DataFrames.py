import pandas as pd

# Inciso a: y b:
datos= {'Estado': ['EdoMex','CDMX','Veracruz','Jalisco'],
'Pob': [17363,8811,8163,8110]}
inds = [15,9,30,14]
estados = pd.DataFrame(datos, inds)

# Inciso c:
datosMenorP = {'Estado': ['BCS','Colima'], 'Pob': [809,747]}
indsMenorP = [3,6]
menorP = pd.DataFrame(datosMenorP,indsMenorP)
estados = estados._append(menorP)
print('Estados:','\n',estados,'\n')

# inciso d: agregar una columna al DF
estados['PIB'] = [2.9,4.6,1.6,4.7,2.2,5.7]
print('Estados:','\n',estados,'\n')

# inciso e: nuevo DF con claves en orden ascendente
estadosAsc = estados.sort_index()
print('Estados:','\n',estadosAsc,'\n')

# inciso f:



