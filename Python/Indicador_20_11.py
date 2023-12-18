#numero de operaciones a traves de celular - 2022

import pandas as pd

def Indicador_20_11(df_hoja11_1, df_hoja2_1, df_hoja2):
    df81 = df_hoja11_1.copy()

    # Eliminar los dos últimos dígitos numéricos en la columna 'Año'
    df81['Column1'] = df81['Column1'] // 100
    
    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado111 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df81[['Column1', 'Column15','Column4', 'Column10']], how='left', left_on='claveinstitucion', right_on='Column4')

    # Agrupar y agregar según tus necesidades
    df_combinado111 = df_combinado111.groupby(['nombreinstitucion', 'claveinstitucion', 'Column1', 'Column10']).agg(
        numero_de_operaciones_a_traves_de_celular=('Column15', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado111 = df_combinado111[df_combinado111['Column1'] == 2022]
    df_combinado111 = df_combinado111[df_combinado111['Column10'] == 'Celular']

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado111 = df_combinado111.groupby('nombreinstitucion').agg(
        numero_de_operaciones_a_traves_de_celular=('numero_de_operaciones_a_traves_de_celular', 'mean')
    ).reset_index()

    return df_combinado111
