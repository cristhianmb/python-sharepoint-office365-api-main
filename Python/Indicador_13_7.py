# Cartera de crédito valuada a valor razonable de Vivienda Interés Social
import pandas as pd

def Indicador_13_7(df_hoja1, df_hoja2):
    df29 = df_hoja1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado47 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df29[['importe_pesos', 'institucion', 'concepto']], how='left', left_on='claveinstitucion', right_on='institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado47 = df_combinado47.groupby(['nombreinstitucion', 'claveinstitucion', 'concepto']).agg(
        Cartera_de_crédito_valuada_a_valor_razonable_de_Vivienda_Interés_Social=('importe_pesos', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado47 = df_combinado47[df_combinado47['concepto'] == 101801006035]

    # Eliminación de columnas sobrantes
    columna_eliminar = ['concepto', 'claveinstitucion']
    df_combinado47 = df_combinado47.drop(columna_eliminar, axis=1)

    return df_combinado47
