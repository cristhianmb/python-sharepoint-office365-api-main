# Saldo de la Cartera de crédito con riesgo de crédito Etapa 2 de Créditos adquiridos al INFONAVIT o el FOVISSSTE
import pandas as pd

def Indicador_13_9(df_hoja1, df_hoja2):
    df31 = df_hoja1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado49 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df31[['importe_pesos', 'institucion', 'concepto']], how='left', left_on='claveinstitucion', right_on='institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado49 = df_combinado49.groupby(['nombreinstitucion', 'claveinstitucion', 'concepto']).agg(
        Saldo_de_la_Cartera_de_crédito_con_riesgo_de_crédito_Etapa_de_Créditos_adquiridos_al_INFONAVIT_o_el_FOVISSSTE=('importe_pesos', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado49 = df_combinado49[df_combinado49['concepto'] == 101800607030]

    # Eliminación de columnas sobrantes
    columna_eliminar = ['concepto', 'claveinstitucion']
    df_combinado49 = df_combinado49.drop(columna_eliminar, axis=1)

    return df_combinado49
