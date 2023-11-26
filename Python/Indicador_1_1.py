#Saldo de la Cartera de crédito con riesgo de crédito etapa 1 - 2021
import pandas as pd

def Indicador_1_1(df_hoja1, df_hoja2):
    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado6 = pd.merge(df_hoja1, df_hoja2[['claveinstitucion', 'nombreinstitucion']], how='left', left_on='institucion', right_on='claveinstitucion')
    df_combinado6 = df_combinado6.groupby(['nombreinstitucion', 'concepto']).agg(Saldo_de_la_Cartera_de_crédito_con_riesgo_de_crédito_etapa=('importe_pesos', 'mean')).reset_index()
    df_combinado6 = df_combinado6[df_combinado6['concepto'] == 101800104001]
    
    

    IPC = 7.36 / 100
    #df_combinado6['indicador_1_1'] = df_combinado6['promedio'] * (1 + IPC)  
    df_combinado6['Saldo_de_la_Cartera_de_crédito_con_riesgo_de_crédito_etapa'] = df_combinado6['Saldo_de_la_Cartera_de_crédito_con_riesgo_de_crédito_etapa'] * (1 + IPC)  

    

    return df_combinado6
