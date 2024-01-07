import pandas as pd
import csv
import numpy as np



from Indicador_1 import Indicador_1
from Indicador_2 import Indicador_2
from Indicador_3 import Indicador_3
from Indicador_4 import Indicador_4
from Indicador_5 import Indicador_5
from Indicador_1_1 import Indicador_1_1
from Indicador_1_2 import Indicador_1_2
from Indicador_1_3 import Indicador_1_3
from Indicador_1_4 import Indicador_1_4
from Indicador_1_5 import Indicador_1_5
from Indicador_2_1 import Indicador_2_1
from Indicador_2_2 import Indicador_2_2
from Indicador_2_3 import Indicador_2_3
from Indicador_2_4 import Indicador_2_4
from Indicador_2_5 import Indicador_2_5
from Indicador_2_6 import Indicador_2_6
from Indicador_2_7 import Indicador_2_7
from Indicador_2_8 import Indicador_2_8
from Indicador_2_9 import Indicador_2_9
from Indicador_3_1 import Indicador_3_1
from Indicador_4_1 import Indicador_4_1
from Indicador_5_1 import Indicador_5_1
from Indicador_6_1 import Indicador_6_1
from Indicador_7_1 import Indicador_7_1
from Indicador_8_1 import Indicador_8_1
from Indicador_9_1 import Indicador_9_1
from Indicador_10_1 import Indicador_10_1
from Indicador_10_2 import Indicador_10_2
from Indicador_10_3 import Indicador_10_3
from Indicador_10_4 import Indicador_10_4
from Indicador_10_5 import Indicador_10_5
from Indicador_11_1 import Indicador_11_1
from Indicador_11_2 import Indicador_11_2
from Indicador_11_3 import Indicador_11_3
from Indicador_11_4 import Indicador_11_4
from Indicador_11_5 import Indicador_11_5
from Indicador_11_6 import Indicador_11_6
from Indicador_11_7 import Indicador_11_7
from Indicador_12_1 import Indicador_12_1
from Indicador_13_1 import Indicador_13_1
from Indicador_13_2 import Indicador_13_2
from Indicador_13_3 import Indicador_13_3
from Indicador_13_4 import Indicador_13_4
from Indicador_13_5 import Indicador_13_5
from Indicador_13_6 import Indicador_13_6
from Indicador_13_7 import Indicador_13_7
from Indicador_13_8 import Indicador_13_8
from Indicador_13_9 import Indicador_13_9
from Indicador_13_10 import Indicador_13_10
from Indicador_13_11 import Indicador_13_11
from Indicador_13_12 import Indicador_13_12
from Indicador_13_13 import Indicador_13_13
from Indicador_13_14 import Indicador_13_14
from Indicador_14_1 import Indicador_14_1
from Indicador_14_2 import Indicador_14_2
from Indicador_15_1 import Indicador_15_1
from Indicador_15_2 import Indicador_15_2
from Indicador_15_3 import Indicador_15_3
from Indicador_15_4 import Indicador_15_4
from Indicador_15_5 import Indicador_15_5
from Indicador_15_6 import Indicador_15_6
from Indicador_16_1 import Indicador_16_1
from Indicador_16_2 import Indicador_16_2
from Indicador_16_3 import Indicador_16_3
from Indicador_16_4 import Indicador_16_4
from Indicador_16_5 import Indicador_16_5
from Indicador_17_1 import Indicador_17_1
from Indicador_17_1 import Indicador_17_1
from Indicador_17_3 import Indicador_17_3
from Indicador_17_4 import Indicador_17_4
from Indicador_17_5 import Indicador_17_5
from Indicador_17_6 import Indicador_17_6
from Indicador_17_7 import Indicador_17_7
from Indicador_17_8 import Indicador_17_8
from Indicador_17_9 import Indicador_17_9
from Indicador_17_10 import Indicador_17_10
from Indicador_17_11 import Indicador_17_11
from Indicador_17_12 import Indicador_17_12
from Indicador_17_13 import Indicador_17_13
from Indicador_18_1 import Indicador_18_1
from Indicador_18_2 import Indicador_18_2
from Indicador_18_3 import Indicador_18_3
from Indicador_18_4 import Indicador_18_4
from Indicador_18_5 import Indicador_18_5
from Indicador_18_6 import Indicador_18_6
from Indicador_18_7 import Indicador_18_7
from Indicador_18_8 import Indicador_18_8
from Indicador_18_9 import Indicador_18_9
from Indicador_18_10 import Indicador_18_10
from Indicador_18_11 import Indicador_18_11
from Indicador_18_12 import Indicador_18_12
from Indicador_19_1 import Indicador_19_1
from Indicador_19_2 import Indicador_19_2
from Indicador_19_3 import Indicador_19_3
from Indicador_19_4 import Indicador_19_4
from Indicador_19_5 import Indicador_19_5
from Indicador_19_6 import Indicador_19_6
from Indicador_19_7 import Indicador_19_7
from Indicador_19_8 import Indicador_19_8
from Indicador_20_1 import Indicador_20_1
from Indicador_20_2 import Indicador_20_2
from Indicador_20_3 import Indicador_20_3
from Indicador_20_4 import Indicador_20_4
from Indicador_20_5 import Indicador_20_5
from Indicador_20_6 import Indicador_20_6
from Indicador_20_7 import Indicador_20_7
from Indicador_20_8 import Indicador_20_8
from Indicador_20_9 import Indicador_20_9
from Indicador_20_10 import Indicador_20_10
from Indicador_20_11 import Indicador_20_11
from Indicador_20_12 import Indicador_20_12
from Indicador_21_1 import Indicador_21_1
from Indicador_21_2 import Indicador_21_2
from Indicador_21_3 import Indicador_21_3
from Indicador_21_4 import Indicador_21_4














# Ruta al archivo Excel en tu PC para indicadores hoja BD
ruta_archivo_excel1 = r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\Reportes\040_R12A_1219_133.xlsx"
ruta_archivo_excel2 = r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\Reportes\040_R12A_1220_133.xlsx"
ruta_archivo_excel3 = r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\Reportes\040_13A_R3B_Vivienda_2022.xlsx"
ruta_archivo_excel4 = r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\Reportes\040_30B_R2_Nómina.xlsx"
ruta_archivo_excel5 = r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\Reportes\040_31B_R2_Automotriz.xlsx"
ruta_archivo_excel6 = r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\Reportes\040_32B_R2_ABCD.xlsx"
ruta_archivo_excel7 = r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\Reportes\040_33B_R2_Personales.xlsx"
ruta_archivo_excel8 = r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\Reportes\040-11A_2022_Empresas_2022.xlsx"
ruta_archivo_excel9 = r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\Reportes\040_11V_Empresas_2022.xlsx"
ruta_archivo_excel10 = r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\Reportes\040_4A_R12_2022.xlsx"
ruta_archivo_excel11 = r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\Reportes\2441 SISECO\(Información General sobre el uso de Servicios Financieros)_202212.xlsx"
ruta_archivo_excel12_0 = r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\Reportes\Riesgo Operacional SISECO\R28-A2811(2022).xlsx"
ruta_archivo_excel12_1 = r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\Reportes\Riesgo Operacional SISECO\R28-A2811(2021_1).xlsx"
ruta_archivo_excel12_2 = r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\Reportes\Riesgo Operacional SISECO\R28-A2811(2021_2).xlsx"
ruta_archivo_excel12_3 = r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\Reportes\Riesgo Operacional SISECO\R28-A2811(2021_3).xlsx"

#Ruta archivo BD para Indicadores Cálculos
ruta_archivo_excel50 = r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\MergeTotal\MergeTotalF.xlsx"



#ruta_archivo_excel6 = r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\Reportes\040_30B_R2_Nómina.xlsx"
#ruta_archivo_excel8 = r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\Reportes\040_32B_R2_ABCD.xlsx"
#ruta_archivo_excel9 = r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\Reportes\040_33B_R2_Personales.xlsx"






# Nombre de las hojas que deseas cargar del archivo 040_R12A_1219_133.xlsx
hoja1 = '040_R12A_1219_133'
hoja2 = 'catalogo_instituciones_BM'
# Nombre de las hojas que deseas cargar del archivo 040_R12A_1220_133.xlsx
hoja2_1 = '040_R12A_1220_133'
# Nombre de las hojas que deseas cargar del archivo 040_11A_2022_vivienda_2022.xlsx
hoja3_1 = 'Hoja3_1'
# Nombre de las hojas que deseas cargar del archivo 040_30B_R2_Nómina.xlsx
hoja4_1 = 'Hoja4_1'
# Nombre de las hojas que deseas cargar del archivo 040_30B_R2_Automotriz.xlsx
hoja5_1 = 'Hoja5_1'
# Nombre de las hojas que deseas cargar del archivo 040_32B_R2_ABCD.xlsx
hoja6_1 = 'Hoja6_1'
# Nombre de las hojas que deseas cargar del archivo 040_33B_R2_Personales.xlsx
hoja7_1 = 'Hoja7_1'
# Nombre de las hojas que deseas cargar del archivo MD2_Emp_PETOT.InformacionGenera // 040-11A_2022_Empresas_2022
hoja8_1 = 'MD2_Emp_PETOT.InformacionGenera'
#  Nombre de las hojas que deseas cargar del archivo 040-11V_2022_Empresas_2022.xlsx
hoja9_1 = 'Tamaño de empresa lugar de otor'
#  Nombre de las hojas que deseas cargar del archivo 040_4A_R12_2022.xlsx
hoja10_1 = 'No_contratos'
#  Nombre de las hojas que deseas cargar del archivo [Información General sobre el uso de Servicios Financieros]_202212.txt
hoja11_1 = '(Información General sobre el u'
#  Nombre de las hojas que deseas cargar del archivo [Información General sobre el uso de Servicios R28-A 2811 (2022).xlsx
hoja12_0 = 'R28-A2811(2022)'
#  Nombre de las hojas que deseas cargar del archivo [Información General sobre el uso de Servicios R28-A 2811 (2021_1)).xlsx
hoja12_1 = 'R28-A2811(2021_1)'
#  Nombre de las hojas que deseas cargar del archivo [Información General sobre el uso de Servicios R28-A 2811 (2021_2)).xlsx
hoja12_2 = 'R28-A2811(2021_2)'
#  Nombre de las hojas que deseas cargar del archivo [Información General sobre el uso de Servicios R28-A 2811 (2021_3).xlsx
hoja12_3 = 'R28-A2811(2021_3)'


#-...................... Hoja Indicadores Cálculos
#  Nombre de las hojas que deseas cargar del archivo MergeTotalF.xlsx
hoja50 = 'MergeTotalF'





# Cargar el archivo Excel en DataFrames de pandas
df_hoja1 = pd.read_excel(ruta_archivo_excel1, sheet_name=hoja1)
df_hoja2 = pd.read_excel(ruta_archivo_excel1, sheet_name=hoja2)
df_hoja2_1 = pd.read_excel(ruta_archivo_excel2, sheet_name=hoja2_1)
df_hoja3_1 = pd.read_excel(ruta_archivo_excel3, sheet_name=hoja3_1)
df_hoja4_1 = pd.read_excel(ruta_archivo_excel4, sheet_name=hoja4_1)
df_hoja5_1 = pd.read_excel(ruta_archivo_excel5, sheet_name=hoja5_1)
df_hoja6_1 = pd.read_excel(ruta_archivo_excel6, sheet_name=hoja6_1)
df_hoja7_1 = pd.read_excel(ruta_archivo_excel7, sheet_name=hoja7_1)
df_hoja8_1 = pd.read_excel(ruta_archivo_excel8, sheet_name=hoja8_1)
df_hoja9_1 = pd.read_excel(ruta_archivo_excel9, sheet_name=hoja9_1)
df_hoja10_1 = pd.read_excel(ruta_archivo_excel10, sheet_name=hoja10_1)

df_hoja11_1 = pd.read_excel(ruta_archivo_excel11, sheet_name=hoja11_1, header=None)
# Elimina la primera fila del DataFrame y resetea los índices
df_hoja11_1 = df_hoja11_1.iloc[0:].reset_index(drop=True)
# Usa la segunda fila como encabezado de las columnas
df_hoja11_1.columns = df_hoja11_1.iloc[0]
# Elimina la segunda fila, ya que ahora es el encabezado
df_hoja11_1 = df_hoja11_1.iloc[1:]


'''
#Asigna nombres de columnas de forma creciente
nombres_columnas13 = [f'Column{i+1}' for i in range(df_hoja12_0.shape[1])]
df_hoja12_0.columns = nombres_columnas13
'''
df_hoja12_0 = pd.read_excel(ruta_archivo_excel12_0, sheet_name=hoja12_0)
# Intercambiar los datos de las columnas "Column11" y "Column10"
df_hoja12_0['Column11'], df_hoja12_0['Column10'] = df_hoja12_0['Column10'].copy(), df_hoja12_0['Column11'].copy()


df_hoja12_1 = pd.read_excel(ruta_archivo_excel12_1, sheet_name=hoja12_1)
df_hoja12_2 = pd.read_excel(ruta_archivo_excel12_2, sheet_name=hoja12_2)
df_hoja12_3 = pd.read_excel(ruta_archivo_excel12_3, sheet_name=hoja12_3)



#...........Cargar el archivo Excel MergeTotalF en DataFrames de pandas
df_DB = pd.read_excel(ruta_archivo_excel50, sheet_name=hoja50)
nombres_columnas50 = [f'Column{i+1}' for i in range(df_DB.shape[1])]
df_DB.columns = nombres_columnas50



#df_hoja12_1 = pd.read_excel(ruta_archivo_excel12_1, sheet_name=hoja12_1)
# Selecciona solo las columnas deseadas
#columnas_deseadas = ["Column1", "Column2", "Column3", "Column10", "Column12"]
#df_hoja12_1 = df_hoja12_1[columnas_deseadas]




#df_hoja12_2 = pd.read_excel(ruta_archivo_excel12_2, sheet_name=hoja12_2, header=None)
# Asigna nombres de columnas de forma creciente
#nombres_columnas13 = [f'Column{i+1}' for i in range(df_hoja12_2.shape[1])]
#df_hoja12_2.columns = nombres_columnas13
# Selecciona solo las columnas deseadas
#columnas_deseadas = ["Column1", "Column2", "Column3", "Column10", "Column12"]
#df_hoja12_2 = df_hoja12_2[columnas_deseadas]








# Llama a la función de los archivos: Archivo_1, Archivo_2... Acricho_N
df_combinado1 = Indicador_1(df_hoja1, df_hoja2)
df_combinado2 = Indicador_2(df_hoja1, df_hoja2)
df_combinado3 = Indicador_3(df_hoja1, df_hoja2)
df_combinado4 = Indicador_4(df_hoja1, df_hoja2)
df_combinado5 = Indicador_5(df_hoja1, df_hoja2)
df_combinado6 = Indicador_1_1(df_hoja1, df_hoja2)
df_combinado7 = Indicador_1_2(df_hoja1, df_hoja2)
df_combinado8 = Indicador_1_3(df_hoja1, df_hoja2)
df_combinado9 = Indicador_1_4(df_hoja1, df_hoja2)
df_combinado10 = Indicador_1_5(df_hoja1, df_hoja2)
df_combinado11 = Indicador_2_1(df_hoja2_1, df_hoja2)
df_combinado12 = Indicador_2_2(df_hoja2_1, df_hoja2)
df_combinado13 = Indicador_2_3(df_hoja2_1, df_hoja2)
df_combinado14 = Indicador_2_4(df_hoja2_1, df_hoja2)
df_combinado15 = Indicador_2_5(df_hoja2_1, df_hoja2)
df_combinado16 = Indicador_2_6(df_hoja2_1, df_hoja2)
df_combinado17 = Indicador_2_7(df_hoja2_1, df_hoja2)
df_combinado18 = Indicador_2_8(df_hoja2_1, df_hoja2)
df_combinado19 = Indicador_2_9(df_hoja2_1, df_hoja2)
df_combinado20 = Indicador_2_10(df_hoja2_1, df_hoja2)
df_combinado21 = Indicador_3_1(df_hoja3_1, df_hoja2)
df_combinado22 = Indicador_4_1(df_hoja4_1, df_hoja2)
df_combinado23 = Indicador_5_1(df_hoja5_1, df_hoja2)
df_combinado24 = Indicador_6_1(df_hoja6_1, df_hoja2)
df_combinado25 = Indicador_7_1(df_hoja7_1, df_hoja2)
df_combinado26 = Indicador_8_1(df_hoja8_1, df_hoja2)
df_combinado27 = Indicador_9_1(df_hoja3_1, df_hoja2)
df_combinado28 = Indicador_10_1(df_hoja4_1, df_hoja2)
df_combinado29 = Indicador_10_2(df_hoja5_1, df_hoja2)
df_combinado30 = Indicador_10_3(df_hoja6_1, df_hoja2)
df_combinado31 = Indicador_10_4(df_hoja7_1, df_hoja2)
df_combinado32 = Indicador_10_5(df_hoja8_1, df_hoja2)
df_combinado33 = Indicador_11_1(df_hoja1, df_hoja2)
df_combinado34 = Indicador_11_2(df_hoja1, df_hoja2)
df_combinado35 = Indicador_11_3(df_hoja1, df_hoja2)
df_combinado36 = Indicador_11_4(df_hoja9_1, df_hoja2)
df_combinado37 = Indicador_11_5(df_hoja9_1, df_hoja2)
df_combinado38 = Indicador_11_6(df_hoja9_1, df_hoja2)
df_combinado39 = Indicador_11_7(df_hoja9_1, df_hoja2)
df_combinado40 = Indicador_12_1(df_hoja1, df_hoja2)
df_combinado41 = Indicador_13_1(df_hoja1, df_hoja2)
df_combinado42 = Indicador_13_2(df_hoja1, df_hoja2)
df_combinado43 = Indicador_13_3(df_hoja1, df_hoja2)
df_combinado44 = Indicador_13_4(df_hoja1, df_hoja2)
df_combinado45 = Indicador_13_5(df_hoja1, df_hoja2)
df_combinado46 = Indicador_13_6(df_hoja1, df_hoja2)
df_combinado47 = Indicador_13_7(df_hoja1, df_hoja2)
df_combinado48 = Indicador_13_8(df_hoja1, df_hoja2)
df_combinado49 = Indicador_13_9(df_hoja1, df_hoja2)
df_combinado50 = Indicador_13_10(df_hoja1, df_hoja2)
df_combinado51 = Indicador_13_11(df_hoja1, df_hoja2)
df_combinado52 = Indicador_13_12(df_hoja1, df_hoja2)
df_combinado53 = Indicador_13_13(df_hoja1, df_hoja2)
df_combinado54 = Indicador_13_14(df_hoja1, df_hoja2)
df_combinado55 = Indicador_14_1(df_hoja10_1, df_hoja2)
df_combinado56 = Indicador_14_2(df_hoja10_1, df_hoja2)
df_combinado57 = Indicador_15_1(df_hoja2_1, df_hoja2)
df_combinado58 = Indicador_15_2(df_hoja2_1, df_hoja2)
df_combinado59 = Indicador_15_3(df_hoja2_1, df_hoja2)
df_combinado60 = Indicador_15_4(df_hoja2_1, df_hoja2)
df_combinado61 = Indicador_15_5(df_hoja2_1, df_hoja2)
df_combinado62 = Indicador_15_6(df_hoja2_1, df_hoja2)
df_combinado63 = Indicador_16_1(df_combinado57, df_hoja2_1, df_hoja2)
df_combinado64 = Indicador_16_2(df_combinado58, df_hoja2_1, df_hoja2)
df_combinado65 = Indicador_16_3(df_combinado59, df_hoja2_1, df_hoja2)
df_combinado66 = Indicador_16_4(df_combinado62, df_hoja2_1, df_hoja2)
df_combinado67 = Indicador_16_5(df_hoja2_1, df_hoja2)
df_combinado68 = Indicador_17_1(df_hoja2_1, df_hoja2)
df_combinado69 = Indicador_17_2(df_combinado67, df_hoja2_1, df_hoja2)
df_combinado70 = Indicador_17_3(df_combinado68, df_hoja2_1, df_hoja2)
df_combinado71 = Indicador_17_4(df_hoja2_1, df_hoja2)
df_combinado72 = Indicador_17_5(df_hoja2_1, df_hoja2)
df_combinado73 = Indicador_17_6(df_hoja2_1, df_hoja2)
df_combinado74 = Indicador_17_7(df_hoja2_1, df_hoja2)
df_combinado75 = Indicador_17_8(df_hoja2_1, df_hoja2)
df_combinado76 = Indicador_17_9(df_hoja2_1, df_hoja2)
df_combinado77 = Indicador_17_10(df_hoja2_1, df_hoja2)
df_combinado78 = Indicador_17_11(df_hoja2_1, df_hoja2)
df_combinado79 = Indicador_17_12(df_hoja2_1, df_hoja2)
df_combinado80 = Indicador_17_13(df_hoja2_1, df_hoja2)
df_combinado81 = Indicador_18_1(df_combinado71, df_hoja2_1, df_hoja2)
df_combinado82 = Indicador_18_2(df_combinado72, df_hoja2_1, df_hoja2)
df_combinado83 = Indicador_18_3(df_combinado73, df_hoja2_1, df_hoja2)
df_combinado84 = Indicador_18_4(df_combinado74, df_hoja2_1, df_hoja2)
df_combinado85 = Indicador_18_5(df_combinado75, df_hoja2_1, df_hoja2)
df_combinado86 = Indicador_18_6(df_combinado76, df_hoja2_1, df_hoja2)
df_combinado87 = Indicador_18_7(df_combinado77, df_hoja2_1, df_hoja2)
df_combinado88 = Indicador_18_8(df_combinado78, df_hoja2_1, df_hoja2)
df_combinado89 = Indicador_18_9(df_combinado79, df_hoja2_1, df_hoja2)
df_combinado90 = Indicador_18_10(df_combinado80, df_hoja2_1, df_hoja2)
df_combinado91 = Indicador_18_11(df_hoja2_1, df_hoja2)
df_combinado92 = Indicador_18_12(df_combinado91, df_hoja2_1, df_hoja2)
df_combinado93 = Indicador_19_1(df_hoja11_1, df_hoja2_1, df_hoja2)
df_combinado94 = Indicador_19_2(df_hoja11_1, df_hoja2_1, df_hoja2)
df_combinado95 = Indicador_19_3(df_hoja11_1, df_hoja2_1, df_hoja2)
df_combinado96 = Indicador_19_4(df_hoja11_1, df_hoja2_1, df_hoja2)
df_combinado97 = Indicador_19_5(df_hoja11_1, df_hoja2_1, df_hoja2)
df_combinado98 = Indicador_19_6(df_hoja11_1, df_hoja2_1, df_hoja2)
df_combinado99 = Indicador_19_7(df_hoja11_1, df_hoja2_1, df_hoja2)
df_combinado100 = Indicador_19_8(df_hoja11_1, df_hoja2_1, df_hoja2)
df_combinado101 = Indicador_20_1(df_hoja11_1, df_hoja2_1, df_hoja2)
df_combinado102 = Indicador_20_2(df_hoja11_1, df_hoja2_1, df_hoja2)
df_combinado103 = Indicador_20_3(df_hoja11_1, df_hoja2_1, df_hoja2)
df_combinado104 = Indicador_20_4(df_hoja11_1, df_hoja2_1, df_hoja2)
df_combinado105 = Indicador_20_5(df_hoja11_1, df_hoja2_1, df_hoja2)
df_combinado106 = Indicador_20_6(df_hoja11_1, df_hoja2_1, df_hoja2)
df_combinado107 = Indicador_20_7(df_hoja11_1, df_hoja2_1, df_hoja2)
df_combinado108 = Indicador_20_8(df_hoja11_1, df_hoja2_1, df_hoja2)
df_combinado109 = Indicador_20_9(df_hoja11_1, df_hoja2_1, df_hoja2)
df_combinado110 = Indicador_20_10(df_hoja11_1, df_hoja2_1, df_hoja2)
df_combinado111 = Indicador_20_11(df_hoja11_1, df_hoja2_1, df_hoja2)
df_combinado112 = Indicador_20_12(df_hoja11_1, df_hoja2_1, df_hoja2)
df_combinado113 = Indicador_21_1(df_hoja12_0, df_hoja12_1, df_hoja12_2, df_hoja12_3, df_hoja2_1, df_hoja2)
df_combinado113_2 = Indicador_21_2(df_hoja12_0, df_hoja12_1, df_hoja12_2, df_hoja12_3, df_hoja2_1, df_hoja2)
df_combinado113_3 = Indicador_21_3(df_hoja12_0, df_hoja12_1, df_hoja12_2, df_hoja12_3, df_hoja2_1, df_hoja2)
df_combinado113_4 = Indicador_21_4(df_hoja12_0, df_hoja12_1, df_hoja12_2, df_hoja12_3, df_hoja2_1, df_hoja2)


    df93 = df_hoja12_0.copy()
    df94 = df_hoja12_1.copy()
    df95 = df_hoja12_2.copy()
    df96 = df_hoja12_3.copy()

    # Selecciona solo las columnas deseadas en cada DataFrame
    columnas_deseadas = ["Column1", "Column2", "Column14", "Column10"]

    df93 = df_hoja12_0[columnas_deseadas]
    df94 = df_hoja12_1[columnas_deseadas]
    df95 = df_hoja12_2[columnas_deseadas]
    df96 = df_hoja12_3[columnas_deseadas]

    # Agrupa los DataFrames de manera vertical usando la función concat
    df_combinadoDel16 = pd.concat([df93, df94, df95, df96], ignore_index=True)

    # Filtrar por los valores deseados en 'Column10' (equivalente a 'Column11' en Excel)
    valores_filtrados4 = ['Fraude Externo', 'Fraude externo/Fraude con tarjetas bancarias']
    df_combinadoDel16_filtrado = df_combinadoDel16[df_combinadoDel16['Column10'].isin(valores_filtrados4)]

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado113_5 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df_combinadoDel16[['Column2', 'Column10', 'Column14']], how='left', left_on='claveinstitucion', right_on='Column2')


    df_combinado122 = df_combinado113_5.copy()
    df_combinado123 = df_combinado113_5.copy()

    df_combinado122 = df_combinado122[df_combinado122['Column10'] == 'Fraude Externo']
    df_combinado123 = df_combinado123[df_combinado123['Column10'] == 'Fraude externo/Fraude con tarjetas bancarias']

    # Agrupa y suma según tus necesidades
    df_combinado122 = df_combinado122.groupby(['nombreinstitucion']).agg(
        Monto_del_Gasto_asociado_Fraude_externo=('Column14', 'sum')
    ).reset_index()

    # Agrupa y suma según tus necesidades
    df_combinado123 = df_combinado123.groupby(['nombreinstitucion']).agg(
        Monto_del_Gasto_asociado_Fraude_externo=('Column14', 'sum')
    ).reset_index()

    df_combinado113_5 = pd.concat([df_combinado122, df_combinado123], ignore_index=True)

    # Realiza la agregación final sin repetir los valores de 'nombreinstitucion'
    df_combinado113_5 = df_combinado113_4.groupby('nombreinstitucion').agg(
        Monto_del_Gasto_asociado_Fraude_externo=('Monto_del_Gasto_asociado_Fraude_externo', 'sum')
    ).reset_index()



#-----------------------------------------------------------------------------------



IPC = 7.36 / 100
#valor_BQ1 = 100000000

df_combinado92 = df_combinado91.copy()

# Aplicar la fórmula a la columna 'Saldo_de_Intereses_y_rendimientos_a_favor_provenientes_de_inversiones_en_instrumentos_financieros'
df_combinado92['Saldo_del_Resultado_por_compraventa_de_divisas'] = (
    df_combinado92['Saldo_del_Resultado_por_compraventa_de_divisas'] - 2022
) * (1 + IPC) 








#------------------------------------------------------------------------------------
#Codigo de prueba con calculos ya utilizados en el programa
df70 = df_hoja11_1.copy()


# Eliminar los dos últimos dígitos numéricos en la columna 'Año'
df70['Column1'] = df70['Column1'] // 100
# Combinar DataFrames en 'institucion' y 'claveinstitucion'
df_combinado103 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df69[['Column1','Column4', 'Column10']], how='left', left_on='claveinstitucion', right_on='Column4')

# Agrupar y agregar según tus necesidades
df_combinado103 = df_combinado103.groupby(['nombreinstitucion', 'claveinstitucion', 'Column10', 'Column1']).agg(
    numero_de_Corresponsales
=('Column10', 'count')
).reset_index()

# Filtrar por el periodo deseado (2022)
df_combinado103 = df_combinado103[df_combinado103['Column1'] == 2022]
df_combinado103 = df_combinado103[df_combinado103['Column10'] == 'Cajero Automático']

# Eliminación de columnas sobrantes
columna_eliminar = ['Column10', 'claveinstitucion', 'Column1']
df_combinado103 = df_combinado103.drop(columna_eliminar, axis=1)







####################################    CALCULOS INDICADORES CALCULOS       ###############################################################






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

# Normalizar la columna '1.1.1.1' entre 0 y 100 y eliminar decimales
df500['1.1.1.1'] = round((df500['1.1.1.1'] - df500['1.1.1.1'].min()) / (df500['1.1.1.1'].max() - df500['1.1.1.1'].min()) * 100)

# Asegurarse de que los valores estén en el rango correcto (0-100)
df500['1.1.1.1'] = df500['1.1.1.1'].clip(0, 100)




# Definir la función para la fórmula 1.1.1.2
def aplicar_formula2(row):
    numerador = ((row['Column5'] + row['Column6']) - (row['Column7'] + row['Column8'])) - ((row['Column9'] + row['Column10']) - (row['Column11'] + row['Column12']))
    denominador = (row['Column9'] + row['Column10']) - (row['Column11'] + row['Column12'])

    if denominador == 0:
        return 0  # Evitar la división por cero, puedes ajustar esto según tus necesidades

    return (numerador / denominador) * 100

# Aplicar la fórmula a la columna '1.1.1.2'
df501['1.1.1.2'] = df501.apply(aplicar_formula2, axis=1)

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







# Crear un nuevo DataFrame con las columnas deseadas
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


################### ----------Ponderación--------------##############

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
df606 = df_DB.copy()


def aplicar_formula66(row):
    resultado = df604.loc[row.name, 'Y1'] * 0.7
    return resultado 

df606['H1'] = df606.apply(aplicar_formula66, axis=1) 
df606['H1'] = df606['H1'].round()


#H2
df607 = df_DB.copy()


def aplicar_formula67(row):
    resultado = df605.loc[row.name, 'Y2'] * 0.7
    return resultado 

df607['H2'] = df607.apply(aplicar_formula67, axis=1) 
df607['H2'] = df607['H2'].round()


#H3
df608 = df_DB.copy()

def aplicar_formula68(row):
    resultado = df606.loc[row.name, 'Y3'] * 0.7
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

df611 = df_DB.copy()

def aplicar_formula71(row):
    numerador = row['Column46']
    denominador = row['Column40'] + row['Column43'] + row['Column46'] + row['Column48'] + row['Column36']

    # Evitar la división por cero
    if denominador == 0:
        return 0  # Puedes ajustar esto según tus necesidades
    
    resultado = (numerador / denominador) * 100
    return resultado

df611['b-Empresarial'] = df611.apply(aplicar_formula71, axis=1)
df611['b-Empresarial'] = df611['b-Empresarial'].round()





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




# Indicador 1.1.1.5
df620 = df504.copy()

def aplicar_formula79(row):
    min_value = df620['1.1.1.5'].min()
    max_value = df620['1.1.1.5'].max()

    if max_value == min_value or np.isnan(row['1.1.1.5']):
        return 0

    # Calcular la fórmula sin normalizar
    resultado = (row['1.1.1.5'] - min_value) / (max_value - min_value) * 100

    # Verificar si hay NaN después de los cálculos
    if np.isnan(resultado):
        return 0

    # Normalizar la columna '1.1.1.5' entre 0 y 100 y eliminar decimales
    resultado = round((resultado - resultado.min()) / (resultado.max() - resultado.min()) * 100)

    # Asegurarse de que los valores estén en el rango correcto (0-100)
    resultado = resultado.clip(0, 100)

    return resultado

df620['1.1.1.5'] = df620.apply(aplicar_formula79, axis=1)
df620['1.1.1.5'] = df620['1.1.1.5'].round()




# Concatenar los DataFrames en filas en una sola tabla
#result = pd.concat([df_combinado1.set_index('nombreinstitucion'), df_combinado2.set_index('nombreinstitucion'), df_combinado3.set_index('nombreinstitucion'), df_combinado4.set_index('nombreinstitucion'), df_combinado5.set_index('nombreinstitucion'), df_combinado6.set_index('nombreinstitucion'), df_combinado7.set_index('nombreinstitucion'), df_combinado8.set_index('nombreinstitucion'), df_combinado9.set_index('nombreinstitucion'), df_combinado10.set_index('nombreinstitucion'), df_combinado11.set_index('nombreinstitucion'), df_combinado12.set_index('nombreinstitucion'), df_combinado13.set_index('nombreinstitucion'), df_combinado14.set_index('nombreinstitucion'), df_combinado15.set_index('nombreinstitucion'), df_combinado16.set_index('nombreinstitucion'), df_combinado17.set_index('nombreinstitucion'), df_combinado18.set_index('nombreinstitucion'), df_combinado19.set_index('nombreinstitucion'), df_combinado20.set_index('nombreinstitucion'), df_combinado21.set_index('nombreinstitucion'), df_combinado22.set_index('nombreinstitucion'), df_combinado23.set_index('nombreinstitucion'), df_combinado24.set_index('nombreinstitucion'), df_combinado25.set_index('nombreinstitucion'), df_combinado26.set_index('nombreinstitucion'), df_combinado27.set_index('nombreinstitucion'), df_combinado28.set_index('nombreinstitucion'), df_combinado29.set_index('nombreinstitucion'), df_combinado30.set_index('nombreinstitucion'), df_combinado31.set_index('nombreinstitucion'), df_combinado32.set_index('nombreinstitucion'), df_combinado33.set_index('nombreinstitucion'), df_combinado34.set_index('nombreinstitucion'),  df_combinado35.set_index('nombreinstitucion'), df_combinado36.set_index('nombreinstitucion'), df_combinado37.set_index('nombreinstitucion'), df_combinado38.set_index('nombreinstitucion'), df_combinado39.set_index('nombreinstitucion'), df_combinado40.set_index('nombreinstitucion'), df_combinado41.set_index('nombreinstitucion'), df_combinado42.set_index('nombreinstitucion'), df_combinado43.set_index('nombreinstitucion'), df_combinado44.set_index('nombreinstitucion'), df_combinado45.set_index('nombreinstitucion'), df_combinado46.set_index('nombreinstitucion'), df_combinado47.set_index('nombreinstitucion'), df_combinado48.set_index('nombreinstitucion'), df_combinado49.set_index('nombreinstitucion'), df_combinado50.set_index('nombreinstitucion'), df_combinado51.set_index('nombreinstitucion'), df_combinado52.set_index('nombreinstitucion'), df_combinado53.set_index('nombreinstitucion'), df_combinado54.set_index('nombreinstitucion'), df_combinado55.set_index('nombreinstitucion'), df_combinado56.set_index('nombreinstitucion'), df_combinado57.set_index('nombreinstitucion'), df_combinado58.set_index('nombreinstitucion'), df_combinado59.set_index('nombreinstitucion'), df_combinado60.set_index('nombreinstitucion'), df_combinado61.set_index('nombreinstitucion'), df_combinado62.set_index('nombreinstitucion'), df_combinado63.set_index('nombreinstitucion'), df_combinado64.set_index('nombreinstitucion'), df_combinado65.set_index('nombreinstitucion'), df_combinado66.set_index('nombreinstitucion'), df_combinado67.set_index('nombreinstitucion'), df_combinado68.set_index('nombreinstitucion'), df_combinado69.set_index('nombreinstitucion'), df_combinado70.set_index('nombreinstitucion'), df_combinado71.set_index('nombreinstitucion'), df_combinado72.set_index('nombreinstitucion'), df_combinado73.set_index('nombreinstitucion'), df_combinado74.set_index('nombreinstitucion'), df_combinado75.set_index('nombreinstitucion'), df_combinado76.set_index('nombreinstitucion'), df_combinado77.set_index('nombreinstitucion'), df_combinado78.set_index('nombreinstitucion'), df_combinado79.set_index('nombreinstitucion'), df_combinado80.set_index('nombreinstitucion'), df_combinado81.set_index('nombreinstitucion'), df_combinado82.set_index('nombreinstitucion'), df_combinado83.set_index('nombreinstitucion'), df_combinado84.set_index('nombreinstitucion'), df_combinado85.set_index('nombreinstitucion'), df_combinado86.set_index('nombreinstitucion'), df_combinado87.set_index('nombreinstitucion'), df_combinado88.set_index('nombreinstitucion'), df_combinado89.set_index('nombreinstitucion'), df_combinado90.set_index('nombreinstitucion'), df_combinado91.set_index('nombreinstitucion'), df_combinado92.set_index('nombreinstitucion'), df_combinado93.set_index('nombreinstitucion'), df_combinado94.set_index('nombreinstitucion'), df_combinado95.set_index('nombreinstitucion'), df_combinado96.set_index('nombreinstitucion'), df_combinado97.set_index('nombreinstitucion')], axis=1)

# Concatenar los DataFrames en filas en una sola tabla
BD = pd.concat([
    df_combinado1.set_index('nombreinstitucion'),
    df_combinado2.set_index('nombreinstitucion'),
    df_combinado3.set_index('nombreinstitucion'),
    df_combinado4.set_index('nombreinstitucion'),
    df_combinado5.set_index('nombreinstitucion'),
    df_combinado6.set_index('nombreinstitucion'),
    df_combinado7.set_index('nombreinstitucion'),
    df_combinado9.set_index('nombreinstitucion'),
    df_combinado10.set_index('nombreinstitucion'),
    df_combinado11.set_index('nombreinstitucion'),
    df_combinado12.set_index('nombreinstitucion'),
    df_combinado13.set_index('nombreinstitucion'),
    df_combinado14.set_index('nombreinstitucion'),
    df_combinado15.set_index('nombreinstitucion'),
    df_combinado16.set_index('nombreinstitucion'),
    df_combinado17.set_index('nombreinstitucion'),
    df_combinado18.set_index('nombreinstitucion'),
    df_combinado19.set_index('nombreinstitucion'),
    df_combinado20.set_index('nombreinstitucion'),
    df_combinado21.set_index('nombreinstitucion'),
    df_combinado22.set_index('nombreinstitucion'),
    df_combinado24.set_index('nombreinstitucion'),
    df_combinado23.set_index('nombreinstitucion'),
    df_combinado25.set_index('nombreinstitucion'),
    df_combinado26.set_index('nombreinstitucion'),
    df_combinado27.set_index('nombreinstitucion'),
    df_combinado28.set_index('nombreinstitucion'),
    df_combinado29.set_index('nombreinstitucion'),
    df_combinado30.set_index('nombreinstitucion'),
    df_combinado31.set_index('nombreinstitucion'),
    df_combinado32.set_index('nombreinstitucion'),
    df_combinado33.set_index('nombreinstitucion'),
    df_combinado34.set_index('nombreinstitucion'),
    df_combinado35.set_index('nombreinstitucion'),
    df_combinado36.set_index('nombreinstitucion'),
    df_combinado37.set_index('nombreinstitucion'),
    df_combinado38.set_index('nombreinstitucion'),
    df_combinado39.set_index('nombreinstitucion'),
    df_combinado40.set_index('nombreinstitucion'),
    df_combinado41.set_index('nombreinstitucion'),
    df_combinado42.set_index('nombreinstitucion'),
    df_combinado43.set_index('nombreinstitucion'),
    df_combinado44.set_index('nombreinstitucion'),
    df_combinado45.set_index('nombreinstitucion'),
    df_combinado46.set_index('nombreinstitucion'),
    df_combinado47.set_index('nombreinstitucion'),
    df_combinado48.set_index('nombreinstitucion'),
    df_combinado49.set_index('nombreinstitucion'),
    df_combinado50.set_index('nombreinstitucion'),
    df_combinado51.set_index('nombreinstitucion'),
    df_combinado52.set_index('nombreinstitucion'),
    df_combinado53.set_index('nombreinstitucion'),
    df_combinado54.set_index('nombreinstitucion'),
    df_combinado55.set_index('nombreinstitucion'),
    df_combinado56.set_index('nombreinstitucion'),
    df_combinado57.set_index('nombreinstitucion'),
    df_combinado58.set_index('nombreinstitucion'),
    df_combinado59.set_index('nombreinstitucion'),
    df_combinado60.set_index('nombreinstitucion'),
    df_combinado61.set_index('nombreinstitucion'),
    df_combinado62.set_index('nombreinstitucion'),
    df_combinado63.set_index('nombreinstitucion'),
    df_combinado64.set_index('nombreinstitucion'),
    df_combinado65.set_index('nombreinstitucion'),
    df_combinado66.set_index('nombreinstitucion'),
    df_combinado67.set_index('nombreinstitucion'),
    df_combinado68.set_index('nombreinstitucion'),
    df_combinado69.set_index('nombreinstitucion'),
    df_combinado70.set_index('nombreinstitucion'),
    df_combinado71.set_index('nombreinstitucion'),
    df_combinado72.set_index('nombreinstitucion'),
    df_combinado73.set_index('nombreinstitucion'),
    df_combinado74.set_index('nombreinstitucion'),
    df_combinado75.set_index('nombreinstitucion'),
    df_combinado76.set_index('nombreinstitucion'),
    df_combinado77.set_index('nombreinstitucion'),
    df_combinado78.set_index('nombreinstitucion'),
    df_combinado79.set_index('nombreinstitucion'),
    df_combinado80.set_index('nombreinstitucion'),
    df_combinado81.set_index('nombreinstitucion'),
    df_combinado82.set_index('nombreinstitucion'),
    df_combinado83.set_index('nombreinstitucion'),
    df_combinado84.set_index('nombreinstitucion'),
    df_combinado85.set_index('nombreinstitucion'),
    df_combinado86.set_index('nombreinstitucion'),
    df_combinado87.set_index('nombreinstitucion'),
    df_combinado88.set_index('nombreinstitucion'),
    df_combinado89.set_index('nombreinstitucion'),
    df_combinado90.set_index('nombreinstitucion'),
    df_combinado91.set_index('nombreinstitucion'),
    df_combinado92.set_index('nombreinstitucion'),
    df_combinado93.set_index('nombreinstitucion'),
    df_combinado94.set_index('nombreinstitucion'),
    df_combinado95.set_index('nombreinstitucion'),
    df_combinado96.set_index('nombreinstitucion'),
    df_combinado97.set_index('nombreinstitucion'),
    df_combinado98.set_index('nombreinstitucion'),
    df_combinado99.set_index('nombreinstitucion'),
    df_combinado100.set_index('nombreinstitucion'),
    df_combinado101.set_index('nombreinstitucion'),
    df_combinado102.set_index('nombreinstitucion'),
    df_combinado103.set_index('nombreinstitucion'),
    df_combinado104.set_index('nombreinstitucion'),
    df_combinado105.set_index('nombreinstitucion'),
    df_combinado106.set_index('nombreinstitucion'),
    df_combinado107.set_index('nombreinstitucion'),
    df_combinado108.set_index('nombreinstitucion'),
    df_combinado109.set_index('nombreinstitucion'),
    df_combinado110.set_index('nombreinstitucion'),
    df_combinado111.set_index('nombreinstitucion',),
    df_combinado112.set_index('nombreinstitucion',),
    df_combinado113.set_index('nombreinstitucion',),
    df_combinado113_2.set_index('nombreinstitucion',),
    df_combinado113_3.set_index('nombreinstitucion',),
    df_combinado113_4.set_index('nombreinstitucion',)




   
    
    
    
    
    
    ], axis=1)
    
    
    

    
    
    

# Guardar el DataFrame concatenado en un archivo Excel
BD.to_excel(r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\MergeTotal\MergeTotal.xlsx", sheet_name='pag', engine = 'openpyxl')





