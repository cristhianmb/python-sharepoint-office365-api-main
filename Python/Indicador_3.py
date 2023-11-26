#Cartera de crédito con riesgo de crédito Etapa 2 - 2022
import pandas as pd

def Indicador_3(df_hoja1, df_hoja2):
    
    df_combinado3 = pd.merge(df_hoja1, df_hoja2[['claveinstitucion', 'nombreinstitucion']], how='left', left_on='institucion', right_on='claveinstitucion')
    df_combinado3 = df_combinado3.groupby(['nombreinstitucion', 'concepto']).agg(Cartera_de_crédito_con_riesgo_de_crédito_Etapa=('importe_pesos', 'mean')).reset_index()
    df_combinado3 = df_combinado3[df_combinado3['concepto'] == 101800104002 ]
    


    return df_combinado3
