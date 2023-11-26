#Comisiones y tarifas cobradas - 2022
import pandas as pd

def Indicador_2_8(df_hoja1, hoja2_1):
    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado18 = pd.merge(df_hoja1, hoja2_1[['claveinstitucion', 'nombreinstitucion']], how='left', left_on='institucion', right_on='claveinstitucion')
    df_combinado18 = df_combinado18.groupby(['nombreinstitucion', 'concepto']).agg(Comisiones_y_tarifas_cobradas=('importe_pesos', 'sum')).reset_index()
    df_combinado18 = df_combinado18[df_combinado18['concepto'] == 501000301005]
    
    
    return df_combinado18

