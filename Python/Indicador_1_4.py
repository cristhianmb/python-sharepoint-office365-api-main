#Cartera de créditos interbancarios con riesgo de crédito etapa 2 - 2021
import pandas as pd

def Indicador_1_4(df_hoja1, df_hoja2):
    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado9 = pd.merge(df_hoja1, df_hoja2[['claveinstitucion', 'nombreinstitucion']], how='left', left_on='institucion', right_on='claveinstitucion')
    df_combinado9 = df_combinado9.groupby(['nombreinstitucion', 'concepto']).agg(Cartera_de_créditos_interbancarios_con_riesgo_de_crédito_etapa=('importe_pesos', 'mean')).reset_index()
    df_combinado9 = df_combinado9[df_combinado9['concepto'] == 101800807041]
    
    

    IPC = 7.36 / 100
    #df_combinado9['indicador_1_1'] = df_combinado9['promedio'] * (1 + IPC)  
    df_combinado9['Cartera_de_créditos_interbancarios_con_riesgo_de_crédito_etapa'] = df_combinado9['Cartera_de_créditos_interbancarios_con_riesgo_de_crédito_etapa'] * (1 + IPC)  
    
    
    
    # Eliminación de columnas sobrantes
    columna_eliminar = ['concepto']
    df_combinado9=df_combinado9.drop(columna_eliminar,axis = 1)

    return df_combinado9
