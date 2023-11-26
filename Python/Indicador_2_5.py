#Ingresos por Comisiones y tarifas cobradas en operaciones de crédito -2022
import pandas as pd

def Indicador_2_5(df_hoja1, hoja2_1):
    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado15 = pd.merge(df_hoja1, hoja2_1[['claveinstitucion', 'nombreinstitucion']], how='left', left_on='institucion', right_on='claveinstitucion')
    df_combinado15 = df_combinado15.groupby(['nombreinstitucion', 'concepto']).agg(Ingresos_por_Comisiones_y_tarifas_cobradas_en_operaciones_de_creditos=('importe_pesos', 'sum')).reset_index()
    df_combinado15 = df_combinado15[df_combinado15['concepto'] == 501000301005]
    
    
    return df_combinado15


