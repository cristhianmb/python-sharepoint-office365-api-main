# Saldo de la Cartera de crédito con riesgo de crédito Etapa 1 de Créditos adquiridos al INFONAVIT o el FOVISSSTE
import pandas as pd

def Indicador_13_8(df_hoja1, df_hoja2):
    df30 = df_hoja1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado48 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df30[['importe_pesos', 'institucion', 'concepto']], how='left', left_on='claveinstitucion', right_on='institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado48 = df_combinado48.groupby(['nombreinstitucion', 'claveinstitucion', 'concepto']).agg(
        Saldo_de_la_Cartera_de_crédito_con_riesgo_de_crédito_Etapa_de_Créditos_adquiridos_al_INFONAVIT_o_el_FOVISSSTE=('importe_pesos', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado48 = df_combinado48[df_combinado48['concepto'] == 101800507025]

    # Eliminación de columnas sobrantes
    columna_eliminar = ['concepto', 'claveinstitucion']
    df_combinado48 = df_combinado48.drop(columna_eliminar, axis=1)

    return df_combinado48
