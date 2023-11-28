#Cartera de créditos interbancarios con riesgo de crédito etapa 2 - 2022
import pandas as pd

def Indicador_5(df_hoja1, df_hoja2):
    
    df_combinado5 = pd.merge(df_hoja1, df_hoja2[['claveinstitucion', 'nombreinstitucion']], how='left', left_on='institucion', right_on='claveinstitucion')
    df_combinado5 = df_combinado5.groupby(['nombreinstitucion', 'concepto']).agg(Cartera_de_créditos_interbancarios_con_riesgo_de_crédito_etapa=('importe_pesos', 'mean')).reset_index()
    df_combinado5 = df_combinado5[df_combinado5['concepto'] == 101800807041]
    
    
    
    # Eliminación de columnas sobrantes
    columna_eliminar = ['concepto']
    df_combinado5=df_combinado5.drop(columna_eliminar,axis = 1)
 

    return df_combinado5
