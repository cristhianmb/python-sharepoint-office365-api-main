#EPRC.- Estimación Preventiva para Riesgos Crediticios - 2022
import pandas as pd

def Indicador_2_6(df_hoja1, hoja2_1):
    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado16 = pd.merge(df_hoja1, hoja2_1[['claveinstitucion', 'nombreinstitucion']], how='left', left_on='institucion', right_on='claveinstitucion')
    df_combinado16 = df_combinado16.groupby(['nombreinstitucion', 'concepto']).agg(EPRC_Estimaciones_Preventiva_para_Riesgos_Crediticios=('importe_pesos', 'sum')).reset_index()
    df_combinado16 = df_combinado16[df_combinado16['concepto'] == 600800201004]
    
    
    return df_combinado16

