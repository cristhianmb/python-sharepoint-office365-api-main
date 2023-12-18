#numero de operaciones en Sucursales - 2021

import pandas as pd

def Indicador_20_3(df_hoja11_1, df_hoja2_1, df_hoja2):

    df71 = df_hoja11_1.copy()

    # Eliminar los dos últimos dígitos numéricos en la columna 'Año'
    df71['Column1'] = df71['Column1'] // 100
    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado103 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df71[['Column1', 'Column15','Column4', 'Column10']], how='left', left_on='claveinstitucion', right_on='Column4')

    # Agrupar y agregar según tus necesidades
    df_combinado103 = df_combinado103.groupby(['nombreinstitucion', 'claveinstitucion', 'Column1', 'Column10']).agg(
        numero_de_operaciones_en_ATMs=('Column15', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado103 = df_combinado103[df_combinado103['Column1'] == 2022]
    df_combinado103 = df_combinado103[df_combinado103['Column10'] == 'Cajero Automático']

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado103 = df_combinado103.groupby('nombreinstitucion').agg(
        numero_de_operaciones_en_ATMs=('numero_de_operaciones_en_ATMs', 'mean')
    ).reset_index()

    return df_combinado103
