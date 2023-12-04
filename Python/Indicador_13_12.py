#Saldo de la Cartera de crédito con riesgo de crédito Etapa 2 de Remodelación o mejoramiento con garantía otorgada por la Banca de Desarrollo o fideicomisos públicos

import pandas as pd

def Indicador_13_12(df_hoja1, df_hoja2):
    df34 = df_hoja1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado52 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df34[['importe_pesos', 'institucion', 'concepto']], how='left', left_on='claveinstitucion', right_on='institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado52 = df_combinado52.groupby(['nombreinstitucion', 'claveinstitucion', 'concepto']).agg(
        Saldo_de_la_Cartera_de_crédito_con_riesgo_de_crédito_Etapa_de_Remodelación_o_mejoramiento_con_garantía_otorgada_por_la_Banca_de_Desarrollo_o_fideicomisos_públicos=('importe_pesos', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado52 = df_combinado52[df_combinado52['concepto'] == 101800607031]

    # Eliminación de columnas sobrantes
    columna_eliminar = ['concepto', 'claveinstitucion']
    df_combinado52 = df_combinado52.drop(columna_eliminar, axis=1)

    return df_combinado52
