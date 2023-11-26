import pandas as pd

def Indicador_3_1(df_hoja3_1, df_hoja2):

   df2 = df_hoja3_1.copy()

       # Eliminar los dos últimos dígitos numéricos en la columna 'cve_periodo'
   df2['cve_periodo'] = df2['cve_periodo'] // 100

       # Combinar DataFrames en 'institucion' y 'claveinstitucion'
   df_combinado21 = pd.merge(df_hoja2[['nombreinstitucion','claveinstitucion']], df2[['cve_periodo', 'cve_institucion','cve_moneda', 'dat_id_credito_met_cnbv']], how='left', left_on='claveinstitucion', right_on='cve_institucion')
       
       # Agrupar y agregar según tus necesidades
   df_combinado21 = df_combinado21.groupby(['nombreinstitucion', 'cve_periodo', 'cve_moneda']).agg(
         operaciones=('dat_id_credito_met_cnbv', 'sum')
       ).reset_index()

   df_combinado21 = df_combinado21[(df_combinado21['cve_moneda'] == 99)&(df_combinado21['cve_periodo'] == 2022)]   

   columna_eliminar = ['cve_periodo','cve_moneda']

   df_combinado21=df_combinado21.drop(columna_eliminar,axis = 1)
   
   return df_combinado21
