#Captación tradicional



import pandas as pd

def Indicador_13_13(df_hoja1, df_hoja2):
    df35 = df_hoja1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado53 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df35[['importe_pesos', 'institucion', 'concepto']], how='left', left_on='claveinstitucion', right_on='institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado53 = df_combinado53.groupby(['nombreinstitucion', 'claveinstitucion', 'concepto']).agg(
        Capacitaci�n_tradicional=('importe_pesos', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado53 = df_combinado53[df_combinado53['concepto'] == 200200001001]

    # Eliminación de columnas sobrantes
    columna_eliminar = ['concepto', 'claveinstitucion']
    df_combinado53 = df_combinado53.drop(columna_eliminar, axis=1)

    return df_combinado53
