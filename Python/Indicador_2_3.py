#Ingresos por Intereses de Cartera de crédito con riesgo de crédito etapa 3 - 2022
import pandas as pd

def Indicador_2_3(df_hoja1, hoja2_1):
    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado13 = pd.merge(df_hoja1, hoja2_1[['claveinstitucion', 'nombreinstitucion']], how='left', left_on='institucion', right_on='claveinstitucion')
    df_combinado13 = df_combinado13.groupby(['nombreinstitucion', 'concepto']).agg(Ingresos_por_Intereses_de_Cartera_de_crédito_con_riesgo_de_crédito_etapa=('importe_pesos', 'sum')).reset_index()
    df_combinado13 = df_combinado13[df_combinado13['concepto'] == 500200102010]
    
    
    return df_combinado13


