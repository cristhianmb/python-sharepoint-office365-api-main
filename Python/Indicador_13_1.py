#Cartera de crédito valuada a valor razonable de Vivienda Media y Residencial


import pandas as pd

def Indicador_13_1(df_hoja1, df_hoja2):
    df23 = df_hoja1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado41 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df23[['importe_pesos', 'institucion', 'concepto']], how='left', left_on='claveinstitucion', right_on='institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado41 = df_combinado41.groupby(['nombreinstitucion', 'claveinstitucion', 'concepto']).agg(
        Saldo_de_la_Cartera_de_credrito_con_riesgo_de_credito_etapa_de_Vivienda_Media_y_Residencial=('importe_pesos', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado41 = df_combinado41[df_combinado41['concepto'] == 101800104004]

    # Eliminación de columnas sobrantes
    columna_eliminar = ['concepto', 'claveinstitucion']
    df_combinado41 = df_combinado41.drop(columna_eliminar, axis=1)

    return df_combinado41
