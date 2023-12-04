#Saldo Cartera de crédito con riesgo de crédito Etapa 3 Vivienda Interés Social


import pandas as pd

def Indicador_13_2(df_hoja1, df_hoja2):
    df24 = df_hoja1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado42 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df24[['importe_pesos', 'institucion', 'concepto']], how='left', left_on='claveinstitucion', right_on='institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado42 = df_combinado42.groupby(['nombreinstitucion', 'claveinstitucion', 'concepto']).agg(
        Saldo_Cartera_de_crédito_con_riesgo_de_crédito_Etapa_Vivienda_Interés_Sociall=('importe_pesos', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado42 = df_combinado42[df_combinado42['concepto'] == 101800706019]

    # Eliminación de columnas sobrantes
    columna_eliminar = ['concepto', 'claveinstitucion']
    df_combinado42 = df_combinado42.drop(columna_eliminar, axis=1)

    return df_combinado42

