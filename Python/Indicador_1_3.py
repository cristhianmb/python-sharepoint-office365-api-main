#Saldo Vigente Cartera de créditos interbancarios con riesgo de crédito etapa 1 - 2021
import pandas as pd

def Indicador_1_3(df_hoja1, df_hoja2):
    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado8 = pd.merge(df_hoja1, df_hoja2[['claveinstitucion', 'nombreinstitucion']], how='left', left_on='institucion', right_on='claveinstitucion')
    df_combinado8 = df_combinado8.groupby(['nombreinstitucion', 'concepto']).agg(Saldo_Vigente_Cartera_de_créditos_interbancarios_con_riesgo_de_crédito_etapa=('importe_pesos', 'mean')).reset_index()
    df_combinado8 = df_combinado8[df_combinado8['concepto'] == 101800208009]
    
    

    IPC = 7.36 / 100
    #df_combinado8['indicador_1_1'] = df_combinado8['promedio'] * (1 + IPC) 
    df_combinado8['Saldo_Vigente_Cartera_de_créditos_interbancarios_con_riesgo_de_crédito_etapa'] = df_combinado8['Saldo_Vigente_Cartera_de_créditos_interbancarios_con_riesgo_de_crédito_etapa'] * (1 + IPC)  
    
    # Eliminación de columnas sobrantes
    columna_eliminar = ['concepto']
    df_combinado8=df_combinado8.drop(columna_eliminar,axis = 1)

    return df_combinado8
