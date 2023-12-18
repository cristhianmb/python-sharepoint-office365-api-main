import pandas as pd
import csv


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














# Ruta al archivo Excel en tu PC
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





