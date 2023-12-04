#Saldo de la Cartera de crédito con riesgo de crédito etapa 1+2 de Vivienda Media y Residencial


import pandas as pd

def Indicador_12_1(df_hoja1, df_hoja2):
    df22 = df_hoja1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado40 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df22[['importe_pesos', 'institucion', 'concepto']], how='left', left_on='claveinstitucion', right_on='institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado40 = df_combinado40.groupby(['nombreinstitucion', 'claveinstitucion', 'concepto']).agg(
        Saldo_de_la_Cartera_de_crédito_con_riesgo_de_crédito_etapa_de_Vivienda_Media_y_Residencial=('importe_pesos', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado40 = df_combinado40[df_combinado40['concepto'] == 101800105003]

    # Eliminación de columnas sobrantes
    columna_eliminar = ['concepto', 'claveinstitucion']
    df_combinado40 = df_combinado40.drop(columna_eliminar, axis=1)

    return df_combinado40
