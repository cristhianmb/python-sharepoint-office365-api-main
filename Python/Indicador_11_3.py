#Quitas y Castigos de Cartera al Consumo
import pandas as pd

def Indicador_11_3(df_hoja1, df_hoja2):
    df17 = df_hoja1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado35 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df17[['importe_pesos', 'institucion', 'concepto']], how='left', left_on='claveinstitucion', right_on='institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado35 = df_combinado35.groupby(['nombreinstitucion', 'claveinstitucion', 'concepto']).agg(
        cartera_valuada_a_valor_razonable=('importe_pesos', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado35 = df_combinado35[df_combinado35['concepto'] == 101800104004]

    # Eliminación de columnas sobrantes
    columna_eliminar = ['concepto', 'claveinstitucion']
    df_combinado35 = df_combinado35.drop(columna_eliminar, axis=1)

    return df_combinado35
