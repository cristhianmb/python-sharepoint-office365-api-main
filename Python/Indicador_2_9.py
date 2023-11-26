#Resultado por Intermediación - 2022
import pandas as pd

def Indicador_2_9(df_hoja1, hoja2_1):
    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado19 = pd.merge(df_hoja1, hoja2_1[['claveinstitucion', 'nombreinstitucion']], how='left', left_on='institucion', right_on='claveinstitucion')
    df_combinado19 = df_combinado19.groupby(['nombreinstitucion', 'concepto']).agg(Resultado_por_Intermediaciones=('importe_pesos', 'sum')).reset_index()
    df_combinado19 = df_combinado19[df_combinado19['concepto'] == 501400301007]
    
    
    return df_combinado19

