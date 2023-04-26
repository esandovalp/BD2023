import pandas as pd
import bibArchivos as bib

# inciso a: leer los datos y crear el DF
columnas = ['NOMBRE','GÉNERO','EDAD','OCUPACIÓN','CP']
encuesta = bib.leeDatosDF('Ej2_4_EncuestaOcupacion.csv',False,columnas)
print('Encuesta:\n',encuesta,'\n')

# inciso b: crear serie en ocupación
ocupacion = encuesta['OCUPACIÓN']
print('Ocupación:\n',ocupacion,'\n')

# inciso c:
renglones3 = encuesta.iloc[3:6]
print('Renglones3:\n',renglones3,'\n')

# inciso d:
print('2o. encuestado: ', encuesta.iloc[1,[0,1]])
print('2o. encuestado: ', encuesta.loc[1,['NOMBRE','GÉNERO']],'\n')

# inciso e:
encuesta.loc[len(encuesta)] = ['ANA FLORES','F',30,'ADMIN',4577]
print('Encuesta e:\n ', encuesta,'\n')

# inciso f
print('Inciso f:\n',encuesta.loc[:,['EDAD','OCUPACIÓN']])

# inciso g
print('Inciso g:\n',encuesta.iloc[:,[0,3]])

# inciso i
print('Uso de las funciones de agregados:\n',encuesta.describe())

# inciso j
mayores = encuesta.iloc[:,[0,2,3]][encuesta['EDAD']>50]
print('Inciso j:\n',mayores)