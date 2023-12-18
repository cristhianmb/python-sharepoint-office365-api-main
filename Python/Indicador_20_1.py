#Numero de operaciones en Sucursales - 2022

import pandas as pd

def Indicador_20_1(df_hoja11_1, df_hoja2_1, df_hoja2):

    df69 = df_hoja11_1.copy()

    # Eliminar los dos últimos dígitos numéricos en la columna 'Año'
    df69['Column1'] = df69['Column1'] // 100
    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado101 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df69[['Column1', 'Column15','Column4', 'Column10']], how='left', left_on='claveinstitucion', right_on='Column4')

    # Agrupar y agregar según tus necesidades
    df_combinado101 = df_combinado101.groupby(['nombreinstitucion', 'claveinstitucion', 'Column1', 'Column10']).agg(
        numero_de_operaciones_en_Sucursales=('Column15', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado101 = df_combinado101[df_combinado101['Column1'] == 2022]
    df_combinado101 = df_combinado101[df_combinado101['Column10'] == 'Sucursal']

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado101 = df_combinado101.groupby('nombreinstitucion').agg(
        numero_de_operaciones_en_Sucursales=('numero_de_operaciones_en_Sucursales', 'mean')
    ).reset_index()

    return df_combinado101
