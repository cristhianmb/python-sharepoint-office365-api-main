#Captación total



import pandas as pd

def Indicador_13_14(df_hoja1, df_hoja2):
    df36 = df_hoja1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado54 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df36[['importe_pesos', 'institucion', 'concepto']], how='left', left_on='claveinstitucion', right_on='institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado54 = df_combinado54.groupby(['nombreinstitucion', 'claveinstitucion', 'concepto']).agg(
        Captación_total=('importe_pesos', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado54 = df_combinado54[df_combinado54['concepto'] == 200000000000]

    # Eliminación de columnas sobrantes
    columna_eliminar = ['concepto', 'claveinstitucion']
    df_combinado54 = df_combinado54.drop(columna_eliminar, axis=1)

    return df_combinado54
