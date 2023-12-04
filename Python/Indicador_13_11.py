#Cartera de crédito valuada a valor razonable de Créditos adquiridos al INFONAVIT o el FOVISSSTEimport pandas as pd

import pandas as pd

def Indicador_13_11(df_hoja1, df_hoja2):
    df33 = df_hoja1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado51 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df33[['importe_pesos', 'institucion', 'concepto']], how='left', left_on='claveinstitucion', right_on='institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado51 = df_combinado51.groupby(['nombreinstitucion', 'claveinstitucion', 'concepto']).agg(
        Saldo_de_la_Cartera_de_crédito_con_riesgo_de_crédito_Etapa_1_de_Remodelación_o_mejoramiento_con_garantía_otorgada_por_la_Banca_de_Desarrollo_o_fideicomisos_públicos=('importe_pesos', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado51 = df_combinado51[df_combinado51['concepto'] == 101800507026]

    # Eliminación de columnas sobrantes
    columna_eliminar = ['concepto', 'claveinstitucion']
    df_combinado51 = df_combinado51.drop(columna_eliminar, axis=1)

    return df_combinado51
