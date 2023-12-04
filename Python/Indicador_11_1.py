import pandas as pd

def Indicador_11_1(df_hoja1, df_hoja2):
    df15 = df_hoja1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado33 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df15[['importe_pesos', 'institucion', 'concepto']], how='left', left_on='claveinstitucion', right_on='institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado33 = df_combinado33.groupby(['nombreinstitucion', 'claveinstitucion', 'concepto']).agg(
        Saldo_de_la_Cartera_de_Consumo_con_riesgo_de_crédito=('importe_pesos', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado33 = df_combinado33[df_combinado33['concepto'] == 101800104003]

    # Eliminación de columnas sobrantes
    columna_eliminar = ['concepto', 'claveinstitucion']
    df_combinado33 = df_combinado33.drop(columna_eliminar, axis=1)

    return df_combinado33
