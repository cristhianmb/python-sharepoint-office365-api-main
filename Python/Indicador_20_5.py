#numero de operaciones en Comisionistas - 2022

import pandas as pd

def Indicador_20_5(df_hoja11_1, df_hoja2_1, df_hoja2):

    df74 = df_hoja11_1.copy()

    # Eliminar los dos últimos dígitos numéricos en la columna 'Año'
    df74['Column1'] = df74['Column1'] // 100
    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado106 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df74[['Column1', 'Column15','Column4', 'Column10']], how='left', left_on='claveinstitucion', right_on='Column4')

    # Agrupar y agregar según tus necesidades
    df_combinado106 = df_combinado106.groupby(['nombreinstitucion', 'claveinstitucion', 'Column1', 'Column10']).agg(
        numero_de_operaciones_en_Comisionistas=('Column15', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado106 = df_combinado106[df_combinado106['Column1'] == 2022]
    df_combinado106 = df_combinado106[df_combinado106['Column10'] == 'Comisionistas']

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado106 = df_combinado106.groupby('nombreinstitucion').agg(
        numero_de_operaciones_en_Comisionistas=('numero_de_operaciones_en_Comisionistas', 'mean')
    ).reset_index()

    return df_combinado106
