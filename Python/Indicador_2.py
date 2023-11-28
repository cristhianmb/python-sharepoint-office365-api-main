#Saldo de la Cartera de crédito con riesgo de crédito Etapa 1 - 2022
import pandas as pd

def Indicador_2(df_hoja1, df_hoja2):
    
    df_combinado2 = pd.merge(df_hoja1, df_hoja2[['claveinstitucion', 'nombreinstitucion']], how='left', left_on='institucion', right_on='claveinstitucion')
    df_combinado2 = df_combinado2.groupby(['nombreinstitucion', 'concepto']).agg(Saldo_de_la_Cartera_de_crédito_con_riesgo_de_crédito_Etapa=('importe_pesos', 'mean')).reset_index()
    df_combinado2 = df_combinado2[df_combinado2['concepto'] == 101800104001]
    
    
    # Eliminación de columnas sobrantes
    columna_eliminar = ['concepto']
    df_combinado2=df_combinado2.drop(columna_eliminar,axis = 1)
    

    return df_combinado2
