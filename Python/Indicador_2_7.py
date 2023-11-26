#Ingresos por Intereses - 2022
import pandas as pd

def Indicador_2_7(df_hoja1, hoja2_1):
    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado17 = pd.merge(df_hoja1, hoja2_1[['claveinstitucion', 'nombreinstitucion']], how='left', left_on='institucion', right_on='claveinstitucion')
    df_combinado17 = df_combinado17.groupby(['nombreinstitucion', 'concepto']).agg(Ingresos_por_Intereses=('importe_pesos', 'sum')).reset_index()
    df_combinado17 = df_combinado17[df_combinado17['concepto'] == 500200101001]
    
    
    return df_combinado17

