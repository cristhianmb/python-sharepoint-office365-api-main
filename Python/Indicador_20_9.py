#numero de operaciones a traves de Banca por Internet - 2022

import pandas as pd

def Indicador_20_9(df_hoja11_1, df_hoja2_1, df_hoja2):
    df78 = df_hoja11_1.copy()

    # Eliminar los dos últimos dígitos numéricos en la columna 'Año'
    df78['Column1'] = df78['Column1'] // 100
    
    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado109 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df78[['Column1', 'Column15','Column4', 'Column10']], how='left', left_on='claveinstitucion', right_on='Column4')

    # Agrupar y agregar según tus necesidades
    df_combinado109 = df_combinado109.groupby(['nombreinstitucion', 'claveinstitucion', 'Column1', 'Column10']).agg(
        numero_de_operaciones_a_traves_de_Banca_por_Internet=('Column15', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado109 = df_combinado109[df_combinado109['Column1'] == 2022]
    df_combinado109 = df_combinado109[df_combinado109['Column10'] == 'Internet']

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado109 = df_combinado109.groupby('nombreinstitucion').agg(
        numero_de_operaciones_a_traves_de_Banca_por_Internet=('numero_de_operaciones_a_traves_de_Banca_por_Internet', 'mean')
    ).reset_index()
    
    return df_combinado109
