#Ingresos por Comisiones por el otorgamiento inicial del crédito - 2022
import pandas as pd

def Indicador_2_4(df_hoja1, hoja2_1):
    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado14 = pd.merge(df_hoja1, hoja2_1[['claveinstitucion', 'nombreinstitucion']], how='left', left_on='institucion', right_on='claveinstitucion')
    df_combinado14 = df_combinado14.groupby(['nombreinstitucion', 'concepto']).agg(Ingresos_por_Comisiones_por_el_otorgamiento_inicial_del_creditos=('importe_pesos', 'sum')).reset_index()
    df_combinado14 = df_combinado14[df_combinado14['concepto'] == 500200102013]
    
    
    return df_combinado14


