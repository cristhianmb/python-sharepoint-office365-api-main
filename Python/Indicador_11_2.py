#Quitas y Castigos de Cartera al Consumo
import pandas as pd

def Indicador_11_2(df_hoja1, df_hoja2):
    df16 = df_hoja1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado34 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df16[['importe_pesos', 'institucion', 'concepto']], how='left', left_on='claveinstitucion', right_on='institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado34 = df_combinado34.groupby(['nombreinstitucion', 'claveinstitucion', 'concepto']).agg(
        Quitas_y_Castigos_de_Cartera_al_Consumo=('importe_pesos', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado34 = df_combinado34[df_combinado34['concepto'] == 101800104003]

    # Eliminación de columnas sobrantes
    columna_eliminar = ['concepto', 'claveinstitucion']
    df_combinado34 = df_combinado34.drop(columna_eliminar, axis=1)

    return df_combinado34
