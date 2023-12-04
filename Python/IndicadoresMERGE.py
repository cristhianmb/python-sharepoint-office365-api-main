import pandas as pd

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




df36 = df_hoja1.copy()

# Combinar DataFrames en 'institucion' y 'claveinstitucion'
df_combinado54 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df36[['importe_pesos', 'institucion', 'concepto']], how='left', left_on='claveinstitucion', right_on='institucion')

# Agrupar y agregar según tus necesidades
df_combinado54 = df_combinado54.groupby(['nombreinstitucion', 'claveinstitucion', 'concepto']).agg(
    Captación_total

=('importe_pesos', 'mean')
).reset_index()

# Filtrar por el periodo deseado (2022)
df_combinado54 = df_combinado54[df_combinado54['concepto'] == 200000000000]

# Eliminación de columnas sobrantes
columna_eliminar = ['concepto', 'claveinstitucion']
df_combinado54 = df_combinado54.drop(columna_eliminar, axis=1)













# Concatenar los DataFrames en filas en una sola tabla
result = pd.concat([df_combinado1.set_index('nombreinstitucion'), df_combinado2.set_index('nombreinstitucion'), df_combinado3.set_index('nombreinstitucion'), df_combinado4.set_index('nombreinstitucion'), df_combinado5.set_index('nombreinstitucion'), df_combinado6.set_index('nombreinstitucion'), df_combinado7.set_index('nombreinstitucion'), df_combinado8.set_index('nombreinstitucion'), df_combinado9.set_index('nombreinstitucion'), df_combinado10.set_index('nombreinstitucion'), df_combinado11.set_index('nombreinstitucion'), df_combinado12.set_index('nombreinstitucion'), df_combinado13.set_index('nombreinstitucion'), df_combinado14.set_index('nombreinstitucion'), df_combinado15.set_index('nombreinstitucion'), df_combinado16.set_index('nombreinstitucion'), df_combinado17.set_index('nombreinstitucion'), df_combinado18.set_index('nombreinstitucion'), df_combinado19.set_index('nombreinstitucion'), df_combinado20.set_index('nombreinstitucion'), df_combinado21.set_index('nombreinstitucion'), df_combinado22.set_index('nombreinstitucion'), df_combinado23.set_index('nombreinstitucion'), df_combinado24.set_index('nombreinstitucion'), df_combinado25.set_index('nombreinstitucion'), df_combinado26.set_index('nombreinstitucion'), df_combinado27.set_index('nombreinstitucion'), df_combinado28.set_index('nombreinstitucion'), df_combinado29.set_index('nombreinstitucion'), df_combinado30.set_index('nombreinstitucion'), df_combinado31.set_index('nombreinstitucion'), df_combinado32.set_index('nombreinstitucion'), df_combinado33.set_index('nombreinstitucion'), df_combinado34.set_index('nombreinstitucion'),  df_combinado35.set_index('nombreinstitucion'), df_combinado36.set_index('nombreinstitucion'), df_combinado37.set_index('nombreinstitucion'), df_combinado38.set_index('nombreinstitucion'), df_combinado39.set_index('nombreinstitucion'), df_combinado40.set_index('nombreinstitucion'), df_combinado41.set_index('nombreinstitucion'), df_combinado42.set_index('nombreinstitucion'), df_combinado43.set_index('nombreinstitucion'), df_combinado44.set_index('nombreinstitucion'), df_combinado45.set_index('nombreinstitucion'), df_combinado46.set_index('nombreinstitucion'), df_combinado47.set_index('nombreinstitucion'), df_combinado48.set_index('nombreinstitucion'), df_combinado49.set_index('nombreinstitucion'), df_combinado50.set_index('nombreinstitucion'), df_combinado51.set_index('nombreinstitucion'), df_combinado52.set_index('nombreinstitucion'), df_combinado53.set_index('nombreinstitucion'), df_combinado54.set_index('nombreinstitucion')], axis=1)

# Guardar el DataFrame concatenado en un archivo Excel
result.to_excel(r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\MergeTotal\MergeTotal.xlsx", sheet_name='pag', engine = 'openpyxl')





