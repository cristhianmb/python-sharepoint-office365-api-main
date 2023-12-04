#Saldo de la Cartera de crédito con riesgo de crédito Etapa 1 de Remodelación o mejoramiento con garantía otorgada por la Banca de Desarrollo o fideicomisos públicos
import pandas as pd

def Indicador_13_10(df_hoja1, df_hoja2):
    df32 = df_hoja1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado50 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df32[['importe_pesos', 'institucion', 'concepto']], how='left', left_on='claveinstitucion', right_on='institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado50 = df_combinado50.groupby(['nombreinstitucion', 'claveinstitucion', 'concepto']).agg(
        Cartera_de_crédito_valuada_a_valor_razonable_de_Créditos_adquiridos_al_INFONAVIT_o_el_FOVISSSTE=('importe_pesos', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado50 = df_combinado50[df_combinado50['concepto'] == 101801006036]

    # Eliminación de columnas sobrantes
    columna_eliminar = ['concepto', 'claveinstitucion']
    df_combinado50 = df_combinado50.drop(columna_eliminar, axis=1)

    return df_combinado50
