#Comisiones y tarifas cobradas - 2022
import pandas as pd

def Indicador_2_8(df_hoja1, hoja2_1):
    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado18 = pd.merge(df_hoja1, hoja2_1[['claveinstitucion', 'nombreinstitucion']], how='left', left_on='institucion', right_on='claveinstitucion')
    df_combinado18 = df_combinado18.groupby(['nombreinstitucion', 'concepto', 'periodo']).agg(Comisiones_y_tarifas_cobradas=('importe_pesos', 'mean')).reset_index()
    df_combinado18 = df_combinado18[df_combinado18['concepto'] == 501000301005]
    df_combinado18 = df_combinado18[df_combinado18['periodo'] == 202212]
    
    
    
    # Eliminación de columnas sobrantes
    columna_eliminar = ['concepto', 'periodo']
    df_combinado18=df_combinado18.drop(columna_eliminar,axis = 1)
    
    return df_combinado18

