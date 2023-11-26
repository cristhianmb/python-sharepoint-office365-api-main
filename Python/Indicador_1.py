#Activo Total
import pandas as pd

def Indicador_1(df_hoja1, df_hoja2):
    
    df_combinado1 = pd.merge(df_hoja1, df_hoja2[['claveinstitucion', 'nombreinstitucion']], how='left', left_on='institucion', right_on='claveinstitucion')
    df_combinado1 = df_combinado1.groupby(['nombreinstitucion', 'concepto']).agg(Activo_Total=('importe_pesos', 'mean')).reset_index()
    df_combinado1 = df_combinado1[df_combinado1['concepto'] == 100000000000 ]
    
    return df_combinado1
