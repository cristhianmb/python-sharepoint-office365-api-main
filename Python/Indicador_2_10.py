#Otros ingresos (egresos) de la operacioenes 2022
import pandas as pd

def Indicador_2_10(df_hoja1, hoja2_1):
    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado20 = pd.merge(df_hoja1, hoja2_1[['claveinstitucion', 'nombreinstitucion']], how='left', left_on='institucion', right_on='claveinstitucion')
    df_combinado20 = df_combinado20.groupby(['nombreinstitucion', 'concepto']).agg(Otros_ingresos_egresos_de_la_operaciones=('importe_pesos', 'sum')).reset_index()
    df_combinado20 = df_combinado20[df_combinado20['concepto'] == 501600301008]
    
    
    
    # Eliminación de columnas sobrantes
    columna_eliminar = ['concepto']
    df_combinado20=df_combinado20.drop(columna_eliminar,axis = 1)
    
    
    return df_combinado20

