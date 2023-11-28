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






# Ruta al archivo Excel en tu PC
ruta_archivo_excel1 = r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\Reportes\040_R12A_1219_133.xlsx"
ruta_archivo_excel2 = r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\Reportes\040_R12A_1220_133.xlsx"
ruta_archivo_excel3 = r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\Reportes\040_13A_R3B_Vivienda_2022.xlsx"
ruta_archivo_excel4 = r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\Reportes\040_30B_R2_Nómina.xlsx"
ruta_archivo_excel5 = r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\Reportes\040_31B_R2_Automotriz.xlsx"
ruta_archivo_excel6 = r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\Reportes\040_32B_R2_ABCD.xlsx"
ruta_archivo_excel7 = r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\Reportes\040_33B_R2_Personales.xlsx"
ruta_archivo_excel8 = r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\Reportes\040-11A_2022_Empresas_2022.xlsx"
#ruta_archivo_excel6 = r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\Reportes\040_30B_R2_Nómina.xlsx"
#ruta_archivo_excel8 = r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\Reportes\040_32B_R2_ABCD.xlsx"
#ruta_archivo_excel9 = r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\Reportes\040_33B_R2_Personales.xlsx"








# Nombre de las hojas que deseas cargar del archivo 040_R12A_1219_133.xlsx
hoja1 = '040_R12A_1219_133'
hoja2 = 'catalogo_instituciones_BM'
# Nombre de las hojas que deseas cargar del archivo 040_R12A_1220_133.xlsx
hoja2_1 = '040_R12A_1220_133'
# Nombre de las hojas que deseas cargar del archivo 040_11A_2022_Empresas_2022.xlsx
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









  


# Concatenar los DataFrames en filas en una sola tabla
result = pd.concat([df_combinado1.set_index('nombreinstitucion'), df_combinado2.set_index('nombreinstitucion'), df_combinado3.set_index('nombreinstitucion'), df_combinado4.set_index('nombreinstitucion'), df_combinado5.set_index('nombreinstitucion'), df_combinado6.set_index('nombreinstitucion'), df_combinado7.set_index('nombreinstitucion'), df_combinado8.set_index('nombreinstitucion'), df_combinado9.set_index('nombreinstitucion'), df_combinado10.set_index('nombreinstitucion'), df_combinado11.set_index('nombreinstitucion'), df_combinado12.set_index('nombreinstitucion'), df_combinado13.set_index('nombreinstitucion'), df_combinado14.set_index('nombreinstitucion'), df_combinado15.set_index('nombreinstitucion'), df_combinado16.set_index('nombreinstitucion'), df_combinado17.set_index('nombreinstitucion'), df_combinado18.set_index('nombreinstitucion'), df_combinado19.set_index('nombreinstitucion'), df_combinado20.set_index('nombreinstitucion'), df_combinado21.set_index('nombreinstitucion'), df_combinado22.set_index('nombreinstitucion'), df_combinado23.set_index('nombreinstitucion'), df_combinado24.set_index('nombreinstitucion'), df_combinado25.set_index('nombreinstitucion'), df_combinado26.set_index('nombreinstitucion')], axis=1)

# Guardar el DataFrame concatenado en un archivo Excel
result.to_excel(r"C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS\Anexo IEB\MergeTotal\MergeTotal.xlsx", sheet_name='pag', engine = 'openpyxl')





