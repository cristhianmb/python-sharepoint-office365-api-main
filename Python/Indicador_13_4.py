#Saldo Cartera de crédito con riesgo de crédito Etapa 3a Vivienda, Remodelación o mejoramiento con garantía otorgada por la Banca de Desarrollo o fideicomisos públicos


import pandas as pd

def Indicador_13_4(df_hoja1, df_hoja2):
    df26 = df_hoja1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado44 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df26[['importe_pesos', 'institucion', 'concepto']], how='left', left_on='claveinstitucion', right_on='institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado44 = df_combinado44.groupby(['nombreinstitucion', 'claveinstitucion', 'concepto']).agg(
        Saldo_Cartera_de_crédito_con_riesgo_de_crédito_Etapa_Vivienda_Remodelación_o_mejoramiento_con_garantía_otorgada_por_la_Banca_de_Desarrollo_o_fideicomisos_públicos=('importe_pesos', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado44 = df_combinado44[df_combinado44['concepto'] == 101800706021]

    # Eliminación de columnas sobrantes
    columna_eliminar = ['concepto', 'claveinstitucion']
    df_combinado44 = df_combinado44.drop(columna_eliminar, axis=1)

    return df_combinado44
