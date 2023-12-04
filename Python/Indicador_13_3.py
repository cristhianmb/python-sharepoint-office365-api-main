#Saldo Cartera de crédito con riesgo de crédito Etapa 3 Vivienda, Créditos adquiridos al INFONAVIT o el FOVISSSTE


import pandas as pd

def Indicador_13_3(df_hoja1, df_hoja2):
    df25 = df_hoja1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado43 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df25[['importe_pesos', 'institucion', 'concepto']], how='left', left_on='claveinstitucion', right_on='institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado43 = df_combinado43.groupby(['nombreinstitucion', 'claveinstitucion', 'concepto']).agg(
        Saldo_Cartera_de_crédito_con_riesgo_de_crédito_Etapa_Vivienda_Interés_Sociall=('importe_pesos', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado43 = df_combinado43[df_combinado43['concepto'] == 101800706020]

    # Eliminación de columnas sobrantes
    columna_eliminar = ['concepto', 'claveinstitucion']
    df_combinado43 = df_combinado43.drop(columna_eliminar, axis=1)

    return df_combinado43
