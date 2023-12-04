# Saldo de la Cartera de crédito con riesgo de crédito Etapa 1 de Vivienda Interés Social
import pandas as pd

def Indicador_13_5(df_hoja1, df_hoja2):
    df27 = df_hoja1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado45 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df27[['importe_pesos', 'institucion', 'concepto']], how='left', left_on='claveinstitucion', right_on='institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado45 = df_combinado45.groupby(['nombreinstitucion', 'claveinstitucion', 'concepto']).agg(
        Saldo_de_la_Cartera_de_crédito_con_riesgo_de_crédito_Etapa_1_de_Vivienda_Interés_Social=('importe_pesos', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado45 = df_combinado45[df_combinado45['concepto'] == 101800507024]

    # Eliminación de columnas sobrantes
    columna_eliminar = ['concepto', 'claveinstitucion']
    df_combinado45 = df_combinado45.drop(columna_eliminar, axis=1)

    return df_combinado45

