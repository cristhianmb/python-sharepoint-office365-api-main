#numero de operaciones en Comisionistas - 2022

import pandas as pd

def Indicador_20_6(df_hoja11_1, df_hoja2_1, df_hoja2):

    df75 = df_hoja11_1.copy()

    # Eliminar los dos últimos dígitos numéricos en la columna 'Año'
    df75['Column1'] = df75['Column1'] // 100
    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado107 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df75[['Column1', 'Column15','Column4', 'Column10']], how='left', left_on='claveinstitucion', right_on='Column4')

    # Agrupar y agregar según tus necesidades
    df_combinado107 = df_combinado107.groupby(['nombreinstitucion', 'claveinstitucion', 'Column1', 'Column10']).agg(
        numero_de_operaciones_en_Comisionistas=('Column15', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado107 = df_combinado107[df_combinado107['Column1'] == 2021]
    df_combinado107 = df_combinado107[df_combinado107['Column10'] == 'Comisionistas']

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado107 = df_combinado107.groupby('nombreinstitucion').agg(
        numero_de_operaciones_en_Comisionistas=('numero_de_operaciones_en_Comisionistas', 'mean')
    ).reset_index()

    return df_combinado107
