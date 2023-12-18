#numero de operaciones a traves de celular - 2022

import pandas as pd

def Indicador_20_12(df_hoja11_1, df_hoja2_1, df_hoja2):
    df82 = df_hoja11_1.copy()

    # Eliminar los dos últimos dígitos numéricos en la columna 'Año'
    df82['Column1'] = df82['Column1'] // 100
    
    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado112 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df82[['Column1', 'Column15','Column4', 'Column10']], how='left', left_on='claveinstitucion', right_on='Column4')

    # Agrupar y agregar según tus necesidades
    df_combinado112 = df_combinado112.groupby(['nombreinstitucion', 'claveinstitucion', 'Column1', 'Column10']).agg(
        numero_de_operaciones_a_traves_de_celular=('Column15', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado112 = df_combinado112[df_combinado112['Column1'] == 2021]
    df_combinado112 = df_combinado112[df_combinado112['Column10'] == 'Celular']

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado112 = df_combinado112.groupby('nombreinstitucion').agg(
        numero_de_operaciones_a_traves_de_celular=('numero_de_operaciones_a_traves_de_celular', 'mean')
    ).reset_index()

    return df_combinado112
