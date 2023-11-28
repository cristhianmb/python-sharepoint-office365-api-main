#Cartera de crédito con riesgo de crédito etapa 2 - 2021
import pandas as pd

def Indicador_1_2(df_hoja1, df_hoja2):
    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado7 = pd.merge(df_hoja1, df_hoja2[['claveinstitucion', 'nombreinstitucion']], how='left', left_on='institucion', right_on='claveinstitucion')
    df_combinado7 = df_combinado7.groupby(['nombreinstitucion', 'concepto']).agg(Cartera_de_crédito_con_riesgo_de_crédito_etapa=('importe_pesos', 'mean')).reset_index()
    df_combinado7 = df_combinado7[df_combinado7['concepto'] == 101800104002]
    
    

    IPC = 7.36 / 100
    #df_combinado7['indicador_1_1'] = df_combinado7['promedio'] * (1 + IPC) 
    df_combinado7['Cartera_de_crédito_con_riesgo_de_crédito_etapa'] = df_combinado7['Cartera_de_crédito_con_riesgo_de_crédito_etapa'] * (1 + IPC)  
    
    
    # Eliminación de columnas sobrantes
    columna_eliminar = ['concepto']
    df_combinado7=df_combinado7.drop(columna_eliminar,axis = 1)

    return df_combinado7
