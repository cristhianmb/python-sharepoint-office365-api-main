
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import numpy as np
from scipy.stats import trim_mean




    

#Ruta archivo BD para Indicadores Cálculos
ruta_archivo_excel50 = r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\MergeTotal\MergeTotalF.xlsx"

#-...................... Hoja Indicadores Cálculos
#  Nombre de las hojas que deseas cargar del archivo MergeTotalF.xlsx
hoja50 = 'MergeTotalF'

#...........Cargar el archivo Excel MergeTotalF en DataFrames de pandas
df_DB = pd.read_excel(ruta_archivo_excel50, sheet_name=hoja50)
nombres_columnas50 = [f'Column{i+1}' for i in range(df_DB.shape[1])]
df_DB.columns = nombres_columnas50












# Aplicar la fórmula para Indicador 1.1.1.1:
df500 = df_DB.copy()

# Aplicar la fórmula para Indicador 1.1.1.1
def aplicar_formula(row):
    numerador = (row['Column5'] + row['Column6']) - (row['Column7'] + row['Column8'])
    denominador = row['Column4']

    # Evitar la división por cero
    if denominador == 0:
        return 0

    # Calcular el resultado sin normalizar
    resultado = (numerador / denominador) * 100

    return resultado

# Aplicar la fórmula a la columna '1.1.1.1'
df500['1.1.1.1'] = df500.apply(aplicar_formula, axis=1)

# Calcular la media recortada del 5%
media_recortada_1_1_1_1 = trim_mean(df500['1.1.1.1'], proportiontocut=0.05)

# Normalizar la columna '1.1.1.1' entre 0 y 100 y eliminar decimales
df500['1.1.1.1'] = round((df500['1.1.1.1'] - df500['1.1.1.1'].min()) / (df500['1.1.1.1'].max() - df500['1.1.1.1'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df500['1.1.1.1'] = df500['1.1.1.1'].clip(0, 100)




# Definir la función para la fórmula 1.1.1.2
df501 = df_DB.copy()

def aplicar_formula2(row):
    numerador = ((row['Column5'] + row['Column6']) - (row['Column7'] + row['Column8'])) - ((row['Column9'] + row['Column10']) - (row['Column11'] + row['Column12']))
    denominador = (row['Column9'] + row['Column10']) - (row['Column11'] + row['Column12'])

    if denominador == 0:
        return 0  # Evitar la división por cero, puedes ajustar esto según tus necesidades

    return (numerador / denominador) * 100

# Aplicar la fórmula a la columna '1.1.1.2'
df501['1.1.1.2'] = df501.apply(aplicar_formula2, axis=1)

# Calcular la media recortada del 5%
media_recortada_1_1_1_2 = trim_mean(df501['1.1.1.2'], proportiontocut=0.05)

# Normalizar la columna '1.1.1.2' entre 0 y 100 y eliminar decimales
df501['1.1.1.2'] = round((df501['1.1.1.2'] - df501['1.1.1.2'].min()) / (df501['1.1.1.2'].max() - df501['1.1.1.2'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df501['1.1.1.2'] = df501['1.1.1.2'].clip(0, 100)




# Aplicar la fórmula para Indicador 1.1.1.3
df502 = df_DB.copy()

# Definir la función para la fórmula 1.1.1.3
def aplicar_formula3(row):
    numerador = row['Column5'] + row['Column6']
    denominador = row['Column13']

    if denominador == 0:
        return 0  # Evitar la división por cero, puedes ajustar esto según tus necesidades

    return (numerador / denominador) * 100

# Aplicar la fórmula a la columna '1.1.1.3'
df502['1.1.1.3'] = df502.apply(aplicar_formula3, axis=1)


# Calcular la media recortada del 5%
media_recortada_1_1_1_3 = trim_mean(df502['1.1.1.3'], proportiontocut=0.05)
# Redondear el valor
media_recortada_1_1_1_3_redondeada = round(media_recortada_1_1_1_3, 2)  # Puedes ajustar el número de decimales según tus necesidades

# Normalizar la columna '1.1.1.3' entre 0 y 100 y eliminar decimales
df502['1.1.1.3'] = round((df502['1.1.1.3'] - df502['1.1.1.3'].min()) / (df502['1.1.1.3'].max() - df502['1.1.1.3'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df502['1.1.1.3'] = df502['1.1.1.3'].clip(0, 100)









# Aplicar la fórmula para Indicador 1.1.1.4


df503 = df_DB.copy()

# Definir la función para la fórmula 1.1.1.4
def aplicar_formula4(row):
    numerador = row['Column14'] + row['Column15'] + row['Column16'] + row['Column17'] + row['Column18'] - row['Column19']
    denominador = row['Column20'] + row['Column21'] + row['Column22'] + row['Column23']
    
    if denominador == 0:
        return 0  # Evitar la división por cero, puedes ajustar esto según tus necesidades
        
    return (numerador / denominador) * 100

# Aplicar la fórmula a la columna '1.1.1.4'
df503['1.1.1.4'] = df503.apply(aplicar_formula4, axis=1)

# Normalizar la columna '1.1.1.4' entre 0 y 100 y eliminar decimales
df503['1.1.1.4'] = round((df503['1.1.1.4'] - df503['1.1.1.4'].min()) / (df503['1.1.1.4'].max() - df503['1.1.1.4'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df503['1.1.1.4'] = df503['1.1.1.4'].clip(0, 100)







# Aplicar la fórmula para Indicador 1.1.1.5

df504 = df_DB.copy()

# Definir la función para la fórmula 1.1.1.5
def aplicar_formula5(row):
    numerador = row.loc['Column24':'Column29'].sum() - row.loc['Column30':'Column35'].sum()
    denominador = row.loc['Column30':'Column35'].sum()
    
    if denominador == 0:
        return 0  # Evitar la división por cero, puedes ajustar esto según tus necesidades
        
    return (numerador / denominador) * 100

# Aplicar la fórmula a la columna '1.1.1.4'
df504['1.1.1.5'] = df504.apply(aplicar_formula5, axis=1)


# Normalizar la columna '1.1.1.4' entre 0 y 100 y eliminar decimales
df504['1.1.1.5'] = round((df504['1.1.1.5'] - df504['1.1.1.5'].min()) / (df504['1.1.1.5'].max() - df504['1.1.1.5'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df504['1.1.1.5'] = df504['1.1.1.5'].clip(0, 100)















# Aplicar la fórmula para Indicador 1.1.2.1


df505 = df_DB.copy()

# Definir la función para la fórmula 1.1.2.1
def aplicar_formula6(row):
    numerador = row['Column36'] + row['Column37'] 
    denominador = row['Column38'] + row['Column37'] 
    
    if denominador == 0:
        return 0  # Evitar la división por cero, puedes ajustar esto según tus necesidades
        
    return 1 - ((numerador / denominador) * 100)

# Aplicar la fórmula a la columna '1.1.1.4'
df505['1.1.2.1'] = df505.apply(aplicar_formula6, axis=1)

# Normalizar la columna '1.1.1.4' entre 0 y 100 y eliminar decimales
df505['1.1.2.1'] = round((df505['1.1.2.1'] - df505['1.1.2.1'].min()) / (df505['1.1.2.1'].max() - df505['1.1.2.1'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df505['1.1.2.1'] = df505['1.1.2.1'].clip(0, 100)








# Aplicar la fórmula para Indicador 1.1.2.2




df506 = df_DB.copy()

# Definir la función para la fórmula 1.1.2.2
def aplicar_formula7(row):
    numerador = row['Column40'] 
    denominador = row['Column39'] + row['Column40']  + row['Column41'] 
    
    if denominador == 0:
        return 0  # Evitar la división por cero, puedes ajustar esto según tus necesidades
        
    return 1 - ((numerador / denominador) * 100)

# Aplicar la fórmula a la columna '1.1.1.4'
df506['1.1.2.2'] = df506.apply(aplicar_formula7, axis=1)

# Normalizar la columna '1.1.1.4' entre 0 y 100 y eliminar decimales
df506['1.1.2.2'] = round((df506['1.1.2.2'] - df506['1.1.2.2'].min()) / (df506['1.1.2.2'].max() - df506['1.1.2.2'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df506['1.1.2.2'] = df506['1.1.2.2'].clip(0, 100)









# Aplicar la fórmula para Indicador 1.1.2.3



df507 = df_DB.copy()

# Definir la función para la fórmula 1.1.2.3
def aplicar_formula8(row):
    numerador = row['Column43'] 
    denominador = row['Column42'] + row['Column43'] + row['Column44']
    
    if denominador == 0:
        return 0  # Evitar la división por cero, puedes ajustar esto según tus necesidades
        
    return 1 - ((numerador / denominador) * 100)

# Aplicar la fórmula a la columna '1.1.1.4'
df507['1.1.2.3'] = df507.apply(aplicar_formula8, axis=1)

# Normalizar la columna '1.1.1.4' entre 0 y 100 y eliminar decimales
df507['1.1.2.3'] = round((df507['1.1.2.3'] - df507['1.1.2.3'].min()) / (df507['1.1.2.3'].max() - df507['1.1.2.3'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df507['1.1.2.3'] = df507['1.1.2.3'].clip(0, 100)








# Aplicar la fórmula para Indicador 1.1.2.4




df508 = df_DB.copy()

# Definir la función para la fórmula 1.1.2.4
def aplicar_formula9(row):
    numerador = row['Column46'] 
    denominador = row['Column45'] + row['Column46'] + row['Column47']
    
    if denominador == 0:
        return 0  # Evitar la división por cero, puedes ajustar esto según tus necesidades
        
    return 1 - ((numerador / denominador) * 100)

# Aplicar la fórmula a la columna '1.1.1.4'
df508['1.1.2.4'] = df508.apply(aplicar_formula9, axis=1)

# Normalizar la columna '1.1.1.4' entre 0 y 100 y eliminar decimales
df508['1.1.2.4'] = round((df508['1.1.2.4'] - df508['1.1.2.4'].min()) / (df508['1.1.2.4'].max() - df508['1.1.2.4'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df508['1.1.2.4'] = df508['1.1.2.4'].clip(0, 100)












# Aplicar la fórmula para Indicador 1.1.2.5





df509 = df_DB.copy()

# Definir la función para la fórmula 1.1.2.5
def aplicar_formula10(row):
    numerador = row['Column48'] + row['Column49'] + row['Column50']
    denominador = row['Column51'] + row['Column52'] + row['Column53'] + row['Column54'] + row['Column55'] + row['Column56'] + row['Column57'] + row['Column58']
    
    if denominador == 0:
        return 0  # Evitar la división por cero, puedes ajustar esto según tus necesidades
        
    return 1 - ((numerador / denominador) * 100)

# Aplicar la fórmula a la columna '1.1.1.4'
df509['1.1.2.5'] = df509.apply(aplicar_formula10, axis=1)

# Normalizar la columna '1.1.1.4' entre 0 y 100 y eliminar decimales
df509['1.1.2.5'] = round((df509['1.1.2.5'] - df509['1.1.2.5'].min()) / (df509['1.1.2.5'].max() - df509['1.1.2.5'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df509['1.1.2.5'] = df509['1.1.2.5'].clip(0, 100)






# Aplicar la fórmula para Indicador 1.2.1


df510 = df_DB.copy()

# Definir la función para la fórmula 1.2.1
def aplicar_formula11(row):
    numerador = row['Column59']
    denominador = row['Column62']
    
    if denominador == 0:
        return 0  # Evitar la división por cero, puedes ajustar esto según tus necesidades
        
    return (numerador / denominador) * 100

# Aplicar la fórmula a la columna '1.1.1.4'
df510['1.2.1'] = df510.apply(aplicar_formula11, axis=1)

# Normalizar la columna '1.1.1.4' entre 0 y 100 y eliminar decimales
df510['1.2.1'] = round((df510['1.2.1'] - df510['1.2.1'].min()) / (df510['1.2.1'].max() - df510['1.2.1'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df510['1.2.1'] = df510['1.2.1'].clip(0, 100)






# Aplicar la fórmula para Indicador 1.2.2




df511 = df_DB.copy()

# Definir la función para la fórmula 1.2.2
def aplicar_formula12(row):
    numerador = row['Column63'] + row['Column64']
    denominador = row['Column64']
    
    if denominador == 0:
        return 0  # Evitar la división por cero, puedes ajustar esto según tus necesidades
        
    return (numerador / denominador) * 100

# Aplicar la fórmula a la columna '1.1.1.4'
df511['1.2.2'] = df511.apply(aplicar_formula12, axis=1)

# Normalizar la columna '1.1.1.4' entre 0 y 100 y eliminar decimales
df511['1.2.2'] = round((df511['1.2.2'] - df511['1.2.2'].min()) / (df511['1.2.2'].max() - df511['1.2.2'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df511['1.2.2'] = df511['1.2.2'].clip(0, 100)








# Aplicar la fórmula para Indicador 2.1



df512 = df_DB.copy()

columnas_numerador = df512.loc[:, 'Column65':'Column70']
columnas_denominador = df512.loc[:, 'Column71':'Column76']

df512['2.1'] = (columnas_numerador.sum(axis=1) - columnas_denominador.sum(axis=1)) / np.abs(columnas_denominador.sum(axis=1)) * 100

# Manejar valores infinitos o NaN
df512['2.1'] = df512['2.1'].replace([np.inf, -np.inf], np.nan).fillna(0)



# Normalizar la columna '1.1.1.4' entre 0 y 100 y eliminar decimales
df512['2.1'] = round((df512['2.1'] - df512['2.1'].min()) / (df512['2.1'].max() - df512['2.1'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df512['2.1'] = df512['2.1'].clip(0, 100)











# Aplicar la fórmula para Indicador 2.2

df513 = df_DB.copy()

# Definir la función para la fórmula 2.2
def aplicar_formula14(row):
    numerador = (row['Column77'] + row['Column78']) - (row['Column79'] + row['Column80'])
    denominador = np.abs(row['Column79'] + row['Column80'])
    
    if denominador == 0:
        return 0  # Evitar la división por cero, puedes ajustar esto según tus necesidades
        
    # Aplicar la fórmula y convertir a porcentaje
    resultado = (numerador / denominador) * 100

    return resultado

# Aplicar la fórmula a la columna '2.2'
df513['2.2'] = df513.apply(aplicar_formula14, axis=1)

# Normalizar la columna '2.2' entre 0 y 100 y eliminar decimales
df513['2.2'] = round((df513['2.2'] - df513['2.2'].min()) / (df513['2.2'].max() - df513['2.2'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df513['2.2'] = df513['2.2'].clip(0, 100)






# Aplicar la fórmula para Indicador 2.3



df513_1 = df_DB.copy()

# Definir la función para aplicar la fórmula
def aplicar_formula14_1(row):
    numerador = (
        row['Column81'] - row['Column82'] - row['Column83'] -
        row['Column84'] - row['Column85'] - row['Column86'] -
        row['Column87'] - row['Column88'] - row['Column89'] -
        row['Column90']
    )
    denominador = (
        row['Column91'] - row['Column92'] - row['Column93'] -
        row['Column94'] - row['Column95'] - row['Column96'] -
        row['Column97'] - row['Column98'] - row['Column99'] -
        row['Column100']
    )
    
    if denominador == 0:
        return 0  # Evitar la división por cero, puedes ajustar esto según tus necesidades
        
    # Aplicar la fórmula y convertir a porcentaje
    resultado = ((numerador / denominador) - 1) * 100

    return resultado

# Aplicar la función a la columna '2.3'
df513_1['2.3'] = df513_1.apply(aplicar_formula14_1, axis=1)

# Normalizar la columna '2.3' entre 0 y 100 y eliminar decimales
df513_1['2.3'] = round((df513_1['2.3'] - df513_1['2.3'].min()) / (df513_1['2.3'].max() - df513_1['2.3'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df513_1['2.3'] = df513_1['2.3'].clip(0, 100)










# Aplicar la fórmula para Indicador 3.1



df514 = df_DB.copy()

# Definir la función para aplicar la fórmula
def aplicar_formula15(row):
    numerador = row['Column101'] - row['Column102']
    denominador = np.abs(row['Column102'])
    
    if denominador == 0:
        return 0  # Evitar la división por cero, puedes ajustar esto según tus necesidades
        
    # Aplicar la fórmula y convertir a porcentaje
    resultado = (numerador / denominador) * 100

    return resultado

# Aplicar la función a la columna '3.1'
df514['3.1'] = df514.apply(aplicar_formula15, axis=1)

# Normalizar la columna '3.1' entre 0 y 100 y eliminar decimales
df514['3.1'] = round((df514['3.1'] - df514['3.1'].min()) / (df514['3.1'].max() - df514['3.1'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df514['3.1'] = df514['3.1'].clip(0, 100)










# Aplicar la fórmula para Indicador 4.1.1



df515 = df_DB.copy()

def aplicar_formula16(row):
    denominador = row['Column104']
    
    # Evitar la división por cero
    if denominador == 0:
        return 0
    
    numerador = ((row['Column103'] / denominador) - 1) * 100
    
    return numerador


# Aplicar la fórmula y redondear hacia arriba los resultados
df515['4.1.1'] = df515.apply(aplicar_formula16, axis=1).apply(np.ceil)


# Normalizar la columna '3.1' entre 0 y 100 y eliminar decimales
df515['4.1.1'] = round((df515['4.1.1'] - df515['4.1.1'].min()) / (df515['4.1.1'].max() - df515['4.1.1'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df515['4.1.1'] = df515['4.1.1'].clip(0, 100)





# Aplicar la fórmula para Indicador 4.1.2

df516 = df_DB.copy()

def aplicar_formula17(row):
    denominador = row['Column106']
    
    # Evitar la división por cero
    if denominador == 0:
        return 0
    
    numerador = ((row['Column105'] / denominador) - 1) * 100
    
    return numerador

df516['4.1.2'] = df516.apply(aplicar_formula17, axis=1) 


# Normalizar la columna '3.1' entre 0 y 100 y eliminar decimales
df516['4.1.2'] = round((df516['4.1.2'] - df516['4.1.2'].min()) / (df516['4.1.2'].max() - df516['4.1.2'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df516['4.1.2'] = df516['4.1.2'].clip(0, 100)



# Aplicar la fórmula para Indicador 4.1.3


df517 = df_DB.copy()

def aplicar_formula18(row):
    denominador = row['Column108']
    
    # Evitar la división por cero
    if denominador == 0:
        return 0
    
    numerador = ((row['Column107'] / denominador) - 1) * 100
    
    return numerador

df517['4.1.3'] = df517.apply(aplicar_formula18, axis=1) 



# Normalizar la columna '3.1' entre 0 y 100 y eliminar decimales
df517['4.1.3'] = round((df517['4.1.3'] - df517['4.1.3'].min()) / (df517['4.1.3'].max() - df517['4.1.3'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df517['4.1.3'] = df517['4.1.3'].clip(0, 100)





# Aplicar la fórmula para Indicador 4.1.4


df518 = df_DB.copy()

def aplicar_formula19(row):
    denominador = row['Column110']
    
    # Evitar la división por cero
    if denominador == 0:
        return 0
    
    numerador = ((row['Column109'] / denominador) - 1) * 100
    
    return numerador

df518['4.1.4'] = df518.apply(aplicar_formula19, axis=1) 

# Normalizar la columna '3.1' entre 0 y 100 y eliminar decimales
df518['4.1.4'] = round((df518['4.1.4'] - df518['4.1.4'].min()) / (df518['4.1.4'].max() - df518['4.1.4'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df518['4.1.4'] = df518['4.1.4'].clip(0, 100)



# Aplicar la fórmula para Indicador 4.2.1

df519 = df_DB.copy()

def aplicar_formula20(row):
    denominador = row['Column112']
    
    # Evitar la división por cero
    if denominador == 0:
        return 0
    
    numerador = ((row['Column111'] / denominador) - 1) * 100
    
    return numerador

df519['4.2.1'] = df519.apply(aplicar_formula20, axis=1) 

# Normalizar la columna '4.2.1' entre 0 y 100 y eliminar decimales
df519['4.2.1'] = round((df519['4.2.1'] - df519['4.2.1'].min()) / (df519['4.2.1'].max() - df519['4.2.1'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df519['4.2.1'] = df519['4.2.1'].clip(0, 100)



# Aplicar la fórmula para Indicador 4.2.2

df520 = df_DB.copy()

def aplicar_formula21(row):
    denominador = row['Column114']
    
    # Evitar la división por cero
    if denominador == 0:
        return 0
    
    numerador = ((row['Column113'] / denominador) - 1) * 100
    
    return numerador

df520['4.2.2'] = df520.apply(aplicar_formula21, axis=1) 


# Normalizar la columna '4.2.1' entre 0 y 100 y eliminar decimales
df520['4.2.2'] = round((df520['4.2.2'] - df520['4.2.2'].min()) / (df520['4.2.2'].max() - df520['4.2.2'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df520['4.2.2'] = df520['4.2.2'].clip(0, 100)







# Aplicar la fórmula para Indicador 4.2.3

df521 = df_DB.copy()

def aplicar_formula22(row):
    denominador = row['Column116']
    
    # Evitar la división por cero
    if denominador == 0:
        return 0
    
    numerador = ((row['Column115'] / denominador) - 1) * 100
    
    return numerador

df521['4.2.3'] = df521.apply(aplicar_formula22, axis=1) 

# Normalizar la columna '4.2.1' entre 0 y 100 y eliminar decimales
df521['4.2.3'] = round((df521['4.2.3'] - df521['4.2.3'].min()) / (df521['4.2.3'].max() - df521['4.2.3'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df521['4.2.3'] = df521['4.2.3'].clip(0, 100)





# Aplicar la fórmula para Indicador 4.2.4

df522 = df_DB.copy()

def aplicar_formula23(row):
    denominador = row['Column118']
    
    # Evitar la división por cero
    if denominador == 0:
        return 0
    
    numerador = ((row['Column117'] / denominador) - 1) * 100
    
    return numerador

df522['4.2.4'] = df522.apply(aplicar_formula23, axis=1) 

# Normalizar la columna '4.2.1' entre 0 y 100 y eliminar decimales
df522['4.2.4'] = round((df522['4.2.4'] - df522['4.2.4'].min()) / (df522['4.2.4'].max() - df522['4.2.4'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df522['4.2.4'] = df522['4.2.4'].clip(0, 100)








# Aplicar la fórmula para Indicador 4.2.5


df523 = df_DB.copy()

def aplicar_formula24(row):
    denominador = row['Column124']
    
    # Evitar la división por cero
    if denominador == 0:
        return 0
    
    numerador = (((row['Column121'] / denominador) - 1) * 100)
    
    return numerador

df523['4.2.5'] = df523.apply(aplicar_formula24, axis=1) 



# Normalizar la columna '4.2.1' entre 0 y 100 y eliminar decimales
df523['4.2.5'] = round((df523['4.2.5'] - df523['4.2.5'].min()) / (df523['4.2.5'].max() - df523['4.2.5'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df523['4.2.5'] = df523['4.2.5'].clip(0, 100)





# Aplicar la fórmula para Indicador 4.2.6

df524 = df_DB.copy()

def aplicar_formula25(row):
    denominador = row['Column130']
    
    # Evitar la división por cero
    if denominador == 0:
        return 0
    
    numerador = (((row['Column127'] / denominador) - 1) * 100)
    
    return numerador

df524['4.2.6'] = df524.apply(aplicar_formula25, axis=1) 
# Normalizar la columna '4.2.1' entre 0 y 100 y eliminar decimales
df524['4.2.6'] = round((df524['4.2.6'] - df524['4.2.6'].min()) / (df524['4.2.6'].max() - df524['4.2.6'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df524['4.2.6'] = df524['4.2.6'].clip(0, 100)




# Aplicar la fórmula para Indicador 5.1 es Column131

df525 = df_DB.copy()


if 'Column131' in df525.columns:
    # Normalizar la columna 'Column131' entre 0 y 100 y eliminar decimales
    df525['Column131'] = round((df525['Column131'] - df525['Column131'].min()) / (df525['Column131'].max() - df525['Column131'].min()) * 100)

    # Asegurarse de que los valores estén en el rango correcto (0-100)
    df525['Column131'] = df525['Column131'].clip(0, 100)

    # Renombrar la columna a '5.1'
    df525 = df525.rename(columns={'Column131': '5.1'})









# Aplicar la fórmula para Indicador 6.1

df526 = df_DB.copy()

def aplicar_formula26(row):
    denominador_parte1 = row['Column135']
    denominador_parte2 = row['Column139']
    
    # Evitar la división por cero
    if denominador_parte1 == 0 or denominador_parte2 == 0:
        return 0
    
    numerador = (row['Column132'] + row['Column133'] - row['Column134']) / denominador_parte1
    denominador = (row['Column136'] + row['Column137'] - row['Column138']) / denominador_parte2
    
    resultado = ((numerador / denominador) - 1) * 100
    
    
    return 1 - resultado

df526['6.1'] = df526.apply(aplicar_formula26, axis=1)



# Normalizar la columna '4.2.1' entre 0 y 100 y eliminar decimales
df526['6.1'] = round((df526['6.1'] - df526['6.1'].min()) / (df526['6.1'].max() - df526['6.1'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df526['6.1'] = df526['6.1'].clip(0, 100)



# Aplicar la fórmula para Indicador 6.2

df527 = df_DB.copy()

def aplicar_formula27(row):
    denominador_parte1 = row['Column143']
    denominador_parte2 = row['Column147']
    
    # Evitar la división por cero
    if denominador_parte1 == 0 or denominador_parte2 == 0:
        return 0
    
    numerador = (row['Column140'] + row['Column141'] - row['Column142']) / denominador_parte1
    denominador = (row['Column144'] + row['Column145'] - row['Column146']) / denominador_parte2
    
    resultado = ((numerador / denominador) - 1) * 100
    return 1 - resultado

df527['6.2'] = df527.apply(aplicar_formula27, axis=1)

# Normalizar la columna '4.2.1' entre 0 y 100 y eliminar decimales
df527['6.2'] = round((df527['6.2'] - df527['6.2'].min()) / (df527['6.2'].max() - df527['6.2'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df527['6.2'] = df527['6.2'].clip(0, 100)





# Aplicar la fórmula para Indicador 7.1.1

df528 = df_DB.copy()

def aplicar_formula28(row):
    numerador = row['Column39'] - row['Column148']
    denominador = row['Column148']
    
    # Evitar la división por cero
    if denominador == 0:
        return 0
    
    resultado = (numerador / denominador) * 100
    return resultado

df528['7.1.1'] = df528.apply(aplicar_formula28, axis=1)


# Normalizar la columna '2.2' entre 0 y 100 y eliminar decimales
df528['7.1.1'] = round((df528['7.1.1'] - df528['7.1.1'].min()) / (df528['7.1.1'].max() - df528['7.1.1'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df528['7.1.1'] = df528['7.1.1'].clip(0, 100)




# Aplicar la fórmula para Indicador 7.2.1
df529 = df_DB.copy()

def aplicar_formula29(row):
    numerador = row['Column42'] - row['Column149']
    denominador = row['Column149']
    
    # Evitar la división por cero
    if denominador == 0:
        return 0
    
    resultado = (numerador / denominador) * 100
    return resultado

df529['7.2.1'] = df529.apply(aplicar_formula29, axis=1)

# Normalizar la columna '7.2.1' entre 0 y 100 y eliminar decimales
df529['7.2.1'] = round((df529['7.2.1'] - df529['7.2.1'].min()) / (df529['7.2.1'].max() - df529['7.2.1'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df529['7.2.1'] = df529['7.2.1'].clip(0, 100)
    
    
    
    
    
    
    
# Aplicar la fórmula para Indicador 7.3.1
   

df530 = df_DB.copy()

def aplicar_formula30(row):
    numerador = (row['Column150'] / row['Column151'] - 1) *100
    
    return numerador

df530['7.3.1'] = df530.apply(aplicar_formula30, axis=1)


# Normalizar la columna '2.2' entre 0 y 100 y eliminar decimales
df530['7.3.1'] = round((df530['7.3.1'] - df530['7.3.1'].min()) / (df530['7.3.1'].max() - df530['7.3.1'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df530['7.3.1'] = df530['7.3.1'].clip(0, 100)




# Aplicar la fórmula para Indicador 7.3.2

df531 = df_DB.copy()

def aplicar_formula31(row):
    numerador = (row['Column152'] / row['Column153'] - 1) * 100
    
    return numerador

df531['7.3.2'] = df531.apply(aplicar_formula31, axis=1)




# Normalizar la columna '2.2' entre 0 y 100 y eliminar decimales
df531['7.3.2'] = round((df531['7.3.2'] - df531['7.3.2'].min()) / (df531['7.3.2'].max() - df531['7.3.2'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df531['7.3.2'] = df531['7.3.2'].clip(0, 100)







# Aplicar la fórmula para Indicador 7.3.3

df532 = df_DB.copy()

def aplicar_formula32(row):
    numerador = (row['Column154'] / row['Column155'] - 1) * 100
    
    return numerador

df532['7.3.3'] = df532.apply(aplicar_formula32, axis=1)


# Normalizar la columna '2.2' entre 0 y 100 y eliminar decimales
df532['7.3.3'] = round((df532['7.3.3'] - df532['7.3.3'].min()) / (df532['7.3.3'].max() - df532['7.3.3'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df532['7.3.3'] = df532['7.3.3'].clip(0, 100)






# Aplicar la fórmula para Indicador 7.3.4


df533 = df_DB.copy()

def aplicar_formula33(row):
    denominador = row['Column157']
    
    # Evitar la división por cero
    if denominador == 0:
        return 0  # Puedes ajustar esto según tus necesidades
    
    numerador = (row['Column156'] / denominador - 1) * 100
    
    return numerador

df533['7.3.4'] = df533.apply(aplicar_formula33, axis=1)

# Normalizar la columna '2.2' entre 0 y 100 y eliminar decimales
df533['7.3.4'] = round((df533['7.3.4'] - df533['7.3.4'].min()) / (df533['7.3.4'].max() - df533['7.3.4'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df533['7.3.4'] = df533['7.3.4'].clip(0, 100)






# Aplicar la fórmula para Indicador 7.4.1

df534 = df_DB.copy()

def aplicar_formula34(row):
    denominador = row['Column159']
    
    # Evitar la división por cero
    if denominador == 0:
        return 0  # Puedes ajustar esto según tus necesidades
    
    numerador = (row['Column158'] / denominador - 1) * 100
    
    return numerador

df534['7.4.1'] = df534.apply(aplicar_formula34, axis=1)

# Normalizar la columna '2.2' entre 0 y 100 y eliminar decimales
df534['7.4.1'] = round((df534['7.4.1'] - df534['7.4.1'].min()) / (df534['7.4.1'].max() - df534['7.4.1'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df534['7.4.1'] = df534['7.4.1'].clip(0, 100)














# Crear un nuevo DataFrame con las columnas deseadas Idicadores finales y estandarizacion
IC = pd.concat([
    df500.set_index('Column1')['Column2'],
    df500.set_index('Column1')['Column3'],
    df500.set_index('Column1')['1.1.1.1'],
    df501.set_index('Column1')['1.1.1.2'],
    df502.set_index('Column1')['1.1.1.3'],
    df503.set_index('Column1')['1.1.1.4'],
    df504.set_index('Column1')['1.1.1.5'],
    df505.set_index('Column1')['1.1.2.1'],
    df506.set_index('Column1')['1.1.2.2'],
    df507.set_index('Column1')['1.1.2.3'],
    df508.set_index('Column1')['1.1.2.4'],
    df509.set_index('Column1')['1.1.2.5'],
    df510.set_index('Column1')['1.2.1'],
    df511.set_index('Column1')['1.2.2'],
    df512.set_index('Column1')['2.1'],
    df513.set_index('Column1')['2.2'],
    df513_1.set_index('Column1')['2.3'],
    df514.set_index('Column1')['3.1'],
    df515.set_index('Column1')['4.1.1'],
    df516.set_index('Column1')['4.1.2'],
    df517.set_index('Column1')['4.1.3'],
    df518.set_index('Column1')['4.1.4'],
    df519.set_index('Column1')['4.2.1'],
    df520.set_index('Column1')['4.2.2'],
    df521.set_index('Column1')['4.2.3'],
    df522.set_index('Column1')['4.2.4'],
    df523.set_index('Column1')['4.2.5'],
    df524.set_index('Column1')['4.2.6'],
    df525.set_index('Column1')['5.1'],
    df526.set_index('Column1')['6.1'],
    df527.set_index('Column1')['6.2'],
    df528.set_index('Column1')['7.1.1'],
    df529.set_index('Column1')['7.2.1'],
    df530.set_index('Column1')['7.3.1'],
    df531.set_index('Column1')['7.3.2'],
    df532.set_index('Column1')['7.3.3'],
    df533.set_index('Column1')['7.3.4'],
    df534.set_index('Column1')['7.4.1'],
    
    
    
], axis=1)
















################### ----------Ponderación segunda parte--------------##############

# Ingresos por cartera de credito


df600 = df_DB.copy()

def aplicar_formula60(row):
    Resultado = row['Column14'] + row['Column15'] + row['Column16'] + row['Column17'] - row['Column19']
    
    return Resultado

df600['Ingresos_por_cartera_de_credito'] = df600.apply(aplicar_formula60, axis=1)


# Ingresos por servicios de inversion
df601 = df_DB.copy()

def aplicar_formula61(row):
    Resultado = row['Column65'] + row['Column66'] + row['Column67'] + row['Column68'] - row['Column69'] + row['Column70'] + row['Column81']
    
    return Resultado

df601['Ingresos_por_servicios_de_inversion'] = df601.apply(aplicar_formula61, axis=1)



# Ingresos por banca de divisas
df602 = df_DB.copy()

def aplicar_formula62(row):
    Resultado = row['Column101'] 
    
    return Resultado

df602['Ingresos_por_banca_de_divisas'] = df602.apply(aplicar_formula62, axis=1)

# Ingresos IEB

df603 = df_DB.copy()

def aplicar_formula63(row):
    resultado = df600.loc[row.name, 'Ingresos_por_cartera_de_credito'] + df601.loc[row.name, 'Ingresos_por_servicios_de_inversion'] + df602.loc[row.name, 'Ingresos_por_banca_de_divisas']
    return resultado

df603['Ingresos_IEB'] = df603.apply(aplicar_formula63, axis=1)



#Y1
df604 = df_DB.copy()

def aplicar_formula64(row):
    resultado = df600.loc[row.name, 'Ingresos_por_cartera_de_credito'] / df603.loc[row.name, 'Ingresos_IEB']
    return resultado * 100

df604['Y1'] = df604.apply(aplicar_formula64, axis=1)
df604['Y1'] = df604['Y1'].round()


#Y2
df605 = df_DB.copy()

def aplicar_formula65(row):
    resultado = df601.loc[row.name, 'Ingresos_por_servicios_de_inversion'] / df603.loc[row.name, 'Ingresos_IEB']
    return resultado * 100

df605['Y2'] = df605.apply(aplicar_formula65, axis=1)
df605['Y2'] = df605['Y2'].round()



#Y3
df606 = df_DB.copy()

def aplicar_formula66(row):
    resultado = df602.loc[row.name, 'Ingresos_por_banca_de_divisas'] / df603.loc[row.name, 'Ingresos_IEB']
    return resultado * 100

df606['Y3'] = df606.apply(aplicar_formula66, axis=1)
df606['Y3'] = df606['Y3'].round()




#H1
df606_1 = df_DB.copy()


def aplicar_formula66_1(row):
    resultado = df604.loc[row.name, 'Y1'] * 0.70
    return resultado 

df606_1['H1'] = df606_1.apply(aplicar_formula66_1, axis=1) 
df606_1['H1'] = df606_1['H1'].round()


#H2
df607 = df_DB.copy()


def aplicar_formula67(row):
    resultado = df605.loc[row.name, 'Y2'] * 0.70
    return resultado 

df607['H2'] = df607.apply(aplicar_formula67, axis=1) 
df607['H2'] = df607['H2'].round()


#H3
df608 = df_DB.copy()

def aplicar_formula68(row):
    resultado = df606.loc[row.name, 'Y3'] * 0.70
    return resultado 

df608['H3'] = df608.apply(aplicar_formula68, axis=1) 
df608['H3'] = df608['H3'].round()


# b-Consumo

df609 = df_DB.copy()

def aplicar_formula69(row):
    numerador = row['Column36']
    denominador = row['Column40'] + row['Column43'] + row['Column46'] + row['Column48'] + row['Column36']

    # Evitar la división por cero
    if denominador == 0:
        return 0  # Puedes ajustar esto según tus necesidades
    
    resultado = (numerador / denominador) * 100
    return resultado

df609['b-Consumo'] = df609.apply(aplicar_formula69, axis=1)
df609['b-Consumo'] = df609['b-Consumo'].round()



# b-Pymes

df610 = df_DB.copy()

def aplicar_formula70(row):
    numerador = row['Column40']
    denominador = row['Column40'] + row['Column43'] + row['Column46'] + row['Column48'] + row['Column36']

    # Evitar la división por cero
    if denominador == 0:
        return 0  # Puedes ajustar esto según tus necesidades
    
    resultado = (numerador / denominador) * 100
    return resultado

df610['b-Pymes'] = df610.apply(aplicar_formula70, axis=1)
df610['b-Pymes'] = df610['b-Pymes'].round()


# b-Empresarial

df611 = df_DB.copy()

def aplicar_formula71(row):
    numerador = row['Column43']
    denominador = row['Column40'] + row['Column43'] + row['Column46'] + row['Column48'] + row['Column36']

    # Evitar la división por cero
    if denominador == 0:
        return 0  # Puedes ajustar esto según tus necesidades
    
    resultado = (numerador / denominador) * 100
    return resultado

df611['b-Empresarial'] = df611.apply(aplicar_formula71, axis=1)
df611['b-Empresarial'] = df611['b-Empresarial'].round()




# b-Viv.medyRes

df611_1 = df_DB.copy()

def aplicar_formula71_1(row):
    numerador = row['Column46']
    denominador = row['Column40'] + row['Column43'] + row['Column46'] + row['Column48'] + row['Column36']

    # Evitar la división por cero
    if denominador == 0:
        return 0  # Puedes ajustar esto según tus necesidades
    
    resultado = (numerador / denominador) * 100
    return resultado

df611_1['b-Viv.medyRes'] = df611_1.apply(aplicar_formula71_1, axis=1)
df611_1['b-Viv.medyRes'] = df611_1['b-Viv.medyRes'].round()





# b-Viv.Int.Soc

df612 = df_DB.copy()

def aplicar_formula72(row):
    numerador = row['Column48']
    denominador = row['Column40'] + row['Column43'] + row['Column46'] + row['Column48'] + row['Column36']

    # Evitar la división por cero
    if denominador == 0:
        return 0  # Puedes ajustar esto según tus necesidades
    
    resultado = (numerador / denominador) * 100
    return resultado

df612['b-Viv.Int.Soc'] = df612.apply(aplicar_formula72, axis=1)
df612['b-Viv.Int.Soc'] = df612['b-Viv.Int.Soc'].round()




# b-Sucursales

df613 = df_DB.copy()

def aplicar_formula73(row):
    numerador = row['Column103']
    denominador = row['Column103'] + row['Column105'] + row['Column107'] + row['Column109']

    # Evitar la división por cero
    if denominador == 0:
        return 0  # Puedes ajustar esto según tus necesidades
    
    resultado = (numerador / denominador) * 100
    return resultado

df613['b-Sucursales'] = df613.apply(aplicar_formula73, axis=1)
df613['b-Sucursales'] = df613['b-Sucursales'].round()


# b-ATMs

df613_2 = df_DB.copy()

def aplicar_formula73_2(row):
    numerador = row['Column105']
    denominador = row['Column103'] + row['Column105'] + row['Column107'] + row['Column109']

    # Evitar la división por cero
    if denominador == 0:
        return 0  # Puedes ajustar esto según tus necesidades
    
    resultado = (numerador / denominador) * 100
    return resultado

df613_2['b-ATMs'] = df613_2.apply(aplicar_formula73_2, axis=1)
df613_2['b-ATMs'] = df613_2['b-ATMs'].round()


# b-TPVs

df613_3 = df_DB.copy()

def aplicar_formula73_3(row):
    numerador = row['Column107']
    denominador = row['Column103'] + row['Column105'] + row['Column107'] + row['Column109']

    # Evitar la división por cero
    if denominador == 0:
        return 0  # Puedes ajustar esto según tus necesidades
    
    resultado = (numerador / denominador) * 100
    return resultado

df613_3['b-TPVs'] = df613_3.apply(aplicar_formula73_3, axis=1)
df613_3['b-TPVs'] = df613_3['b-TPVs'].round()

# b-Corresponsales

df613_4 = df_DB.copy()

def aplicar_formula73_4(row):
    numerador = row['Column109']
    denominador = row['Column103'] + row['Column105'] + row['Column107'] + row['Column109']

    # Evitar la división por cero
    if denominador == 0:
        return 0  # Puedes ajustar esto según tus necesidades
    
    resultado = (numerador / denominador) * 100
    return resultado

df613_4['b-Corresponsales'] = df613_4.apply(aplicar_formula73_4, axis=1)
df613_4['b-Corresponsales'] = df613_4['b-Corresponsales'].round()


# c-Sucursales

df614_1 = df_DB.copy()

def aplicar_formula74_1(row):
    numerador = row['Column111']
    denominador = row['Column111'] + row['Column113'] + row['Column115'] + row['Column117'] + row['Column121'] + row['Column127']

    # Evitar la división por cero
    if denominador == 0:
        return 0  # Puedes ajustar esto según tus necesidades
    
    resultado = (numerador / denominador) * 100
    return resultado

df614_1['c-Sucursales'] = df614_1.apply(aplicar_formula74_1, axis=1)
df614_1['c-Sucursales'] = df614_1['c-Sucursales'].round()







# c-ATMs

df614 = df_DB.copy()

def aplicar_formula74(row):
    numerador = row['Column113']
    denominador = row['Column111'] + row['Column113'] + row['Column115'] + row['Column117'] + row['Column121'] + row['Column127']

    # Evitar la división por cero
    if denominador == 0:
        return 0  # Puedes ajustar esto según tus necesidades
    
    resultado = (numerador / denominador) * 100
    return resultado

df614['c-ATMs'] = df614.apply(aplicar_formula74, axis=1)
df614['c-ATMs'] = df614['c-ATMs'].round()


# c-TPVs

df615 = df_DB.copy()

def aplicar_formula75(row):
    numerador = row['Column115']
    denominador = row['Column111'] + row['Column113'] + row['Column115'] + row['Column117'] + row['Column121'] + row['Column127']

    # Evitar la división por cero
    if denominador == 0:
        return 0  # Puedes ajustar esto según tus necesidades
    
    resultado = (numerador / denominador) * 100
    return resultado

df615['c-TPVs'] = df615.apply(aplicar_formula75, axis=1)
df615['c-TPVs'] = df615['c-TPVs'].round()


# c-Comisionistas

df616 = df_DB.copy()

def aplicar_formula76(row):
    numerador = row['Column117']
    denominador = row['Column111'] + row['Column113'] + row['Column115'] + row['Column117'] + row['Column121'] + row['Column127']

    # Evitar la división por cero
    if denominador == 0:
        return 0  # Puedes ajustar esto según tus necesidades
    
    resultado = (numerador / denominador) * 100
    return resultado

df616['c-Comisionistas'] = df616.apply(aplicar_formula76, axis=1)
df616['c-Comisionistas'] = df616['c-Comisionistas'].round()




# c-BancaInternet

df617 = df_DB.copy()

def aplicar_formula77(row):
    numerador = row['Column121']
    denominador = row['Column111'] + row['Column113'] + row['Column115'] + row['Column117'] + row['Column121'] + row['Column127']

    # Evitar la división por cero
    if denominador == 0:
        return 0  # Puedes ajustar esto según tus necesidades
    
    resultado = (numerador / denominador) * 100
    return resultado

df617['c-BancaInternet'] = df617.apply(aplicar_formula77, axis=1)
df617['c-BancaInternet'] = df617['c-BancaInternet'].round()


# c-BancaMovil

df618 = df_DB.copy()

def aplicar_formula78(row):
    numerador = row['Column127']
    denominador = row['Column111'] + row['Column113'] + row['Column115'] + row['Column117'] + row['Column121'] + row['Column127']

    # Evitar la división por cero
    if denominador == 0:
        return 0  # Puedes ajustar esto según tus necesidades
    
    resultado = (numerador / denominador) * 100
    return resultado

df618['c-BancaMovil'] = df618.apply(aplicar_formula78, axis=1)
df618['c-BancaMovil'] = df618['c-BancaMovil'].round()









# Crear un nuevo DataFrame con las columnas deseadas, Ponderación Final
PON = pd.concat([
    df500.set_index('Column1')['Column2'],
    df500.set_index('Column1')['Column3'],
    df606_1.set_index('Column1')['H1'],
    df607.set_index('Column1')['H2'],
    df608.set_index('Column1')['H3'],
    df603.set_index('Column1')['Ingresos_IEB'],
    df604.set_index('Column1')['Y1'],
    df600.set_index('Column1')['Ingresos_por_cartera_de_credito'],
    df605.set_index('Column1')['Y2'],
    df601.set_index('Column1')['Ingresos_por_servicios_de_inversion'],
    df606.set_index('Column1')['Y3'],
    df602.set_index('Column1')['Ingresos_por_banca_de_divisas'],
    df609.set_index('Column1')['b-Consumo'],
    df610.set_index('Column1')['b-Pymes'],
    df611.set_index('Column1')['b-Empresarial'],
    df611_1.set_index('Column1')['b-Viv.medyRes'],
    df612.set_index('Column1')['b-Viv.Int.Soc'],
    df613.set_index('Column1')['b-Sucursales'],
    df613_2.set_index('Column1')['b-ATMs'],
    df613_3.set_index('Column1')['b-TPVs'],
    df613_4.set_index('Column1')['b-Corresponsales'],
    df614_1.set_index('Column1')['c-Sucursales'],
    df614.set_index('Column1')['c-ATMs'],
    df615.set_index('Column1')['c-TPVs'],
    df616.set_index('Column1')['c-Comisionistas'],
    df617.set_index('Column1')['c-BancaInternet'],
    df618.set_index('Column1')['c-BancaMovil'],
    
    
    
    
    
    
    
    
    
], axis=1)








##############----------Hoja ponderacion, items que faltan ---------------------------
#############-----------------------------------------------------######################




# Aplicar la fórmula para Indicador 1.1.1:

df500_2 = df_DB.copy()

def aplicar_formula_2(row):
    resultado = (
        (df606_1.loc[row.name, 'H1'] * df500.loc[row.name, '1.1.1.1']) * 0.15 +
        (df501.loc[row.name, '1.1.1.2']) * 0.15 +
        (df502.loc[row.name, '1.1.1.3']) * 0.15 +
        (df503.loc[row.name, '1.1.1.4']) * 0.15 +
        (df504.loc[row.name, '1.1.1.5']) * 0.12
    ) 
    return resultado / 100

# Aplicar la fórmula a la columna '1.'
df500_2['1.1.1'] = df500_2.apply(aplicar_formula_2, axis=1)
# Redondear utilizando leyes de aproximación
df500_2['1.1.1'] = df500_2['1.1.1'].apply(lambda x: round(x, 0) if x >= 0 else round(x, 0))





# Aplicar la fórmula para Indicador 1.1.2:

df504_2 = df_DB.copy()

def aplicar_formula_5_2(row):
    resultado = (
            (df606_1.loc[row.name, 'H1'] * 0.018) * 
            df505.loc[row.name, '1.1.2.1'] * df609.loc[row.name, 'b-Consumo'] +
            df506.loc[row.name, '1.1.2.2'] * df610.loc[row.name, 'b-Pymes'] +
            df507.loc[row.name, '1.1.2.3'] * df611.loc[row.name, 'b-Empresarial'] +
            df508.loc[row.name, '1.1.2.4'] * df611_1.loc[row.name, 'b-Viv.medyRes'] +
            df509.loc[row.name, '1.1.2.5'] * df612.loc[row.name, 'b-Viv.Int.Soc']
        
    ) 
    return resultado / 1000

# Aplicar la fórmula a la columna '1.1.2'
df504_2['1.1.2'] = df504_2.apply(aplicar_formula_5_2, axis=1)
# Redondear utilizando leyes de aproximación
df504_2['1.1.2'] = df504_2['1.1.2'].apply(lambda x: round(x, 0) if x >= 0 else round(x, 0))


# Aplicar la fórmula para Indicador 1.1

df500_22 = df_DB.copy()

def aplicar_formula_22(row):
    resultado = (
        df606_1.loc[row.name, 'H1'] * (0.72 +
        df504_2.loc[row.name, '1.1.2'] * 0.18) 
    
    )
    return resultado / 10

# Aplicar la fórmula a la columna '1.1.1'
df500_22['1.1'] = df500_2.apply(aplicar_formula_22, axis=1)

# Redondear utilizando leyes de aproximación
df500_22['1.1'] = df500_22['1.1'].apply(lambda x: round(x, 0) if x >= 0 else round(x, 0))






# Definir la función para la fórmula 1.2

df509_2 = df_DB.copy()

def aplicar_formula_10_2(row):
    resultado = (
            (df606_1.loc[row.name, 'H1'] * 0.05) * 
            (df510.loc[row.name, '1.2.1'] + df511.loc[row.name, '1.2.2'])
         
    )
    return resultado / 100

# Aplicar la fórmula a la columna '1.2'
df509_2['1.2'] = df509_2.apply(aplicar_formula_10_2, axis=1)
# Redondear utilizando leyes de aproximación
df509_2['1.2'] = df509_2['1.2'].apply(lambda x: round(x, 0) if x >= 0 else round(x, 0))







# Aplicar la fórmula para Indicador 1.

df500_11 = df_DB.copy()

def aplicar_formula_11(row):
    resultado = (
        df606_1.loc[row.name, 'H1'] * (0.72 +
        df500_22.loc[row.name, '1.1'] * 0.18 +
        df509_2.loc[row.name, '1.2'] * 0.10) 
    
    )
    return resultado / 10

# Aplicar la fórmula a la columna '1.1.1'
df500_11['1.'] = df500_11.apply(aplicar_formula_11, axis=1)

# Redondear utilizando leyes de aproximación
df500_11['1.'] = df500_11['1.'].apply(lambda x: round(x, 0) if x >= 0 else round(x, 0))



# Aplicar la fórmula para Indicador 2

df500_222 = df_DB.copy()

def aplicar_formula_222(row):
    resultado = (
        df607.loc[row.name, 'H2'] * (
        df512.loc[row.name, '2.1'] * 0.35 +
        df513.loc[row.name, '2.2'] * 0.30 +
        df513_1.loc[row.name, '2.3'] * 0.35)
    
    )
    return resultado / 100

# Aplicar la fórmula a la columna '1.1.1'
df500_222['2.'] = df500_222.apply(aplicar_formula_222, axis=1)

# Redondear utilizando leyes de aproximación
df500_222['2.'] = df500_222['2.'].apply(lambda x: round(x, 0) if x >= 0 else round(x, 0))



# Aplicar la fórmula para Indicador 3

df500_33 = df_DB.copy()

def aplicar_formula_33(row):
    resultado = (
        df514.loc[row.name, '3.1'] * 
        df608.loc[row.name, 'H3'] 
    
    )
    return resultado / 100

# Aplicar la fórmula a la columna '1.1.1'
df500_33['3.'] = df500_33.apply(aplicar_formula_33, axis=1)

# Redondear utilizando leyes de aproximación
df500_33['3.'] = df500_33['3.'].apply(lambda x: round(x, 0) if x >= 0 else round(x, 0))


# Aplicar la fórmula para Indicador 4.1

df500_44 = df_DB.copy()

def aplicar_formula_44(row):
    resultado = 0.10 * ( 
        df613.loc[row.name, 'b-Sucursales'] * 
        df515.loc[row.name, '4.1.1'] +
        df516.loc[row.name, '4.1.2'] * 
        df613_2.loc[row.name, 'b-ATMs'] +
        df613_3.loc[row.name, 'b-TPVs'] * 
        df517.loc[row.name, '4.1.3'] +
        df518.loc[row.name, '4.1.4'] *
        df613_4.loc[row.name, 'b-Corresponsales']
        
    
    )
    return resultado / 100

# Aplicar la fórmula a la columna '1.1.1'
df500_44['4.1'] = df500_44.apply(aplicar_formula_44, axis=1)

# Redondear utilizando leyes de aproximación
df500_44['4.1'] = df500_44['4.1'].apply(lambda x: round(x, 0) if x >= 0 else round(x, 0))





# Aplicar la fórmula para Indicador 4.2
df500_466 = df_DB.copy()

def aplicar_formula46(row):
    # Calcular la primera parte de la fórmula
    suma_sucursales_corresponsales = (
        df613.loc[row.name, 'b-Sucursales'] + df613_4.loc[row.name, 'b-Corresponsales']
    )
    
    if 0.1 * suma_sucursales_corresponsales == 0.1:
        valor_4_2 = 0.05
    else:
        valor_4_2 = 0.15
    
    # Calcular el resultado final
    resultado_final = valor_4_2 * (
        df519.loc[row.name, '4.2.1'] * df614_1.loc[row.name, 'c-Sucursales'] +
        df614.loc[row.name, 'c-ATMs'] * df520.loc[row.name, '4.2.2'] +
        df615.loc[row.name, 'c-TPVs'] * df521.loc[row.name, '4.2.3'] +
        df616.loc[row.name, 'c-Comisionistas'] * df522.loc[row.name, '4.2.4'] +
        df617.loc[row.name, 'c-BancaInternet'] * df523.loc[row.name, '4.2.5'] +
        df618.loc[row.name, 'c-BancaMovil'] * df524.loc[row.name, '4.2.6']
    )
    
    return resultado_final

# Aplicar la fórmula a una nueva columna 'Resultado'
df500_466['4.2'] = df500_466.apply(aplicar_formula46, axis=1)

# Normalizar la columna '4.2' entre 0 y 100 sin redondear antes
df500_466['4.2'] = ((df500_466['4.2'] - df500_466['4.2'].min()) / (df500_466['4.2'].max() - df500_466['4.2'].min())) * 100

# Asegurarse de que los valores estén en el rango correcto (0-100)
df500_466['4.2'] = df500_466['4.2'].clip(0, 100)






# Aplicar la fórmula para Indicador 4

df500_45 = df_DB.copy()
def aplicar_formula_45(row):
    # Calcular la primera parte de la fórmula
    
    parte_1 = df500_44.loc[row.name, '4.1'] * 0.1
    
    
    # Calcular la segunda parte de la fórmula
    suma_sucursales_corresponsales = (
        df613.loc[row.name, 'b-Sucursales'] + df613_4.loc[row.name, 'b-Corresponsales']
    )
    
    if 0.1 * suma_sucursales_corresponsales == 0.1:
        parte_2 = df500_466.loc[row.name, '4.2'] * 0.05
    else:
        parte_2 = df500_466.loc[row.name, '4.2'] * 0.15
    
    # Sumar las dos partes
    resultado_final = parte_1 + parte_2
    
    return resultado_final

# Aplicar la fórmula a una nueva columna '4.'
df500_45['4.'] = df500_45.apply(aplicar_formula_45, axis=1)





# Aplicar la fórmula para Indicador 5


df525_11 = df_DB.copy()


if 'Column131' in df525_11.columns:
    # Normalizar la columna 'Column131' entre 0 y 100 y eliminar decimales
    df525_11['Column131'] = round((df525_11['Column131'] - df525_11['Column131'].min()) / (df525_11['Column131'].max() - df525_11['Column131'].min()) * 100)

    # Asegurarse de que los valores estén en el rango correcto (0-100)
    df525_11['Column131'] = df525_11['Column131'].clip(0, 100)

    # Renombrar la columna a '5.1'
    df525_11 = df525_11.rename(columns={'Column131': '5.'})



# Aplicar la fórmula para Indicador 6

df500_66 = df_DB.copy()

def aplicar_formula_66(row):
    resultado = 0.5 * (
        df526.loc[row.name, '6.1'] +
        df527.loc[row.name, '6.2'] 
       
    )
    return resultado 

# Aplicar la fórmula a la columna '1.1.1'
df500_66['6.'] = df500_66.apply(aplicar_formula_66, axis=1)

# Redondear utilizando leyes de aproximación
df500_66['6.'] = df500_66['6.'].apply(lambda x: round(x, 0) if x >= 0 else round(x, 0))




# Aplicar la fórmula para Indicador 7.1


df528_70 = df_DB.copy()

def aplicar_formula70(row):
    numerador = row['Column39'] - row['Column148']
    denominador = row['Column148']
    
    # Evitar la división por cero
    if denominador == 0:
        return 0
    
    resultado = (numerador / denominador) * 100
    return resultado

df528_70['7.1'] = df528_70.apply(aplicar_formula70, axis=1)


# Normalizar la columna '2.2' entre 0 y 100 y eliminar decimales
df528_70['7.1'] = round((df528_70['7.1'] - df528_70['7.1'].min()) / (df528_70['7.1'].max() - df528_70['7.1'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df528_70['7.1'] = df528_70['7.1'].clip(0, 100)



# Aplicar la fórmula para Indicador 7.2

df528_72 = df_DB.copy()


def aplicar_formula72(row):
    numerador = row['Column42'] - row['Column149']
    denominador = row['Column149']
    
    # Evitar la división por cero
    if denominador == 0:
        return 0
    
    resultado = (numerador / denominador) * 100
    return resultado

df528_72['7.2'] = df528_72.apply(aplicar_formula72, axis=1)

# Normalizar la columna '7.2.1' entre 0 y 100 y eliminar decimales
df528_72['7.2'] = round((df528_72['7.2'] - df528_72['7.2'].min()) / (df528_72['7.2'].max() - df528_72['7.2'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df528_72['7.2'] = df528_72['7.2'].clip(0, 100)
    


# Aplicar la fórmula para Indicador 7.3


df500_73 = df_DB.copy()

def aplicar_formula_73(row):
    resultado = 0.25 * (
        df613.loc[row.name, 'b-Sucursales'] *
        df530.loc[row.name, '7.3.1'] +
        df613_2.loc[row.name, 'b-ATMs'] *
        df531.loc[row.name, '7.3.2'] +
        df613_3.loc[row.name, 'b-TPVs'] * 
        df532.loc[row.name, '7.3.3'] +
        df613_4.loc[row.name, 'b-Corresponsales'] *
        df533.loc[row.name, '7.3.4']
        
        )
    
    
    return resultado / 100

# Aplicar la fórmula a la columna '1.1.1'
df500_73['7.3'] = df500_73.apply(aplicar_formula_73, axis=1)

# Redondear utilizando leyes de aproximación
df500_73['7.3'] = df500_73['7.3'].apply(lambda x: round(x, 0) if x >= 0 else round(x, 0))







# Aplicar la fórmula para Indicador 7.4
df500_74 = df_DB.copy()

def aplicar_formula74(row):
    denominador = row['Column159']
    
    # Evitar la división por cero
    if denominador == 0:
        return 0  # Puedes ajustar esto según tus necesidades
    
    numerador = (row['Column158'] / denominador - 1) * 100
    
    return numerador

df500_74['7.4'] = df500_74.apply(aplicar_formula74, axis=1)

# Normalizar la columna '2.2' entre 0 y 100 y eliminar decimales
df500_74['7.4'] = round((df500_74['7.4'] - df500_74['7.4'].min()) / (df500_74['7.4'].max() - df500_74['7.4'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df500_74['7.4'] = df500_74['7.4'].clip(0, 100)





# Aplicar la fórmula para Indicador 7

df500_700 = df_DB.copy()

def aplicar_formula_711(row):
    resultado = (
        df528_70.loc[row.name, '7.1'] * 0.30 +
        df528_72.loc[row.name, '7.2'] * 0.30 +
        df500_73.loc[row.name, '7.3'] * 0.30 +
        df500_74.loc[row.name, '7.4'] * 0.10
    
    )
    return resultado 

# Aplicar la fórmula a la columna '1.1.1'
df500_700['7.'] = df500_700.apply(aplicar_formula_711, axis=1)

# Redondear utilizando leyes de aproximación
df500_700['7.'] = df500_700['7.'].apply(lambda x: round(x, 0) if x >= 0 else round(x, 0))





# Aplicar la fórmula para Indicador IEB

df500_111 = df_DB.copy()

def aplicar_formula_111(row):
    resultado = (
        df500_11.loc[row.name, '1.'] *
        df606_1.loc[row.name, 'H1'] +
        df500_222.loc[row.name, '2.'] *
        df607.loc[row.name, 'H2'] +
        df500_33.loc[row.name, '3.'] *
        df608.loc[row.name, 'H3'] +
        df500_45.loc[row.name, '4.'] * 0.15 +
        df525_11.loc[row.name, '5.'] * 0.05 +
        df500_66.loc[row.name, '6.'] * 0.10
        
    )
    return resultado / 10

# Aplicar la fórmula a la columna '1.1.1'
df500_111['IEB'] = df500_111.apply(aplicar_formula_111, axis=1)

# Redondear utilizando leyes de aproximación
df500_111['IEB'] = df500_111['IEB'].apply(lambda x: round(x, 0) if x >= 0 else round(x, 0))
















########## Indicadores cálculos,lo comentado es lo estandarizado. 
### Con el presente codigo consigó el valor de refenrencia 


    
# Aplicar la fórmula para Indicador 1.1.1.1: 
df500_A = df_DB.copy()

def aplicar_formula_A(row):
    resultado = ((row['Column5'] + row['Column6']) - (row['Column7'] + row['Column8'])) / row['Column4'] * 100
    return round(resultado, 2)

df500_A['1.1.1.1'] = df500_A.apply(aplicar_formula, axis=1)









# Aplicar la fórmula para Indicador 1.1.1.2: 
    
df501_A = df_DB.copy()

def aplicar_formula2_A(row):
    numerador = ((row['Column5'] + row['Column6']) - (row['Column7'] + row['Column8'])) - ((row['Column9'] + row['Column10']) - (row['Column11'] + row['Column12']))
    denominador = (row['Column9'] + row['Column10']) - (row['Column11'] + row['Column12'])
    
    if denominador == 0:
        return 0  # Evitar la división por cero, puedes ajustar esto según tus necesidades
        
    return (numerador / denominador) * 100

df501_A['1.1.1.2'] = df501_A.apply(aplicar_formula2_A, axis=1)








# Aplicar la fórmula para Indicador 1.1.1.3

df502_A = df_DB.copy()


def aplicar_formula3_A(row):
    numerador = row['Column5'] + row['Column6']
    denominador = row['Column13']
    
    if denominador == 0:
        return 0  # Evitar la división por cero, puedes ajustar esto según tus necesidades
        
    return (numerador / denominador) * 100


df502_A['1.1.1.3'] = df502_A.apply(aplicar_formula3_A, axis=1)








# Aplicar la fórmula para Indicador 1.1.1.4

df503_A = df_DB.copy()

def aplicar_formula4_A(row):
    numerador = row['Column14'] + row['Column15'] + row['Column16'] + row['Column17'] + row['Column18'] - row['Column19']
    denominador = row['Column20'] + row['Column21'] + row['Column22'] + row['Column23']
    
    if denominador == 0:
        return 0  # Evitar la división por cero, puedes ajustar esto según tus necesidades
        
    return (numerador / denominador) * 100

df503_A['1.1.1.4'] = df503_A.apply(aplicar_formula4_A, axis=1)





# Aplicar la fórmula para Indicador 1.1.1.5

df504_A = df_DB.copy()

# Aplicar la fórmula para Indicador Z
def aplicar_formula5_A(row):
    numerador = row.loc['Column24':'Column29'].sum() - row.loc['Column30':'Column35'].sum()
    denominador = row.loc['Column30':'Column35'].sum()
    
    if denominador == 0:
        return 0  # Evitar la división por cero, puedes ajustar esto según tus necesidades
        
    return (numerador / denominador) * 100

df504_A['1.1.1.5'] = df504_A.apply(aplicar_formula5_A, axis=1)












# Aplicar la fórmula para Indicador 1.1.2.1


# Copiar el DataFrame original
df505_A = df_DB.copy()

# Aplicar la fórmula para Indicador 1.1.2.1: 
def aplicar_formula6_A(row):
    numerador = row['Column36'] + row['Column37']
    denominador = row['Column38'] + row['Column37']
    
    if denominador == 0:
        return 0  # Evitar la división por cero, puedes ajustar esto según tus necesidades
    
    return (numerador / denominador) * 100

# Aplicar la fórmula a la columna '1.1.2.1'
df505_A['1.1.2.1'] = df505_A.apply(aplicar_formula6_A, axis=1)



# Aplicar la fórmula para Indicador 1.1.2.2

df506_A = df_DB.copy()


def aplicar_formula7_A(row):
    numerador = row['Column40']
    denominador = row['Column39'] + row['Column40'] + row['Column41']
    
    if denominador == 0:
        return 0  # Evitar la división por cero, puedes ajustar esto según tus necesidades
        
    return (numerador / denominador) * 100

df506_A['1.1.2.2'] = df506_A.apply(aplicar_formula7_A, axis=1)





# Aplicar la fórmula para Indicador 1.1.2.3

df507_A = df_DB.copy()


def aplicar_formula8_A(row):
    numerador = row['Column43']
    denominador = row['Column42'] + row['Column43'] + row['Column44']
    
    if denominador == 0:
        return 0  # Evitar la división por cero, puedes ajustar esto según tus necesidades
        
    return (numerador / denominador) * 100

df507_A['1.1.2.3'] = df507_A.apply(aplicar_formula8_A, axis=1)









# Aplicar la fórmula para Indicador 1.1.2.4

df508_A = df_DB.copy()

def aplicar_formula9_A(row):
    numerador = row['Column46']
    denominador = row['Column45'] + row['Column46'] + row['Column47']
    
    if denominador == 0:
        return 0  # Evitar la división por cero, puedes ajustar esto según tus necesidades
        
    return (numerador / denominador) * 100

df508_A['1.1.2.4'] = df508_A.apply(aplicar_formula9_A, axis=1)











# Aplicar la fórmula para Indicador 1.1.2.5

df509_A = df_DB.copy()

def aplicar_formula10_A(row):
    numerador = row['Column48'] + row['Column49'] + row['Column50']
    denominador = row['Column51'] + row['Column52'] + row['Column53'] + row['Column54'] + row['Column55'] + row['Column56'] + row['Column57'] + row['Column58']
    
    if denominador == 0:
        return 0  # Evitar la división por cero, puedes ajustar esto según tus necesidades
        
    return (numerador / denominador) * 100

df509_A['1.1.2.5'] = df509_A.apply(aplicar_formula10_A, axis=1)













# Aplicar la fórmula para Indicador 1.2.1

df510_A = df_DB.copy()

# Aplicar la fórmula para Indicador Z3
def aplicar_formula11_A(row):
    numerador = row['Column59']
    denominador = row['Column60']
    
    if denominador == 0:
        return 0  # Evitar la división por cero, puedes ajustar esto según tus necesidades
        
    return (numerador / denominador) * 100

df510_A['1.2.1'] = df510_A.apply(aplicar_formula11_A, axis=1)











# Aplicar la fórmula para Indicador 1.2.2

df511_A = df_DB.copy()


def aplicar_formula12_A(row):
    numerador = row['Column63'] + row['Column64']
    denominador = row['Column64']
    
    if denominador == 0:
        return 0  # Evitar la división por cero, puedes ajustar esto según tus necesidades
        
    return (numerador / denominador) * 100

df511_A['1.2.2'] = df511_A.apply(aplicar_formula12_A, axis=1)










# Aplicar la fórmula para Indicador 2.1



df512_A = df_DB.copy()

columnas_numerador = df512.loc[:, 'Column65':'Column70']
columnas_denominador = df512.loc[:, 'Column71':'Column76']

df512_A['2.1'] = (columnas_numerador.sum(axis=1) - columnas_denominador.sum(axis=1)) / np.abs(columnas_denominador.sum(axis=1)) * 100

# Manejar valores infinitos o NaN
df512_A['2.1'] = df512_A['2.1'].replace([np.inf, -np.inf], np.nan).fillna(0)













# Aplicar la fórmula para Indicador 2.2

df513_A = df_DB.copy()

def aplicar_formula14_A(row):
    numerador = (row['Column77'] + row['Column78']) - (row['Column79'] + row['Column80'])
    denominador = np.abs(row['Column79'] + row['Column80'])
    
    if denominador == 0:
        return 0  # Evitar la división por cero, puedes ajustar esto según tus necesidades
        
    return (numerador / denominador) * 100

df513_A['2.2'] = df513_A.apply(aplicar_formula14_A, axis=1)








# Aplicar la fórmula para Indicador 2.3


df513_1_A = df_DB.copy()

# Definir la función para aplicar la fórmula
def aplicar_formula14_1_A(row):
    numerador = (
        row['Column81'] - row['Column82'] - row['Column83'] -
        row['Column84'] - row['Column85'] - row['Column86'] -
        row['Column87'] - row['Column88'] - row['Column89'] -
        row['Column90']
    )
    denominador = (
        row['Column91'] - row['Column92'] - row['Column93'] -
        row['Column94'] - row['Column95'] - row['Column96'] -
        row['Column97'] - row['Column98'] - row['Column99'] -
        row['Column100']
    )
    
    if denominador == 0:
        return 0  # Evitar la división por cero, puedes ajustar esto según tus necesidades
        
    return ((numerador / denominador) - 1) * 100

# Aplicar la función a una nueva columna 'Nueva_Columna'
df513_1_A['2.3'] = df513_1_A.apply(aplicar_formula14_1_A, axis=1)








# Aplicar la fórmula para Indicador 3.1

df514_A = df_DB.copy()

def aplicar_formula15_A(row):
    numerador = row['Column101'] - row['Column102']
    denominador = np.abs(row['Column102'])
    
    if denominador == 0:
        return 0  # Evitar la división por cero, puedes ajustar esto según tus necesidades
        
    return (numerador / denominador) * 100

df514_A['3.1'] = df514_A.apply(aplicar_formula15_A, axis=1)











# Aplicar la fórmula para Indicador 4.1.1

df515_A = df_DB.copy()

def aplicar_formula16_A(row):
    denominador = row['Column104']
    
    # Evitar la división por cero
    if denominador == 0:
        return 0
    
    numerador = ((row['Column103'] / denominador) - 1) * 100
    
    return numerador


# Aplicar la fórmula y redondear hacia arriba los resultados
df515_A['4.1.1'] = df515_A.apply(aplicar_formula16_A, axis=1).apply(np.ceil)







# Aplicar la fórmula para Indicador 4.1.2

df516_A = df_DB.copy()

def aplicar_formula17_A(row):
    denominador = row['Column106']
    
    # Evitar la división por cero
    if denominador == 0:
        return 0
    
    numerador = ((row['Column105'] / denominador) - 1) * 100
    
    return numerador

df516_A['4.1.2'] = df516_A.apply(aplicar_formula17_A, axis=1) 






# Aplicar la fórmula para Indicador 4.1.3

df517_A = df_DB.copy()

def aplicar_formula18_A(row):
    denominador = row['Column107']
    
    # Evitar la división por cero
    if denominador == 0:
        return 0
    
    numerador = ((row['Column108'] / denominador) - 1) * 100
    
    return numerador

df517_A['4.1.3'] = df517_A.apply(aplicar_formula18_A, axis=1) 








# Aplicar la fórmula para Indicador 4.1.4

df518_A = df_DB.copy()

def aplicar_formula19_A(row):
    denominador = row['Column109']
    
    # Evitar la división por cero
    if denominador == 0:
        return 0
    
    numerador = ((row['Column110'] / denominador) - 1) * 100
    
    return numerador

df518_A['4.1.4'] = df518_A.apply(aplicar_formula19_A, axis=1) 









# Aplicar la fórmula para Indicador 4.2.1

df519_A = df_DB.copy()

def aplicar_formula20_A(row):
    denominador = row['Column111']
    
    # Evitar la división por cero
    if denominador == 0:
        return 0
    
    numerador = ((row['Column112'] / denominador) - 1) * 100
    
    return numerador

df519_A['4.2.1'] = df519_A.apply(aplicar_formula20_A, axis=1) 









# Aplicar la fórmula para Indicador 4.2.2

df520_A = df_DB.copy()

def aplicar_formula21_A(row):
    denominador = row['Column113']
    
    # Evitar la división por cero
    if denominador == 0:
        return 0
    
    numerador = ((row['Column114'] / denominador) - 1) * 100
    
    return numerador

df520_A['4.2.2'] = df520_A.apply(aplicar_formula21_A, axis=1) 





# Aplicar la fórmula para Indicador 4.2.3

df521_A = df_DB.copy()

def aplicar_formula22_A(row):
    denominador = row['Column115']
    
    # Evitar la división por cero
    if denominador == 0:
        return 0
    
    numerador = ((row['Column116'] / denominador) - 1) * 100
    
    return numerador

df521_A['4.2.3'] = df521_A.apply(aplicar_formula22_A, axis=1) 









# Aplicar la fórmula para Indicador 4.2.4

df522_A = df_DB.copy()

def aplicar_formula23_A(row):
    denominador = row['Column117']
    
    # Evitar la división por cero
    if denominador == 0:
        return 0
    
    numerador = ((row['Column118'] / denominador) - 1) * 100
    
    return numerador

df522_A['4.2.4'] = df522_A.apply(aplicar_formula23_A, axis=1) 






# Aplicar la fórmula para Indicador 4.2.5

df523_A = df_DB.copy()

def aplicar_formula24_A(row):
    denominador = row['Column121']
    
    # Evitar la división por cero
    if denominador == 0:
        return 0
    
    numerador = (((row['Column124'] / denominador) - 1) * 100)
    
    return numerador

df523_A['4.2.5'] = df523_A.apply(aplicar_formula24_A, axis=1) 





# Aplicar la fórmula para Indicador 4.2.6

df524_A = df_DB.copy()

def aplicar_formula25_A(row):
    denominador = row['Column127']
    
    # Evitar la división por cero
    if denominador == 0:
        return 0
    
    numerador = (((row['Column130'] / denominador) - 1) * 100)
    
    return numerador

df524_A['4.2.6'] = df524_A.apply(aplicar_formula25_A, axis=1) 


# Aplicar la fórmula para Indicador 6.1

df526_A = df_DB.copy()

def aplicar_formula26_A(row):
    denominador_parte1 = row['Column135']
    denominador_parte2 = row['Column139']
    
    # Evitar la división por cero
    if denominador_parte1 == 0 or denominador_parte2 == 0:
        return 0
    
    numerador = (row['Column132'] + row['Column133'] - row['Column134']) / denominador_parte1
    denominador = (row['Column136'] + row['Column137'] - row['Column138']) / denominador_parte2
    
    resultado = ((numerador / denominador) - 1) * 100
    return resultado

df526_A['6.1'] = df526_A.apply(aplicar_formula26_A, axis=1)







# Aplicar la fórmula para Indicador 6.2

df527_A = df_DB.copy()

def aplicar_formula27_A(row):
    denominador_parte1 = row['Column143']
    denominador_parte2 = row['Column147']
    
    # Evitar la división por cero
    if denominador_parte1 == 0 or denominador_parte2 == 0:
        return 0
    
    numerador = (row['Column140'] + row['Column141'] - row['Column142']) / denominador_parte1
    denominador = (row['Column144'] + row['Column145'] - row['Column146']) / denominador_parte2
    
    resultado = ((numerador / denominador) - 1) * 100
    return resultado

df527_A['6.2'] = df527_A.apply(aplicar_formula27_A, axis=1)






# Aplicar la fórmula para Indicador 7.1.1

df528_A = df_DB.copy()

def aplicar_formula28_A(row):
    numerador = row['Column39'] - row['Column148']
    denominador = row['Column148']
    
    # Evitar la división por cero
    if denominador == 0:
        return 0
    
    resultado = (numerador / denominador) * 100
    return resultado

df528_A['7.1.1'] = df528_A.apply(aplicar_formula28_A, axis=1)







# Aplicar la fórmula para Indicador 7.2.1

df529_A = df_DB.copy()

def aplicar_formula29_A(row):
    numerador = row['Column42'] - row['Column149']
    denominador = row['Column149']
    
    # Evitar la división por cero
    if denominador == 0:
        return 0
    
    resultado = (numerador / denominador) * 100
    return resultado

df529_A['7.2.1'] = df529_A.apply(aplicar_formula29_A, axis=1)




    
    
    
    
    
# Aplicar la fórmula para Indicador 7.3.1
 
df530_A = df_DB.copy()

def aplicar_formula30_A(row):
    numerador = (row['Column150'] / row['Column151'] - 1) *100
    
    return numerador

df530_A['7.3.1'] = df530_A.apply(aplicar_formula30_A, axis=1)



# Aplicar la fórmula para Indicador 7.3.2

df531_A = df_DB.copy()

def aplicar_formula31_A(row):
    numerador = (row['Column152'] / row['Column153'] - 1) * 100
    
    return numerador

df531_A['7.3.2'] = df531_A.apply(aplicar_formula31_A, axis=1)







# Aplicar la fórmula para Indicador 7.3.3

df532_A = df_DB.copy()

def aplicar_formula32_A(row):
    numerador = (row['Column154'] / row['Column155'] - 1) * 100
    
    return numerador

df532_A['7.3.3'] = df532_A.apply(aplicar_formula32_A, axis=1)










# Aplicar la fórmula para Indicador 7.3.4

df533_A = df_DB.copy()

def aplicar_formula33_A(row):
    denominador = row['Column157']
    
    # Evitar la división por cero
    if denominador == 0:
        return 0  # Puedes ajustar esto según tus necesidades
    
    numerador = (row['Column156'] / denominador - 1) * 100
    
    return numerador

df533_A['7.3.4'] = df533_A.apply(aplicar_formula33_A, axis=1)


# Aplicar la fórmula para Indicador 7.4.1

df534_A = df_DB.copy()

def aplicar_formula34_A(row):
    denominador = row['Column159']
    
    # Evitar la división por cero
    if denominador == 0:
        return 0  # Puedes ajustar esto según tus necesidades
    
    numerador = (row['Column158'] / denominador - 1) * 100
    
    return numerador

df534_A['7.4.1'] = df534_A.apply(aplicar_formula34_A, axis=1)



# Crear un nuevo DataFrame con las columnas deseadas antes de Estandarizar
IC_1 = pd.concat([
    df500.set_index('Column1')['Column2'],
    df500.set_index('Column1')['Column3'],
    df500_A.set_index('Column1')['1.1.1.1'],
    df501_A.set_index('Column1')['1.1.1.2'],
    df502_A.set_index('Column1')['1.1.1.3'],
    df503_A.set_index('Column1')['1.1.1.4'],
    df504_A.set_index('Column1')['1.1.1.5'],
    df505.set_index('Column1')['1.1.2.1'],
    df506.set_index('Column1')['1.1.2.2'],
    df507.set_index('Column1')['1.1.2.3'],
    df508.set_index('Column1')['1.1.2.4'],
    df509.set_index('Column1')['1.1.2.5'],
    df510_A.set_index('Column1')['1.2.1'],
    df511_A.set_index('Column1')['1.2.2'],
    df512_A.set_index('Column1')['2.1'],
    df513_A.set_index('Column1')['2.2'],
    df513_1_A.set_index('Column1')['2.3'],
    df514_A.set_index('Column1')['3.1'],
    df515_A.set_index('Column1')['4.1.1'],
    df516_A.set_index('Column1')['4.1.2'],
    df517_A.set_index('Column1')['4.1.3'],
    df518_A.set_index('Column1')['4.1.4'],
    df519_A.set_index('Column1')['4.2.1'],
    df520_A.set_index('Column1')['4.2.2'],
    df521_A.set_index('Column1')['4.2.3'],
    df522_A.set_index('Column1')['4.2.4'],
    df523_A.set_index('Column1')['4.2.5'],
    df524_A.set_index('Column1')['4.2.6'],
    df526_A.set_index('Column1')['6.1'],
    df527_A.set_index('Column1')['6.2'],
    df528_A.set_index('Column1')['7.1.1'],
    df529_A.set_index('Column1')['7.2.1'],
    df530_A.set_index('Column1')['7.3.1'],
    df531_A.set_index('Column1')['7.3.2'],
    df532_A.set_index('Column1')['7.3.3'],
    df533_A.set_index('Column1')['7.3.4'],
    df534_A.set_index('Column1')['7.4.1'],
    
    
    
], axis=1)











# Definir la función para calcular la media acotada
def calcular_media_acotada(columna):
    porcentaje = 0.05  # 5%
    
    # Filtrar los valores no nulos y no NaN
    valores_no_nulos = columna.dropna()

    if len(valores_no_nulos) > 0:
        # Filtrar los valores diferentes de cero y no NaN
        valores_no_cero = valores_no_nulos[valores_no_nulos != 0]
        
        if len(valores_no_cero) > 0:
            # Verificar si todos los valores son numéricos
            if np.issubdtype(valores_no_cero, np.number):
                media_acotada = np.mean(np.sort(valores_no_cero)[:int(len(valores_no_cero) * (1 - porcentaje))])

                # Verificar si la media acotada es finita antes de redondear
                if np.isfinite(media_acotada):
                    return round(media_acotada, 5)
                else:
                    return 0
            else:
                return 0  # Si hay valores no numéricos, devolver cero
        else:
            return 0  # Si todos los valores son cero, devolver cero
    else:
        return 0  # Si no hay valores no nulos, devolver cero

# Iterar sobre todas las columnas de IC
for columna in IC_1.columns:
    # Verificar si la columna no es la columna de índice
    if columna != IC_1.index.name:
        # Calcular la media acotada y agregar la fila "Valor de referencia"
        IC_1.loc["Valor de referencia", columna] = calcular_media_acotada(IC_1[columna])




# Crear un nuevo DataFrame agragando los indicadores faltantes de la hoja Ponderación
IC = pd.concat([
    df500.set_index('Column1')['Column2'],
    df500.set_index('Column1')['Column3'],
    df500_111.set_index('Column1')['IEB'],
    df500_11.set_index('Column1')['1.'],
    df500_22.set_index('Column1')['1.1'],
    df500_2.set_index('Column1')['1.1.1'],
    df504_2.set_index('Column1')['1.1.2'],
    df509_2.set_index('Column1')['1.2'],
    df500_222.set_index('Column1')['2.'],
    df500_33.set_index('Column1')['3.'],
    df500_44.set_index('Column1')['4.1'],
    df500_466.set_index('Column1')['4.2'],
    df525_11.set_index('Column1')['5.'],
    df500_66.set_index('Column1')['6.'],
    df500_700.set_index('Column1')['7.'],
    df528_70.set_index('Column1')['7.1'],
    df528_72.set_index('Column1')['7.2'],
    df500_73.set_index('Column1')['7.3'],
    df500_74.set_index('Column1')['7.4'],
    df606_1.set_index('Column1')['H1'],
    df607.set_index('Column1')['H2'],
    df608.set_index('Column1')['H3'],
    df603.set_index('Column1')['Ingresos_IEB'],
    df604.set_index('Column1')['Y1'],
    df600.set_index('Column1')['Ingresos_por_cartera_de_credito'],
    df605.set_index('Column1')['Y2'],
    df601.set_index('Column1')['Ingresos_por_servicios_de_inversion'],
    df606.set_index('Column1')['Y3'],
    df602.set_index('Column1')['Ingresos_por_banca_de_divisas'],
    df609.set_index('Column1')['b-Consumo'],
    df610.set_index('Column1')['b-Pymes'],
    df611.set_index('Column1')['b-Empresarial'],
    df611_1.set_index('Column1')['b-Viv.medyRes'],
    df612.set_index('Column1')['b-Viv.Int.Soc'],
    df613.set_index('Column1')['b-Sucursales'],
    df613_2.set_index('Column1')['b-ATMs'],
    df613_3.set_index('Column1')['b-TPVs'],
    df613_4.set_index('Column1')['b-Corresponsales'],
    df614_1.set_index('Column1')['c-Sucursales'],
    df614.set_index('Column1')['c-ATMs'],
    df615.set_index('Column1')['c-TPVs'],
    df616.set_index('Column1')['c-Comisionistas'],
    df617.set_index('Column1')['c-BancaInternet'],
    df618.set_index('Column1')['c-BancaMovil'],
    
    
    
    
], axis=1)





# Iterar sobre todas las columnas de IC
for columna in IC.columns:
    # Verificar si la columna no es la columna de índice
    if columna != IC.index.name:
        # Calcular la media acotada y agregar la fila "Valor de referencia"
        IC.loc["Valor de referencia", columna] = calcular_media_acotada(IC[columna])







IC_final = pd.merge(IC, IC_1, on=['Column1', 'Column2', 'Column3'], how='inner')




# Definir la función para calcular la media acotada
def calcular_media_acotada(columna):
    porcentaje = 0.05  # 5%

    # Filtrar los valores no nulos y no NaN
    valores_no_nulos = columna.dropna()

    if len(valores_no_nulos) > 0:
        # Filtrar los valores diferentes de cero y no NaN
        valores_no_cero = valores_no_nulos[valores_no_nulos != 0]

        if len(valores_no_cero) > 0:
            # Verificar si todos los valores son numéricos
            if valores_no_cero.apply(lambda x: pd.to_numeric(x, errors='coerce')).notna().all():
                valores_numericos = pd.to_numeric(valores_no_cero, errors='coerce')
                media_acotada = np.mean(np.sort(valores_numericos)[:int(len(valores_numericos) * (1 - porcentaje))])

                # Verificar si la media acotada es finita antes de redondear
                if np.isfinite(media_acotada):
                    return round(media_acotada, 5)
                else:
                    return 0
            else:
                # Si hay valores no numéricos, devolver el primer valor no numérico encontrado
                return valores_no_cero.iloc[0]
        else:
            return 0  # Si todos los valores son cero, devolver cero
    else:
        return 0  # Si no hay valores no nulos, devolver cero



# Excluir las columnas que no se deben normalizar
columnas_excluidas = [
    "Column1", "Column2", "Column3", "1.", "1.1", "1.1.1", "1.1.2", "1.2", "2.", "3.", "4.1", "4.2",
    "5.", "6.", "7.", "7.1", "7.2", "7.4", "H1", "H2", "H3", "Ingresos_IEB", "Y1",
    "Ingresos_por_cartera_de_credito", "Y2", "Ingresos_por_servicios_de_inversion", "Y3",
    "Ingresos_por_banca_de_divisas", "b-Consumo", "b-Pymes", "b-Empresarial",
    "b-Viv.medyRes", "b-Viv.Int.Soc", "b-Sucursales", "b-ATMs", "b-TPVs", "b-Corresponsales",
    "c-Sucursales", "c-ATMs", "c-TPVs", "c-Comisionistas", "c-BancaInternet", "c-BancaMovil"
]

columnas_a_normalizar = [col for col in IC_final.columns if col not in columnas_excluidas]
# Convertir las columnas a normalizar a valores numéricos
IC_final[columnas_a_normalizar] = IC_final[columnas_a_normalizar].apply(pd.to_numeric, errors='coerce')

# Normalizar las columnas seleccionadas de 'IC' entre 0 y 100 y eliminar decimales
for columna in columnas_a_normalizar:
    IC_final[columna] = round((IC_final[columna] - IC_final[columna].min()) / (IC_final[columna].max() - IC_final[columna].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
IC_final[columnas_a_normalizar] = IC_final[columnas_a_normalizar].clip(0, 100)











#######################################Calificación final 


#Valor de referencia
df800_A = IC_final.copy()

# Multiplicar la celda específica por 0.10
df800_A.loc['Valor de referencia', 'IEB'] *= 10






# Calificación (0-10)
df801_A = df_DB.copy()

def aplicar_formula801_A(row):
    ieb =  df800_A.loc['Valor de referencia', 'IEB']
    c52 = df500_111.loc[row.name, 'IEB']

    try:
        resultado = min(((ieb * 10) * 6) / c52, 10)
    except ZeroDivisionError:
        resultado = 0
    
    return resultado

df801_A ['Calificación (0-10)'] = df801_A.apply(aplicar_formula801_A, axis=1)


# Punto extra (0-1)
df802_A = df_DB.copy()

def aplicar_formula802_A(row):
    valor_columna_7 = df500_700.loc[row.name, '7.']
    c53 = df500_111.loc[row.name, 'IEB']

    try:
        resultado = min((valor_columna_7 * 6) / c53, 1, 0)
    except ZeroDivisionError:
        resultado = 0
    
    return resultado

df802_A['Punto extra (0-1)'] = df802_A.apply(aplicar_formula802_A, axis=1)




# Calificación final (0-10)
df803_A = df_DB.copy()

def aplicar_formula803_A(row):
    calificacion_0_10 = df801_A.loc[row.name, 'Calificación (0-10)']
    punto_extra_0_1 = df802_A.loc[row.name, 'Punto extra (0-1)']

    resultado = min(calificacion_0_10 + punto_extra_0_1, 10)
    return resultado

df803_A['Calificación final (0-10)'] = df803_A.apply(aplicar_formula803_A, axis=1)




# Crear un nuevo DataFrame Calificación final
CI = pd.concat([
    df500.set_index('Column1')['Column2'],
    df500.set_index('Column1')['Column3'],
    df801_A.set_index('Column1')['Calificación (0-10)'],
    df802_A.set_index('Column1')['Punto extra (0-1)'],
    df803_A.set_index('Column1')['Calificación final (0-10)'],
], axis=1)





# Guardar el DataFrame concatenado en un archivo Excel hoja Ponderación 
IC_final.to_excel(r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\MergeTotal\Ponderacion.xlsx", sheet_name='pag', engine = 'openpyxl')


# Guardar el DataFrame concatenado en un archivo Excel hoja Calificación final 
CI.to_excel(r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\MergeTotal\CalificacionFINAL.xlsx", sheet_name='pag', engine = 'openpyxl')
